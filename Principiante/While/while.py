respuesta = None
while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("¿Que opcion prefieres? (A, B o C)")

    if respuesta == "A":
        print("No esta mal")
    elif respuesta == "B":
        print("Podria ser mejor")
    elif respuesta == "C":
        print("Perfecto")
    else:
        print("Eso no me vale te lo vuelvo a repetir por si no lo has entendido")