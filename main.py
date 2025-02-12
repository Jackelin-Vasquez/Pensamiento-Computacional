numero=int(input("ingrese un número natural que sea entre en 1 y 9:"))
resultado= ''


if numero<=3: 
    resultado= numero*I

elif numero >=5 :
    resultado= 'V'+(numero-5)*'I'
    
if numero ==  4:
    resultado= 'IV'
    
if numero == 9:
    resultado = 'IX'

if numero > 9:
    resultado=print("numero no valido")


print("El resultado es:", resultado)