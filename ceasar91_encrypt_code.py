# Codigo de encriptacion Cesar
# En criptografía, el cifrado César, también conocido como cifrado por 
# desplazamiento, código de César o desplazamiento de César, es una de las 
# técnicas de cifrado más simples y más usadas. Es un tipo de cifrado por 
# sustitución en el que una letra en el texto original es reemplazada por otra 
# letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. 
# Por ejemplo, con un desplazamiento de 3, la A sería sustituida por la D
# (situada 3 lugares a la derecha de la A), la B sería reemplazada por la E, etc. 
# Este método debe su nombre a Julio César, que lo usaba para comunicarse con sus 
# generales.

def cipher(ptext, key): # funcion
    ctext = "" 
    key %= 26 # llave para desplazar
    for i in ptext: # se itera sobre el texto
        if 64 < ord(i) < 91: # se verifica que este entre el alfabeto (a-z)
            if ord(i) + key > 90: # caso si el numero de codigo esta 
                # por fuera del alfabeto
                print("Ascii", ord(i)) 
                ctext += chr(ord(i) + key - 26) # convierte a caracter el
                # desplazamiento 
                print("ans", ord(i) + key - 26, chr(ord(i) + key - 26))
            else:
                ctext += chr(ord(i) + key) # cuando es menor
        else:
            if ord(i) + key > 122: # caso cuando se pasa de los caracteres alfabeticos
                ctext += chr(ord(i) + key - 26) 
            else:
                ctext += chr(ord(i) + key)
    return ctext


def plain(ctext, key):
    ptext = ""
    key %= 26
    for i in ctext:
        if 64 < ord(i) < 91:
            if ord(i) - key < 65:
                ptext += chr(ord(i) - key + 26)
            else:
                ptext += chr(ord(i) - key)
        else:
            if ord(i) - key < 97:
                ptext += chr(ord(i) - key + 26)
            else:
                ptext += chr(ord(i) - key)
    return ptext


while True:
    print("1.Encryption\n2.Decryption\n3.Exit")
    choice = int(input("Enter Your Choice:(1 or 2)"))
    if choice == 1:
        ptext = input("Enter plain text(only alphabets):")
        key = int(input("Enter key:"))
        if key % 26 == 0:
            print("Error Invalid Key")
        else:
            print(cipher(ptext, key))

    elif choice == 2:
        ctext = input("Enter cipher text(only alphabets):")
        key = int(input("Enter key:"))
        if key % 26 == 0:
            print("Error Invalid Key")
        else:
            ptext = plain(ctext, key)
            print(ptext)
    else:
        break