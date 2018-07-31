import random

# Letras mayusculas
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Letras minusculas
minus = "abcdefghijklmnopqrstuvwxyz"

# Digitos
num = "0123456789"

# Caracteres
carac = "-*?!@#$/()=.,;:"

# Tipos
tipo = ["mayus","minus","num","carac"]

contra = ""

for i in range(0,8):

    tip = random.choice(tipo)

    if tip=="mayus":
        c = random.choice(mayus)
    elif tip=="minus":
        c = random.choice(minus)
    elif tip=="num":
        c = random.choice(num)
    elif tip=="carac":
        c = random.choice(carac)

    contra = contra + c

print (contra)   

