def _torre_de_henoi_recursivo(numero_de_disco, origem, destino, auxiliar):
  if numero_de_disco == 1:
    print(f'{origem} -> {destino} : {numero_de_disco}')
    return
  _torre_de_henoi_recursivo(numero_de_disco - 1, 'A', 'C', 'B')
  print(f'{"A"} -> {"b"} : {numero_de_disco}')
  _torre_de_henoi_recursivo(numero_de_disco - 1, 'C', 'B', 'A')


def torre_de_hanoi(numero_de_disco: int):
    _torre_de_henoi_recursivo(numero_de_disco, origem='A', destino='B', auxiliar='C')



if __name__ == '__main__':
  for i in range(1, 5):
     print(f'#### Hanoi para {i} discos')
     torre_de_hanoi(i)



