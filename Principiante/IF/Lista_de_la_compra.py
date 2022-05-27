
lista_compra=[]

producto = input("¿Que desea comprar? (Q para salir)")

while producto != "Q":
    if producto in lista_compra:
        print("¡¡{} ya esta en la lista de la compra!!".format(producto))

    else:
        confirmacion = input("¿Seguro que quieres comprar {}? (S == si, N == no)".format(producto))

        while confirmacion != "S" and confirmacion != "N":
            print("Las opcioines validas son S y N, te lo volvere a repetir")
            confirmacion = input("¿Seguro que quieres comprar {}? (S == si, N == no)".format(producto))

        if confirmacion == "S":
            lista_compra.append(producto)
            print("Se añadio {} a la lista de la compra".format(producto))

        else:
            print("No se añadio {} a la lista de la compra".format(producto))
    producto = input("¿Que desea comprar? (Q para salir)")

print("La lista de la compra contiene:")
print(*lista_compra, sep="\n")
#print(lista_compra)

#for element in range(len(lista_compra)):
 #   print("\t {}".format(lista_compra[element]))

#for element in lista_compra:
 #   print("\t {}".format(element))