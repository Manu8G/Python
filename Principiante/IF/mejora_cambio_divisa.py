dolar_euro = 0.91
libra_euro = 1.18

opcion = input("""¿Que desea?
    A - Convertir de dolar a euro 
    B - Convertir de euro a dolar
    C - Convertir de libra a euro
    D - Convertir de euro a libra\n""")

texto = "Introduzca la cantidad de {} a convertir: "
if opcion == "A":
    cantidad = float(input(texto.format("dolares")))
    print("La cantidad de euros es: {}".format(cantidad * dolar_euro))
elif opcion == "B":
    cantidad = float(input(texto.format("euros")))
    print("La cantidad de dolares es: {}".format(cantidad / dolar_euro))
elif opcion == "C":
    cantidad = float(input(texto.format("libras")))
    print("La cantidad de euros es: {}".format(cantidad * libra_euro))
elif opcion == "D":
    cantidad = float(input(texto.format("euros")))
    print("La cantidad de libras es: {}".format(cantidad / libra_euro))
else:
    print("La opcion escogida no es valida")