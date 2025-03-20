saldo = 3000
intentos = 0

print("Saldo actual: Q", saldo)

while True:
    monto = input("Ingrese monto a retirar: ").strip()

    if monto == "0":  # Si se ingresa 0, termina el programa
        print("Adiós.")
        break

    # Verificar si la entrada es válida (sin negativos, decimales ni espacios y no vacía)
    if monto.count("-") > 0 or monto.count(".") > 0 or monto.count(" ") > 0 or monto == "":
        print("Entrada inválida. Intente de nuevo.")
        continue

    monto = int(monto)

    #si el saldo es suficiente
    if monto > saldo:
        intentos += 1
        print(f"Saldo insuficiente. Intentos restantes: {3 - intentos}")
        if intentos >= 3:
            print("Demasiados intentos. Adiós.")
            break
    else:
        saldo -= monto  # Retiro de monto
        if saldo == 0:  # Si después del retiro el saldo es 0
            print("Retiro exitoso. Saldo agotado. Adiós.")
            break
        else:
            print(f"Retiro exitoso. Nuevo saldo: Q",saldo)