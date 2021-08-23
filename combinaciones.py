"""Hola, Este programa fue creado para calcular el numero de combinaciones posibles que presenta el siguiente problema.
Problema: Se quiere saber cuantas combinaciones se puede obtener repartiendo n caramelos a m ninos.  """

import os

class Herramientas:
    def __init_(self,new_persons, new_word, new_fac):
        self.persons = new_persons
        self.word = new_word
        self.n = new_fac
    
    def Personas_Caramelos(persons):
        list_persons = []
        list_candy = []
        y = 1
        
        for x in range(1,persons+1):
            name = str(input(f'Ingrese el nombre de la personas {x}: '))
            list_persons.append(name)
        
        while y <= len(list_persons):
            a = list_persons[y-1]
            num_candies = int(input(f'Ingrese cuantos caramelos le dara a {a}: '))
            list_candy.append(num_candies)
            y = y +1
        
        dict_personcandy = dict(zip(list_persons,list_candy))
        return dict_personcandy
    
    def Factorial(n):
        fac = 1
        while n > 1:
            fac *= n
            n -= 1
        return fac
    
    def __repr__(self):
        return self.persons
    
    def __repr__(self):
        return self.word
    
    

persons = int(input('Cuantas personas son: '))

print(" ")

personcandy = Herramientas.Personas_Caramelos(persons)

os.system ("clear")  # limpio pantalla.
print(personcandy)

string = ''

for name,candy in personcandy.items():
    string += name[0]*candy

word = string

code = ''
for i in personcandy.values():
    code += i * '*' + '/'

a = code[0:]
n = a.count('/')
k = a.count('*')


print(f'{word} -> {a}')


m = k+(n-1)


combinacion = Herramientas.Factorial(m) / (Herramientas.Factorial(k)*(Herramientas.Factorial(m-k)))
print(f'El numero de combinaciones posibles son {m}C{k} = {combinacion}')
