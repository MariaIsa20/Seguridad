from socket import gethostbyname # importa la libreria socket y el método traduce
# un nombre de host a formato IPv4


def Miscript(): # funcion
	print("=[Welcome to Ip Scanner by: Hacking Live]=") #
	target = input("'./Enter the Host: '") # obtiene el nombre del host buscado
	targetIP = gethostbyname(target) # usa la funcion, retorna ipv4
	print ("Target IP =====>" + targetIP)
	print ("+------------------------------------+")
	#Miscript()
Miscript() # llamado a la funcion