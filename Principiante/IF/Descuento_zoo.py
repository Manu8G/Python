edad = int(input("Introduzca su edad: "))
carnet = input("Digame su tipo de carnet (E para estudiante, P para pensionista, F para familia numerosa, "
               "N para ninguno)")
if (25 <= edad <= 35 and carnet == "E") or edad < 10 or (edad >= 65 and carnet=="P") or carnet == "F":
    print("Se te aplica descuento")
else:
    print("No se te aplica descuento")