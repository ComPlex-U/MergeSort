from time import clock
from random import randrange
import statistics
# mergesort cython
cdef MergeSort(list lista):
    # print ("split :: ", lista)
    cdef int mid
    cdef list metadeEsq
    cdef list metadeDir
    cdef int i = 0
    cdef int j = 0
    cdef int k = 0

    if len (lista)> 1 :
        mid = len(lista) //2
        metadeEsq = lista [:mid]
        metadeDir = lista [mid:]

        MergeSort(metadeEsq)
        MergeSort(metadeDir)
        while i < len(metadeEsq) and j <  len(metadeDir):
            if metadeEsq[i] < metadeDir[j]:
                lista[k] = metadeEsq[i]
                i += 1
            else:
                lista[k]= metadeDir[j]
                j+= 1
            k+=1
        while i < len(metadeEsq):
            lista [k] = metadeEsq [i]
            i +=1
            k +=1
        while j < len(metadeDir):
            lista [k] = metadeDir [j]
            j +=1
            k +=1
        #PRINT ("merge :: ", lista)

    #codigo para testar
    cpdef teste (int numeroListas, int tamanho, int interacoes):
        fMedia = open('MergeSort_Media_Cython.txt', 'w')
        fDesvio = open('MergeSort_Desvio_Cython.txt', 'w')

        cdef int z
        cdef int k
        cdef int num
        cdef list tempos = []
        cdef list lista = []

        for z in range(interacoes):
            print ("interacoes n.", z +1)
            for k in range (numeroListas):
                for i in range(tamanho):
                    num = randrange(1000)
                    lista.append(num)
                #print ('Array
