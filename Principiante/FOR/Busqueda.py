'''
lista_numeros = []
numero = input("Introduce un numero(Q para terminar): ")

while  numero != "Q":
    lista_numeros.append(int(numero))
    numero = input("Introduce un numero(Q para terminar): ")

num_max = -9999
num_min = 9999

for i in lista_numeros:
    if num_min > i:
        num_min = i
    elif num_max < i:
        num_max = i

print("El numero maximo es {}, y el minimo {}".format(num_max, num_min))
'''
#FORMA 2

print("\n------------------------------------------------\n")

lista_numeros = []
numeros = input("Introduce los numeros separados por comas: ")
#lista_numeros = numeros.split(",")  #Crea una lista dividiendo lo del string en elementos extrallendolos q lo que esta entre comas
lista_numeros = [int(numero) for numero in numeros.split(",")] #list comprehesion, esto aplica un filtro a una lista

num_max = lista_numeros[0]
num_min = lista_numeros[0]

for i in lista_numeros[1:]: #Esto hace que empiece a partir del elemento en la posicion 1 no en la posicon 0, ya que el de la posicion 0 ya lo hemos asignado antes
    if num_min > i:         #Si hacemos [1:3] iria desde la posicion 1 a la 3
        num_min = i

    elif num_max < i:
        num_max = i

print("El numero maximo es {}, y el minimo {}".format(num_max, num_min))

