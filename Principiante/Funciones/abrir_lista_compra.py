def crear(nombre, lista_compra):
    archivo = open("{}.txt".format(nombre), "w")  # r para read, a para append(añadir cosas al final)
    archivo.write("\n".join(lista_compra))
    archivo.close()
    """
    with open("{}.txt".format(nombre), "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

    Esta estructura permite que aqui el archivo este cerrado y en la parte interior se pueda trabajar con el
    """


def main():
    lista_compra = []
    if input("¿Quieres cargar la ultima lista de la compra (S/N)? ") == "S":
        try:        # Intenta esto, si no funciona y da el error del except se ejecutara el except
            with open("listacompra.txt", "r") as mi_archivo:
                lista_compra = mi_archivo.read().split("\n")
        except FileNotFoundError:   # Si ponemos Exception vale para cualquier tipo de excepcion
            print("Archivo de la compra no encontrado")


    productos = ["pan", "leche", "donuts", "azucar", "aal", "huevos"]
    producto = input("¿Que desea comprar? (Q para salir, LISTA para mostrar la lista actual)")

    while producto != "Q":

        if producto == "LISTA":
            print("\n".join(lista_compra))

        elif producto.lower() in [i.lower() for i in lista_compra]:
            print("¡¡{} ya esta en la lista de la compra!!".format(producto))

        elif producto.lower() not in productos:
            print("No hay {} en la tienda en este momento".format(producto))

        else:
            lista_compra.append(producto)

        producto = input("¿Que desea comprar? (Q para salir, LISTA para mostrar la lista actual)")

    nombre = input("¿Como quieres que se llame el archivo?: ")
    crear(nombre, lista_compra)

if __name__ == '__main__':
    main()
