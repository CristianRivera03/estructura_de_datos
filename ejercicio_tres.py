def pedir_numeros():
    i = 0
    lista = []

    while i < 5:
        numero = int(input('ingrese un numero para añadirlo a la lista: \n'))
        lista.append(numero)
        i += 1

    return lista


def ordenar_lista_ascendente(input_list):
    lista_ordenada = []
    copia_lista = input_list.copy()
    while copia_lista:
        minimo = min(copia_lista)  # Obtener el mínimo de la copia de la lista
        lista_ordenada.append(minimo)
        copia_lista.remove(minimo)
    return lista_ordenada


def ordenar_lista_descendente(input_list):
    lista_ordenada = []
    copia_lista = input_list.copy()
    while copia_lista:
        maximo = max(copia_lista)  # Obtener el mínimo de la copia de la lista
        lista_ordenada.append(maximo)
        copia_lista.remove(maximo)
    return lista_ordenada


lista_original = pedir_numeros()
lista_descendente = ordenar_lista_descendente(lista_original)
lista_ascendente = ordenar_lista_ascendente(lista_original)

print(f'')
print(f'''
      {'*' * 80}
      la lista original es: {lista_original}
      la lista ascendente quedaria de la siguiente manera {lista_ascendente}
      la lista descendente quedaria de la siguiente manera {lista_descendente}
      {'*' * 80}
      ''')
