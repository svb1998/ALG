from spellsuggest import TrieSpellSuggester
import time
import collections
import re


#Comparar algoritmos mediante:
#    1. Variando la talla del diccionario
#    2. Variando el threshold

dicts = ["quijote_0_100.txt", "quijote_0_500.txt", "quijote_0_1000.txt"]

for dict in dicts:
    spellsuggester = TrieSpellSuggester("./corpora/"+dict)
    t_ini = time.process_time()
    res = spellsuggester.suggest("progremador", "levenshtein", 1)
    t_end = time.process_time()
    print("Tiempo usando "+dict+":\t"+str(t_end-t_ini))
