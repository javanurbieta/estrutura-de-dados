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
    for n in range(100, 1001, 100)


    print('Testando para entrada de tamanho 2')
    inicio = time()
    meu_max([1, 100])
    fim = time()
    tempo_de_execucao_em_segundos = int(fim - inicio)
    print('*' * (tempo_de_execucao_em_segundos +1))


