

# Comparisons:

# Equal:              ==
# Not iqual:          !=
# Greater than        >
# Less than           <
# Greather or equal:  >=
# Less or equal:      <=
# Objetc identity:    is


# Ejemplo 1

# language = 'Java'

# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
# 	print('Laguage is Java')
# else:
#     print('No match')


# Boolean Operations
# and
# or
# not


# Ejemplo 2 Diferencia entre and y or

# user = 'Admin'
# user_loged = False

# if user == 'Admin' or user_loged:
#     print('Admin page')
# else:
#     print('Bad Creds')

# Ejemplo 3 Utilizar not, solamente cambia el sentido

# user_loged = False

# if not user_loged:
#     print('Plese log in')
# else:
#     print('Welcome')


# Ejemplo 4 Objetos diferentes en memoria

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a is b)
# print(id(a))
# print(id(b))


#False Value

# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = False

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')
