""""
Desarrollo un programa 

"""

num = int(input('Ingrese el numero de elementos  que va a ingresar al dictionario: '))

series = {}

for i in range(1,num +1):
	serie = str(input('Ingresa el nombre de la serie: '))
	valor = int(input('Ingrese el valor de la serie:'))
	series[serie] = valor

print(series)

