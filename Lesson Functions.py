
# Forma de crear una funcion, no se puede dejar vacia se puede colocar pass

# def Hello_function():
#     pass


# def hello_function():
#     print('Hello World')


# hello_function()

# DRY   Dont Repeat Yourself

# Ejemplo 2 Otra manera

# Ejemplo 3  Encadenar funciones, dependen del type que retorna

#
# # Ejemplo 4  Utilizar parametros en la funcion


# def hello_function(greeting, adjetive):
#     return'{}, {} World!'.format(greeting, adjetive)


# print(hello_function('Hi', 'dear'))

# Ejemplo 5  Utilizar parametros por defecto
# Al llamar la funcion tengo tres casos
# Si no coloco parametro, coloca parametro por defecto.
# Si coloco un parametro diferente, utiliza ese parametro con el que llame la fucnion.
# Si no defino parametro por defecto, tengo que colocar parametro al llamar la funcion sino da error.


# def hello_function(greeting, name='Ale'):
#     return'{}, {}!'.format(greeting, name)


# print(hello_function('Hi'))


# Ejemplo 6 Argumentos posicionales y Keyword es una funcion,
# los parametros ingresado como textos y separados por comas los convierte en una tupla
# los parametros definido como llave y el valor, los convierte en un dictionary

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# student_info('Math', 'Art', 'Science', 2, name="Alejandro", age=33,)


# Ejemplo 7 Argumentos posicionales y Keyword es una funcion,
# Si tengo variables iguales a una lista y un dictionary y quiero colocarlos como argumento
# Para obtener el mismo resultado tengo que colocar * y ** para obtener los argumento posicional y keyword

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# courses = ['Math', 'Art', 'Science', 2]
# info = {'name': 'Alejandro', 'age': 33}

# student_info(*courses, **info)


# Ejemplo 8  Construccion de funcion para calcular los dias dias del mes tomando en cuenta los anos bisiesto


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    """Funcion que calcula cuuando un año es bisiesto"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Funcion que calcula los dia del mes, considerando año bisiesto"""

    if not 1 <= month <= 12:
        return "Invalid month"

    if leap_year(year) and month == 2:
        return 29

    else:
        return month_days[month]


print(days_in_month(2012, 2))
