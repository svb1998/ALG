from spellsuggest import TrieSpellSuggester

spellsuggester = TrieSpellSuggester("./corpora/quijote.txt")
res = spellsuggester.suggest("progremador", "levenshtein", 1)
print(len(res))
print(res)