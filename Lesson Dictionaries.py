
# Ejemplo 1

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# print(student)


# Ejemplo 2

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# print(student['age'])


# Ejemplo 3   Cuando no existe el key access da KeyError

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# print(studen['phone'])


# Ejemplo 4   Cuando no existe el key access pero se retorna un mensaje determinado

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# print(student.get('phone', 'Not included'))


# Ejemplo 5   Actualizar el dictionary

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# student['phone'] = '555-5555'
# student['name'] = 'Alejandro'

# print(student)


# Ejemplo 6   Actualizar el dictionary en una sola linea

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# student.update({'name': 'Alejandro', 'age': 20, "phone": '555-5555'})

# print(student)


# Ejemplo 7   Eliminar pares de valores del dictionary

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# del student['age']

# print(student)


# Ejemplo 8   Otra manera de eliminar pares de valores del dictionary pero manteniendo el valor eliminado

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# age = student.pop('age')

# print(student)
# print(age)


# Ejemplo 9   Contar cuantas keys tiene el dictionary

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# print(len(student))


# Ejemplo 10   Diferente informacion de las keys que tiene el dictionary

# student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

# print(student.keys())
# print(student.values())
# print(student.items())


# Ejemplo 11   Imprimir todas las keys que tiene el dictionary

student = {'name': 'John', 'age': 34, "courses": ['Math', 'History']}

for keys, values in student.items():

    print (keys, values)
