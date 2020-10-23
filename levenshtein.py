import numpy as np

def levenshtein_distance(x, y):
    D = np.zeros((len(x)+1,len(y)+1))    
    for i in range(1, len(x)+1):
        D[i,0] = D[i-1,0] + 1
    for j in range(1, len(y)+1):
        D[0,j] = D[0,j-1] + 1
        for i in range(1, len(x)+1):
            D[i,j] = min(D[i-1,j] + 1, D[i,j-1] + 1, D[i-1,j-1]+(x[i-1] != y[j-1]))
    print ("Distancia Levenhstein: ", D[len(x),len(y)])
    return 0

levenshtein_distance("algoritmo","lagortimo")

def levenshtein_restringida(x,y):
    D = np.zeros((len(x)+1,len(y)+1))    
    for i in range(1, len(x)+1):
        D[i,0] = D[i-1,0] + 1
    for j in range(1, len(y)+1):
        D[0,j] = D[0,j-1] + 1
    for i in range(1, len(x)+1):
        for j in range(1,len(y)+1):
            D[i,j] = min(D[i-1,j] + 1, D[i,j-1] + 1, D[i-1,j-1]+(x[i-1] != y[j-1]))
            if i and j and x[i-1]==y[j-2] and x[i-2]==y[j-1]:
                D[i,j] = min( D[(i,j)], D[i-2,j-2]+1)
    print ("Distancia Levenhstein restringida: ", D[len(x),len(y)])
    return 0

levenshtein_restringida("algoritmo","lagortimo")



'''FALTA SABER IMPLEMENTAR LA INTERMEDIA

def levenshtein_intermedia(x,y):
    D = np.zeros((len(x)+1,len(y)+1))    
    for i in range(1, len(x)+1):
        D[i,0] = D[i-1,0] + 1
    for j in range(1, len(y)+1):
        D[0,j] = D[0,j-1] + 1
    for i in range(1, len(x)+1):
        for j in range(1,len(y)+1):
            D[i,j] = min(D[i-1,j] + 1, D[i,j-1] + 1, D[i-1,j-1]+(x[i-1] != y[j-1]))
            if i and j and x[i-1]==y[j-2] and x[i-2]==y[j-1]:
                D[i,j] = min( D[(i,j)], D[i-2,j-2]+1)
    
    print (D[len(x),len(y)])
    return 0
'''
