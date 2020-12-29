# -*- coding: utf-8 -*-
import re

from trie import Trie
from levenshtein_damerau_threshold import dp_levenshtein_backwards, dp_restricted_damerau_backwards, dp_intermediate_damerau_backwards

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
    
if __name__ == "__main__":
    spellsuggester = TrieSpellSuggester("./corpora/quijote.txt")
    print(spellsuggester.suggest("alÃ¡bese"))
    # cuidado, la salida es enorme print(suggester.trie)