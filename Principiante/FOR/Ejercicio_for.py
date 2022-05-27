#texto = "Hola, me llamo Manuel. ¿Tu como te llamas?"   -> 7 espacios, 1 coma, 1 punto
texto = input("Introduzca el texto a comprobar: ")

espacios = 0
comas = 0
puntos = 0

for i in texto:
    if i == " ":
        espacios+=1

    elif i == ",":
        comas+=1

    elif i == ".":
        puntos+=1

print("Espacios={}, comas={}, puntos={}".format(espacios, comas, puntos))