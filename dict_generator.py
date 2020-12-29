import collections
import re

# Intervalo de palabras que se incluirán en el diccionario
b = 0   # Inicio del intervalo
n = 1000 # Final del intervalo
sorted_vocab = []

vocab_file_path = "./corpora/quijote.txt"
tokenizer = re.compile("\W+")
with open(vocab_file_path, "r", encoding='utf-8') as fr:
    c= collections.Counter(tokenizer.split(fr.read().lower()))
    if '' in c:
        del c['']
    reversed_c = [(freq, word) for (word, freq) in c.items()]
    sorted_reversed = sorted(reversed_c, reverse=True)
    sorted_vocab = [word for (freq, word) in sorted_reversed]

with open("./corpora/quijote_"+str(b)+"_"+str(n)+".txt", "w", encoding='utf-8') as new_dict:
    new_dict.write(" ".join(sorted_vocab[b:n]))
