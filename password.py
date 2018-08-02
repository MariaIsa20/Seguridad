import random
length = int(input('Ingrese la longitud de la contraseña, mayor que 8:'))
elements='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdfghijklmopqrstuvwxyz!·$%&?_0123456789'
password = ''

if length>=8:
    while len(password)<int(length):

        password+=random.choice(elements)
else :
    print("longitud inválida")

print (password)