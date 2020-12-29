# -*- coding: utf-8 -*-
import re

reg = re.compile(r"(?P<term>\w+)\t(?P<threshold>\d+)\t(?P<numresul>\d+)\t(?P<dict>[^\n]*)")
entry = re.compile(r"(?P<dist>\d+):(?P<term>\w+)")

if __name__ == "__main__":
    fichero = "result_levenshtein_quijote.txt"
    with open(fichero, "r", encoding='utf-8') as fr:
        for line in fr:
            matchline = reg.match(line)
            term = matchline.group('term')
            threshold = int(matchline.group('threshold'))
            numresul = int(matchline.group('numresul'))
            resul = { g.group('term'):int(g.group('dist'))
                      for g in entry.finditer(matchline.group('dict')) }
            assert(numresul == len(resul))
            # en este punto puedes llamar a suggest con termino,
            # threshold y comprobar que devuelve un diccionario
            # similar a resul
            #
