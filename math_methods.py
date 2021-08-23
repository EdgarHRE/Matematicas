"""Programa para visualizar los diferentes tipos de OPeraciones de Conjuntos Matematicos. """

import os


#Funcion menu -> Muestra un menu al usuario, para elegir una opcion..
def menu():
    print('Nuestras opciones son: ')
    print('Opcion 1 obtener la Union de los conjuntos.')
    print('Opcion 2 obtener la Interseccion de los conjuntos.')
    print('Opcion 3 obtener la Diferencia de los conjuntos.')
    print('Opcion 4 obtener la Diferencia Simetrica de los conjuntos.')
    print('Opcion 5 conocer si el Subconjunto esta en el Conjunto de un set')


######################## Inicio del Programa ##################################

#Variable list_sets -> La Maquina guarda los sets  que el usuario ingreso.
list_sets = []

#Mensaje de Bienvenida.
print("Hola, Bienvenido en este programa podras visualizar los diferentes tipos de Conjutos")  

#Variable num_sets -> El usuario decide cuantos sets va a ingresar.
num_sets = int(input("Cuantos sets, va ingresar: "))

#for -> Se utiliza un para ingresar datos a los conjuntos que el usuario deseo crear.
for i in range(1,num_sets + 1): #for que va de 1 a el numero de set que ingreso el usario.
    set_elemento = set() # set vacio, para guardar los elementos que va ingresando el usuario.
    num_elemnt = int(input(f"De cuantos elementos es tu set {i}: ")) #El usuario ingresa el tamano del set
    #for -> Se utiliza para ingresar el numero de elementos en cada set, que el usuario creo.
    for j in range(1, num_elemnt + 1):  # for que va de 1 a el numero de elemento que el usario va a imgresar.
        elemnt = int(input(f'Ingresa el elemento {j}: ')) # numero de elemento 
        set_elemento. add(elemnt) # el elemento se agrega al set
    
    list_sets.append(set_elemento) # los set se agregan a la lista para guardarlos y utilizarlos mas adelante

os.system ("clear")  # limpio pantalla.

#variable user -> se crea una variable user para que la computadore entre por default al while.
user = 's'

#while-> Realizamos un while donde el usario interactuara con un menu para realizar diferentes opciones
while user == 's':
    
    #Funcion menu() -> de tipo vacio, sin retorno de variables.
    menu()
    
    #variable op -> La variable op representa la opcion del usuario que eligio.
    op = int(input("Eliga una opcion: "))
    os.system ("clear") 

    if op == 1:
        print(f'Tus conjuntos son los siguientes: {list_sets}')
        print('Cuales conjuntos te gustaria conocer su union:')
        union1 = int(input("Conjunto 1: "))
        union2 = int(input('Conjunto 2: '))
        resultado = list_sets[union1].union(list_sets[union2])
        print(f'La union de los conjuntos selecionados son: {resultado}')
    
    elif op == 2:
        print(f'Tus conjuntos son los siguientes: {list_sets}')
        print('Cuales conjuntos te gustaria conocer su intersection:')
        inter1 = int(input("Conjunto 1: "))
        inter2 = int(input('Conjunto 2: '))
        resultado = list_sets[inter1].intersection(list_sets[inter2])
        print(f'La interseccion de los conjuntos selecionados son: {resultado}')
    
    elif op == 3:
        print(f'Tu conjuntos son los siguientes: {list_sets}')
        print('Cuales conjuntos te gustaria conocer su diferencia:')
        dif1 = int(input("Conjunto 1: "))
        dif2 = int(input('Conjunto 2: '))
        resultado = list_sets[dif1].difference(list_sets[dif2])
        print(f'La diferencia de los conjuntos selecionados son: {resultado}')
	
    elif op == 4:
        print(f'Tu conjuntos son los siguientes: {list_sets}')
        print('Cuales conjuntos te gustaria conocer su diferencia simetrica:')
        sd1 = int(input("Conjunto 1: "))
        sd2 = int(input('Conjunto 2: '))
        resultado = list_sets[sd1].symmetric_difference(list_sets[sd2])
        print(f'Ladiferencia simetrica de los conjuntos selecionados son: {resultado}')
	
    else:
        print('Esta opcion no es valida')
        print('Porfavor ingrese una opcion valida...')
    
    user = input('Desea continuar... s/n: ')
    os.system ("clear") 


    







