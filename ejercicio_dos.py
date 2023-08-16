def comparador (num_uno , num_dos):
    if num_uno > num_dos:
        print(f'El numero mayor es {num_uno}')
    else:
        print(f'El numero mayor es {num_dos}')
        
print('*' * 50)
num1 = int(input('Ingresa el primer dijito a ser comparado: '))
num2 = int(input('Ingresa el segundo dijito a ser comparado: '))
print('*' * 50)

comparador(num1,num2)