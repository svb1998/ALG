# -*- coding: utf-8 -*-
from spellsuggest import SpellSuggester

if __name__ == "__main__":
    spellsuggester = SpellSuggester("./corpora/quijote.txt")
    for distance in ['levenshtein','restricted','intermediate']:
        destiny =  f'result_{distance}_quijote.txt'
        with open(destiny, "w", encoding='utf-8') as fw:
            for palabra in ("casa", "senor", "jabón", "constitución", "ancho",
                            "savaedra", "vicios", "quixot", "s3afg4ew"):
                for threshold in range(1, 6):
                    resul = spellsuggester.suggest(palabra,distance=distance,threshold=threshold)
                    numresul = len(resul)
                    resul = " ".join(sorted(f'{v}:{k}' for k,v in resul.items()))
                    fw.write(f'{palabra}\t{threshold}\t{numresul}\t{resul}\n')