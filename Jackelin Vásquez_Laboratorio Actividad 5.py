""""
# CASO NÚMERO 1
metros = int(input("Ingrese la cantidad de metros cúbicos: "))
habitantes = int(input("Ingrese la cantidad de habitantes en el departamento: "))

#consumo menor a 15
if metros < 15:
    tarifa = 5 * metros
    
#consumo entre 15 y 30
elif (metros >= 15 and metros <= 30):
    if habitantes > 3:
        tarifa = 4 * metros
    elif habitantes == 3:
        tarifa = 4.5 * metros
    else:
        tarifa = 5 * metros

else:  #consumo es mayo a 30
    if habitantes > 5:
        tarifa = 3.5 * metros
    elif habitantes % 2 == 0:
        tarifa = 4 * metros
    else:
        tarifa = 4.2 * metros
                
print ("el costo del consumo de agua es:", tarifa)
"""

#CASO NÚMERO 2
placa = input("Ingrese la placa del vehiculo: ")
año = int(input("Ingrese el año del vehículo: "))
año_actual = int(input("Ingrese el año actual: "))

#último dígito de la placa 
ultimo_digito_placa = int(placa[len(placa) - 1]) 
restricción = ""
# Verificar restricciones por año
if año >= 2001:
    # Restricción por último dígito 
    if ultimo_digito_placa in [0, 2, 4, 6, 8]:
        restricción = "No circula los días lunes."
    elif ultimo_digito_placa in [1, 3, 5, 7, 9]:
        restricción = "No circula los días viernes."

    # año par
    if año % 2 == 0:
        restricción += "Y los sábados solo puede circular hasta el mediodía."
else:
    restricción = "No tiene restricción alguna con respecto a circulación."

if año_actual - año > 25:
    restricción += " ¡Debe otorgar mantenimiento obligatorio por antigüedad del vehículo!"

print("La restricción de circulación es:", restricción)
        
