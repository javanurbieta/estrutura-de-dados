from math import inf
from time import time

def meu_max(interavel):
    numero_maximo = -inf
    for numero in interavel:
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo

if __name__ == '__main__':
    print(meu_max([1]))
    print(meu_max([1, 100]))

    print('Estudo Experimental sobre o tempo da função max')
    inicio = 10000000
    for n in range(0, inicio * 20+1, inicio):
     inicio = time()
     meu_max(range(n))
     fim = time()
     tempo_de_execucao_em_segundos = fim - inicio
     print('*' * int(tempo_de_execucao_em_segundos *10), n)





