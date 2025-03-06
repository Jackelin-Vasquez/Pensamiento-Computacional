"""
#1. Escribe un programa que extraiga la primera y la última palabra de una oración. Split()
texto= ("Python es un lenguaje poderoso")

texto_extraido= texto.split()

palabra_primera=texto_extraido[0]
palabra_ultima=texto_extraido [-1]

print("primera palabra:", palabra_primera)
print("última palabra:", palabra_ultima)
"""


"""
#2. Crea un programa que elimine los espacios repetidos en una cadena
texto= ("Hola  mundo  en Python")
texto_limpio= " ".join(texto.split())
print(texto_limpio)

"""


"""
#3. Dado un correo electrónico, extrae solo el dominio.

Correo= ("usuario@gmail.com")
correo_separado= Correo.split('@')[1]
print(correo_separado)
"""

"""
#4. Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf)

Archivo= ("documento.pdf")
extension= Archivo.endswith("pdf")

Archivo_2= ("image.jpg")
extension_2= Archivo_2.endswith("pdf")

print(extension)
print(extension_2)
"""

"""
#5. Dado un texto, invierte el orden de las palabras

Texto_1= ("Me gusta Phyton")
Texto_invertido= "".join(Texto_1.split()[::-1])
print(Texto_invertido)
"""

"""
#6. Dado un texto ingresado por el usuario detectar palabras claves y responder

poema= ("""Entre estrellas brillantes,
nuestros destinos se cruzaron.
Unidos por un hilo invisible,
el amor nos atrapó.""")

poema_2= ("""En tu mirada encuentro abrigo,
tu sonrisa es mi dulce suspiro.
En cada latido, mi corazón te nombra,
juntos, el amor es nuestro alfabeto.""")

cancion= ("Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podrá romperse el eje de la tierra Como un débil cristal")

cancion_2 = ("Porque soy feliz, aplaude si te sientes como una habitación sin techo. Porque soy feliz, aplaude, si sientes felicidad de verdad")

texto= input("ingrese un texto:").lower()
texto_separado= texto.lower().split()

if "poema".strip() in " ".join(texto_separado) or "amor".strip() in " ".join(texto_separado):
    print("Aquí tienes poemas de ejemplo:")
    print("1:", poema)
    print("2:",poema_2)
  
if "cancion".strip()in " ".join(texto_separado) or "alegria".strip() in " ".join(texto_separado):
    print("Aquí tienes canciónes de ejemplo:","1:", cancion,"2:", cancion_2)
    
"""
