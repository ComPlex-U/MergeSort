from time import clock
from random import randrange
import statistics
# mergesort cython
def MergeSort(lista):
    # print ("split :: ", lista)
    if len(lista) > 1:
        mid = len(lista) // 2
        metadeEsq = lista[:mid]
        metadeDir = lista[mid:]

        MergeSort(metadeEsq)
        MergeSort(metadeDir)

        i = 0
        j = 0
        k = 0

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
                i += 1
                k += 1

            while j < len(metadeDir):
                lista [k] = metadeDir [j]
                j += 1
                k += 1
            #PRINT ("merge :: ", lista)

def teste( numeroListas,  tamanho,interacoes, incremento):
    fMedia = open('MergeSort_Media_CythonV2.txt', 'w')
    fDesvio = open('MergeSort_Desvio_CythonV2.txt', 'w')
    for z in range(interacoes):
                print ("interacoes n.", z +1)
                tempos = []
                for k in range (numeroListas):
                    lista = []
                    for i in range(tamanho):
                        num = randrange(1000)
                        lista.append(num)
                    print("lista não-organizada :: {1}".format((k+1, lista)))
                    print("lista N.{} de tamanho :: {}".format((k+1, tamanho)))
                    tempo1 = clock()
                    MergeSort(lista)
                    tempo2 = clock()

                    tempos. append(tempo1-tempo2)

                    print("listaorganizada :: {1}".format(k+1, lista))
                    print("tempo organizado ::{}s\n".format(tempo2 - tempo1))
                    del lista[:]

                print("\nMedia para {1} elementos ::{0}s".format(statistics.mean(tempos), tamanho))
                print("desvio padrao para {1} elementos ::{0}s\n".format(statistics.stdev(tempos), tamanho))

                sM = '{} {}\n'. format(tamanho, statistics.mean(tempos))
                sD = '{} {}\n'.format(tamanho, statistics.stdev(tempos))
                fMedia.write(sM)
                fDesvio.write(sD)
                tamanho += incremento
                fMedia.close()
                fDesvio.close()
numeroListas = 5
tamanhoListas = 5
interacao = 3
incremento = 100
teste(numeroListas, tamanhoListas, interacao, incremento)


