from spellsuggest import TrieSpellSuggester, SpellSuggester
import time
import collections
import re


#Comparar algoritmos mediante:
#    1. Variando la talla del diccionario
#    2. Variando el threshold

dicts = ["quijote_0_100.txt", "quijote_0_500.txt", "quijote_0_1000.txt", "quijote_0_20000.txt", "quijote_0_40000.txt"]
thresholds = [0, 1, 2, 3, 5]


print("Levenshtein \t\t Levenshtein Restringida \t\t Levenshtein Intermedia \t\t Levenshtein Con Trie \t\t Levenshtein Restringida Con Trie \t\t Levenshtein Intermedia Con Trie")

for dict in dicts:

    spellsuggester = SpellSuggester("./corpora/"+dict)
    trie_spellsuggester = TrieSpellSuggester("./corpora/"+dict)

    for threshold in thresholds:

        #Levenshtein
        t_ini_lev = time.process_time()
        res = spellsuggester.suggest("casa", "levenshtein", threshold)
        t_end_lev = time.process_time()
        #print("[Distancia Levenshtein]                      -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        #Restringida
        t_ini_lev_res = time.process_time()
        res = spellsuggester.suggest("casa", "restricted", threshold)
        t_end_lev_res = time.process_time()
        #print("[Distancia Levenshtein Restringida]          -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        #Intermedia
        t_ini_lev_int = time.process_time()
        res = spellsuggester.suggest("casa", "intermediate", threshold)
        t_end_lev_int = time.process_time()
        #print("[Distancia Levenshtein Intermedia]           -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        #Con Trie
        t_ini_lev_trie = time.process_time()
        res = trie_spellsuggester.suggest("casa", "levenshtein", threshold)
        t_end_lev_trie = time.process_time()
        #print("[Distancia Levenshtein Con Trie]             -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        t_ini_res_trie = time.process_time()
        res = trie_spellsuggester.suggest("casa", "restricted", threshold)
        t_end_res_trie = time.process_time()
        #print("[Distancia Levenshtein Restringida Con Trie] -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))

        t_ini_int_trie = time.process_time()
        res = trie_spellsuggester.suggest("casa", "intermediate", threshold)
        t_end_int_trie = time.process_time()
        #print("[Distancia Levenshtein Intermedia Con Trie]  -> Tiempo usando "+dict+" y threshold: " + str(threshold)+":\t"+str(t_end-t_ini))


        print(str(t_end_lev - t_ini_lev) + " \t\t " + str(t_end_lev_res - t_ini_lev_res) + " \t\t " + str(t_end_lev_int - t_ini_lev_int) + " \t\t " + str(t_end_lev_trie - t_ini_lev_trie) + " \t\t " + str(t_end_res_trie - t_ini_res_trie) + " \t\t " + str(t_end_int_trie - t_ini_int_trie) )    
    

    print("----------------------------------------------------------")
