
# Ejemplo 1  Ejecutar para todos los elementos de una lista

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     print(num)

# Ejemplo 2  Realizar un alto en la iteracion del loop

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('Found!')
#         break
#     print(num)


# Ejemplo 3 Ignorar o saltar un elemento en la iteracion

nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)


# Ejemplo 4  Loop anidados

# for num in nums:
#     for letter in "abc":
#         print(num, letter)

# Ejemplo 5  Iteracion en un rango definido

# for i in range(1, 10):
#     print(i)

# Ejemplo 6 While sirve para iterar hasta que se cumpla una condicion

# x = 0

# while x < 12:
#     print(x)
#     x += 1

# Ejemplo 7 While sirve para iterar hasta que se cumpla una condicion, otra manera

x = 0

while True:
    print(x)
    if x == 5:
        break
    x += 1

# Un loop infinito se puede interrumpir con Ctrl + C