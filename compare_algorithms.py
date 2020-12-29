from spellsuggest import TrieSpellSuggester, SpellSuggester
import time
import collections
import re


#Comparar algoritmos mediante:
#    1. Variando la talla del diccionario
#    2. Variando el threshold

dicts = ["quijote_0_100.txt", "quijote_0_500.txt", "quijote_0_1000.txt"]

for dict in dicts:

    spellsuggester = SpellSuggester("./corpora/"+dict)
    trie_spellsuggester = TrieSpellSuggester("./corpora/"+dict)

    #Levenshtein 
    t_ini = time.process_time()
    res = spellsuggester.suggest("casa", "levenshtein")
    t_end = time.process_time()
    print("[Distancia Levenshtein] -> Tiempo usando "+dict+":\t"+str(t_end-t_ini))

    #Restringida
    t_ini = time.process_time()
    res = spellsuggester.suggest("casa", "restricted")
    t_end = time.process_time()
    print("[Distancia Levenshtein Restringida] -> Tiempo usando "+dict+":\t"+str(t_end-t_ini))

    #Intermedia
    t_ini = time.process_time()
    res = spellsuggester.suggest("casa", "intermediate")
    t_end = time.process_time()
    print("[Distancia Levenshtein Intermedia] -> Tiempo usando "+dict+":\t"+str(t_end-t_ini))
    
    #Con Trie
    t_ini = time.process_time()
    res = trie_spellsuggester.suggest("progremador", "levenshtein", 1)
    t_end = time.process_time()
    print("[Distancia Levenshtein Con Trie] -> Tiempo usando "+dict+":\t"+str(t_end-t_ini))

    print("----------------------------------------------------------")