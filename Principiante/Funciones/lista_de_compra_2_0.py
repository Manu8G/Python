



def main():
    lista_compra=["Pan", "Huevos", "Leche"]
    producto = input("¿Que desea comprar? (Q para salir)")

    while producto != "Q":

        if producto in lista_compra:
            print("¡¡{} ya esta en la lista de la compra!!".format(producto))

        else:
            lista_compra.append(producto)

        producto = input("¿Que desea comprar? (Q para salir)")

    archivo = open("compra.txt", "w")   # r para read, a para append(añadir cosas al final)
    archivo.write("\n".join(lista_compra))
    archivo.close()
    print("La lista de la compra contiene:")
    print(*lista_compra, sep="\n") # print("\n".join(lista_compra))

if __name__ == '__main__':
    main()
