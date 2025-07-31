propietarios={}
vehiculos={}
numero_propietarios= int(input("Ingrese cantidad de propietarias a ingresar:"))
for i in range(numero_propietarios):
    print(f"---Propietario {i+1}---")
    nit=input("Ingrese número de nit")
    nombre_completo=input("Ingrese nombre completo de propietario:")
    telefono=input("Ingrese telefono de contacto:")
    cantidad_vehivulos=int(input("Ingrese cantidad de vehiculos:"))
    for vehiculo in range(cantidad_vehivulos):
        print(f"---DATOS DE VEHICULO {vehiculo +1}")
        placa= input("Ingrese placa de vehiculo:")
        marca= input("Ingrese marca de vehiculo:")
        modelo= input("Ingrese modelo de vehiculo")
        year= int(input("Ingrese año de vehiculo:"))
        impuesto= input("¿Tiene impuesto? Si/No:")

    propietarios[nit]={
        "nombre":nombre_completo,
        "tefelono":telefono,
        "cantidad_vehiculos":{
                "placa":placa,
                "marca":marca,
                "modelo":modelo,
                "año":year,
                "impuesto":impuesto

            }
    }

for propietarios,propietario in propietarios.items():
    print("---DATOS DE PROPIETARIOS---")
    print("---"*4)
    print(f"Nombre:{propietario["nombre"]}")
    print(f"Telefono:{propietario["telefono"]}")
    print(f"vehiculo:{propietario["cantidad_vehiculo"]}")
