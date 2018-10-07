
# Ejempo 1  Como importar un modulo creado en otro archivo .py
# En este caso se importa el modulo completo

# import my_module

# courses = ['History', 'Math', 'Physics', 'CompSci']


# index = my_module.find_index(courses, 'CompSci')

# print(index)


# Ejempo 2  Como importar un modulo creado en otro archivo .py
# En este se indica las funciones especificas que deseo importar del module

# from my_module import find_index, test

# courses = ['History', 'Math', 'Physics', 'CompSci']


# index = find_index(courses, 'CompSci')

# print(index)
# print(test)

# Ejempo 3  Como cambiar la ruta de donde va a encontrar el module.

# import sys

# print(sys.path)  #Con esto puedo visualizar cual es la ruta donde va a importar los module

# sys.path.append('/Users/alejandro/Desktop/Python Learning/Module')

# from my_module import find_index, test

# courses = ['History', 'Math', 'Physics', 'CompSci']


# index = find_index(courses, 'CompSci')

# print(index)
# print(test)


# Ejemplo 4. Instrucciones para cambiar el python path variable y dejar determinado de la ruta donde va a importar el modulo

# Estas intrucciones se ejecutan en la consola.
# nano ~/.bash_profile
# export PYTHONPATH="</ruta que se va a definir>"  #esto se hace la final de la pantalla
# Presiona Cntrl X y  despues 'Y' para guardar
# Reiniciar la terminal


# Ejemplo 5. Importar modulos o funciones de librerias estandar

# import random

# List = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# random_number = random.choice(List)

# print(random_number)


# # Ejemplo 6. Importar modulos o funciones de librerias estandar. Matematicas

# import math

# rads = math.radians(90)
# print(rads)

# sin = math.sin(rads)
# print(int(sin))


# Ejemplo 7. Importar modulos o funciones de librerias estandar. Manejar Fechas

# import datetime
# import calendar

# today = datetime.date.today()
# print(today)

# print(calendar.isleap(2016))


# Ejemplo 8. Importar modulos o funciones de librerias estandar. Informacion del sistema

import os


print(os.getcwd())

print(os.__file__)
