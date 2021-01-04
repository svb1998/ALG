from spellsuggest import TrieSpellSuggester, SpellSuggester
import time
import collections
import re


#Comparar algoritmos mediante:
#    1. Variando la talla del diccionario
#    2. Variando el threshold

dicts = ["quijote_0_100.txt", "quijote_0_500.txt", "quijote_0_1000.txt"]
thresholds = [1, 2, 3, 5, 10, 20]

for dict in dicts:

    spellsuggester = SpellSuggester("./corpora/"+dict)
    trie_spellsuggester = TrieSpellSuggester("./corpora/"+dict)

    for threshold in thresholds:

        #Levenshtein
        t_ini = time.process_time()
        res = spellsuggester.suggest("casa", "levenshtein", threshold)
        t_end = time.process_time()
        print("[Distancia Levenshtein]                      -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        #Restringida
        t_ini = time.process_time()
        res = spellsuggester.suggest("casa", "restricted", threshold)
        t_end = time.process_time()
        print("[Distancia Levenshtein Restringida]          -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        #Intermedia
        t_ini = time.process_time()
        res = spellsuggester.suggest("casa", "intermediate", threshold)
        t_end = time.process_time()
        print("[Distancia Levenshtein Intermedia]           -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        #Con Trie
        t_ini = time.process_time()
        res = trie_spellsuggester.suggest("casa", "levenshtein", threshold)
        t_end = time.process_time()
        print("[Distancia Levenshtein Con Trie]             -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        t_ini = time.process_time()
        res = trie_spellsuggester.suggest("casa", "restricted", threshold)
        t_end = time.process_time()
        print("[Distancia Levenshtein Restringida Con Trie] -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        t_ini = time.process_time()
        res = trie_spellsuggester.suggest("casa", "intermediate", threshold)
        t_end = time.process_time()
        print("[Distancia Levenshtein Intermedia Con Trie]  -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

    print("----------------------------------------------------------")
