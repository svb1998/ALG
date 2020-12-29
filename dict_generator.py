import collections
import re

n = 100 # Palabras a incluir en el diccionario
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

with open("./corpora/quijote_"+str(n)+".txt", "w", encoding='utf-8') as new_dict:
    new_dict.write(" ".join(sorted_vocab[0:n]))
