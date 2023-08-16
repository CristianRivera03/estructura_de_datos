def convertir_m_km(metro):
    return metro / 1000

print('*' * 50)
dato = int(input('Ingrese la cantidad de metros a convertir a km: \n'))
print(f'La en metros equivalente a kilometros es {convertir_m_km(dato)}km')