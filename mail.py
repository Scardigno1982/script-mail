import re
 
extracto ="""

Acá copiar el texto que nos buscó Google

"""
 
patron = re.compile(r'[\w\-\.]+@[\w\-\.]+\.+[a-zA-Z]{1,4}')

resultado = re.findall(patron, extracto)

print(len(resultado))

print()

for p in resultado:
 print(p)