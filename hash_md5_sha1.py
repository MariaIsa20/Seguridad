import hashlib

mensaje = str.encode(input('Ingresar mensaje:'))

# md5 
m = hashlib.md5()
m.update(mensaje)
print("Hash md5:")
print(m.hexdigest())

# sha1
s = hashlib.sha1()
s.update(mensaje)
print("Hash sha1:")
print(s.hexdigest())