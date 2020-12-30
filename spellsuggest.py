# -*- coding: utf-8 -*-
import re

from trie import Trie
from levenshtein_damerau_threshold import dp_levenshtein_backwards, dp_restricted_damerau_backwards, dp_intermediate_damerau_backwards
import numpy as np

class SpellSuggester:

    """
    Clase que implementa el mÃ©todo suggest para la bÃºsqueda de tÃ©rminos.
    """

    def __init__(self, vocab_file_path):
        """MÃ©todo constructor de la clase SpellSuggester

        Construye una lista de tÃ©rminos Ãºnicos (vocabulario),
        que ademÃ¡s se utiliza para crear un trie.

        Args:
            vocab_file (str): ruta del fichero de texto para cargar el vocabulario.

        """

        self.vocabulary  = self.build_vocab(vocab_file_path, tokenizer=re.compile("\W+"))

    def build_vocab(self, vocab_file_path, tokenizer):
        """MÃ©todo para crear el vocabulario.

        Se tokeniza por palabras el fichero de texto,
        se eliminan palabras duplicadas y se ordena
        lexicogrÃ¡ficamente.

        Args:
            vocab_file (str): ruta del fichero de texto para cargar el vocabulario.
            tokenizer (re.Pattern): expresión regular para la tokenización.
        """
        with open(vocab_file_path, "r", encoding='utf-8') as fr:
            vocab = set(tokenizer.split(fr.read().lower()))
            vocab.discard('') # por si acaso
            return sorted(vocab)

    def suggest(self, term, distance="levenshtein", threshold=None):

        """MÃ©todo para sugerir palabras similares siguiendo la tarea 3.

        A completar.

        Args:
            term (str): tÃ©rmino de bÃºsqueda.
            distance (str): algoritmo de bÃºsqueda a utilizar
                {"levenshtein", "restricted", "intermediate"}.
            threshold (int): threshold para limitar la bÃºsqueda
                puede utilizarse con los algoritmos de distancia mejorada de la tarea 2
                o filtrando la salida de las distancias de la tarea 2
        """
        assert distance in ["levenshtein", "restricted", "intermediate"]

        results = {} # diccionario termino:distancia
        
        for word in self.vocabulary: 

            if(distance == "levenshtein"):
                if(threshold != None):
                    dist = dp_levenshtein_backwards(word, term, threshold)

                    if(dist <= threshold):
                        results[word] = dist
                else:
                    dist = dp_levenshtein_backwards(word, term)
                    results[word] = dist

            elif(distance == "restricted"):
                if(threshold != None):
                    dist = dp_restricted_damerau_backwards(word, term, threshold)

                    if(dist <= threshold):
                        results[word] = dist
                else:
                    dist = dp_restricted_damerau_backwards(word, term)
                    results[word] = dist

            elif(distance == "intermediate"):
                if(threshold != None):
                    dist = dp_intermediate_damerau_backwards(word, term, threshold)

                    if(dist <= threshold):
                        results[word] = dist
                else:
                    dist = dp_intermediate_damerau_backwards(word, term)
                    results[word] = dist

        return results

class TrieSpellSuggester(SpellSuggester):
    """
    Clase que implementa el mÃ©todo suggest para la bÃºsqueda de tÃ©rminos y aÃ±ade el trie
    """
    def __init__(self, vocab_file_path):
        super().__init__(vocab_file_path)
        self.trie = Trie(self.vocabulary)


    def dp_levenshtein_backwards_trie(self, x, threshold = 4):

        D = np.zeros((self.trie.get_num_states() + 1, len(x) + 1))

        for i in range(1, self.trie.get_num_states() + 1):
            D[i, 0] = D[self.trie.get_parent(i), 0] + 1

        for j in range(1, len(x) + 1):
            D[0, j] = D[0, j - 1] + 1


            for i in range(1, self.trie.get_num_states() + 1):
                D[i, j] = min(
                    D[self.trie.get_parent(i), j] + 1,
                    D[i, j - 1] + 1,
                    D[self.trie.get_parent(i), j - 1] + (self.trie.get_label(i) != x[j-1]) 
                )

            
            if(min(D[:, j]) > threshold):
                return threshold + 1

        
        return D[:, len(x)]

    def dp_restricted_damerau_backwards_trie(self, x, threshold = 4):

        D = np.zeros((self.trie.get_num_states() + 1, len(x) + 1))

        for i in range(1, self.trie.get_num_states() + 1):
            D[i, 0] = D[self.trie.get_parent(i), 0] + 1


        for j in range(1, len(x) + 1):
            D[0, j] = D[0, j - 1] + 1


            for i in range(1, self.trie.get_num_states() + 1):
                D[i, j] = min(
                    D[self.trie.get_parent(i), j] + 1,
                    D[i, j - 1] + 1,
                    D[self.trie.get_parent(i), j - 1] + (self.trie.get_label(i) != x[j-1]) 
                )


                if i > 1 and j > 1 and x[j - 2] == self.trie.get_label(i) and x[j - 1] == self.trie.get_label(self.trie.get_parent(i)):
                    D[i, j] = min(
                        D[i, j],
                        D[self.trie.get_parent(self.trie.get_parent(i)), j - 2] + 1
                    )

            
            if(min(D[:, j]) > threshold):
                return threshold + 1

        return D[:, len(x)]

    def dp_intermediate_damerau_backwards_trie(self, x, threshold = 4):

        D = np.zeros((self.trie.get_num_states() + 1, len(x) + 1))

        for i in range(1, self.trie.get_num_states() + 1):
            D[i, 0] = D[self.trie.get_parent(i), 0] + 1

        for j in range(1, len(x) + 1):
            D[0, j] = D[0, j - 1] + 1

            for i in range(1, self.trie.get_num_states() + 1):
                D[i, j] = min(
                    D[self.trie.get_parent(i), j] + 1,
                    D[i, j - 1] + 1,
                    D[self.trie.get_parent(i), j - 1] + (self.trie.get_label(i) != x[j-1]) 
                )

                if i > 1 and j > 1 and self.trie.get_label(self.trie.get_parent(i)) == x[j - 1] and self.trie.get_label(i) == x[j-2]:
                    D[i, j] = min(
                        D[i, j],
                        D[self.trie.get_parent(self.trie.get_parent(i)), j - 2] + 1
                    )
                if(i > 2 and j > 1 and self.trie.get_label(self.trie.get_parent(self.trie.get_parent(i))) == x[j - 1] and self.trie.get_label(i) == x[j - 2]):
                    D[i, j] = min(
                        D[i, j],
                        D[self.trie.get_parent(self.trie.get_parent(i)), j - 2] + 1
                    )
                if(i > 1 and j > 2 and self.trie.get_label(i) == x[j - 3] and self.trie.get_label(self.trie.get_parent(i)) == x[j - 1]):
                    D[i, j] = min(
                        D[i, j],
                        D[self.trie.get_parent(self.trie.get_parent(i)), j - 2] + 1
                    )

            if(min(D[:, j]) > threshold):
                return threshold + 1

        return D[:, len(x)]

    def suggest(self, term, distance="levenshtein", threshold=None):

        assert distance in ["levenshtein", "restricted", "intermediate"]

        if distance == "levenshtein":
            if (threshold != None):
                distances = self.dp_levenshtein_backwards_trie(term, threshold)
            else: 
                distances = self.dp_levenshtein_backwards_trie(term)

        elif distance == "restricted":
            if (threshold != None):
                distances = self.dp_restricted_damerau_backwards_trie(term, threshold)
            else: 
                distances = self.dp_restricted_damerau_backwards_trie(term)

        elif distance == "intermediate":
            if (threshold != None):
                distances = self.dp_intermediate_damerau_backwards_trie(term, threshold)
            else: 
                distances = self.dp_intermediate_damerau_backwards_trie(term)

        results = {} # diccionario termino:distancia


        if type(distances) is np.ndarray:
            for i in range(0, self.trie.get_num_states() + 1):
            
                if(self.trie.is_final(i) and distances[i] <= threshold ):
                    word = self.trie.get_output(i)
                    results[word] = distances[i]

        return results
    
if __name__ == "__main__":
    spellsuggester = TrieSpellSuggester("./corpora/quijote.txt")
    print(spellsuggester.suggest("alábese"))
    # cuidado, la salida es enorme print(suggester.trie)