"""
#Ejercicio 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla
for i in range(0, 10):
    if i % 2 == 0:
        i+=1
        print(i+=1)
        
"""
"""
#Ejercicio 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. 

x=1 
while x < 11:
    if x % 2!=0:
        print(x)
    x += 1
"""
"""
#Escenario 1: La instrucción break se implementa para salir/terminar un bucle.
palabra_secreta = "chupacabras"
i= 0 

while i != palabra_secreta:
    palabra= input("Ingrese una palabra:")
    if palabra == palabra_secreta:
        print ( "Haz dejado el bucle con exito!")
        break
"""
#Escenario 2: La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.
user_word=input("ingrese una palabra:")
user_word=user_word.upper()
vocales= ("aeiou")

for vocales in user_word:
    
