import hashlib

mensaje = str.encode(input('Ingresar mensaje:'))

# md5 
m = hashlib.md5()
m.update(mensaje)
print(m.hexdigest())

# sha1
s = hashlib.sha1()
s.update(mensaje)
print(s.hexdigest())