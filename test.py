from spellsuggest import TrieSpellSuggester
from spellsuggest import SpellSuggester


spellsuggester = TrieSpellSuggester("./corpora/quijote.txt")
res = spellsuggester.suggest("casa", "levenshtein", 1)
print(len(res))
print(res)
res = spellsuggester.suggest("casa", "restricted", 1)
print(len(res))
print(res)
res = spellsuggester.suggest("casa", "intermediate", 1)
print(len(res))
print(res)


spellsuggester = SpellSuggester("./corpora/quijote.txt")
res = spellsuggester.suggest("casa", "levenshtein", 1)
print(len(res))
print(res)
res = spellsuggester.suggest("casa", "restricted", 1)
print(len(res))
print(res)
res = spellsuggester.suggest("casa", "intermediate", 1)
print(len(res))
print(res)