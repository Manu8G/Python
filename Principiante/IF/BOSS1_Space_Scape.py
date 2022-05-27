import random

print("Estas en una carcel alienigena, tienes que escapar asi que elige bien tus pasos")
opcion = input("Enfrente de ti hay dos opciones una puerta semiabierta o una escotilla en el suelo,"
               " ¿Que haces? (1 == puerta, 2 == escotilla)")
if opcion == "1":
    opcion = input("De la puerta sale un guardia armado, "
                   "¿Que haces? (1 == hacerme el muerto, 2 == correr)")

    if opcion == "1":
        print("Lo siento el guardia te ha matado")

    elif opcion == "2":
        print("Sigues corriendo y llegas a un hangar donde robas una nave y consigues escapar")

    else:
        print("Te quedas pensando y te mata el guardia")

elif opcion == "2":
    print("Caes a una alcantarilla por la cual caminas hasta llegar a una zona abierta")
    opcion = input("Encuentras un palo y un camino, ¿Que haces? (1 == coger el palo, 2 == no coger el palo)")
    palo = False

    if opcion == "1":
        palo = True

    print("Sigues por el camino y te encuentras con una rata de 2 metros que te pide el resultado "
                   "de una operacion aritmetica")
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    opcion = int(input("Rata: ¿Cuanto es {} * {}?".format(num1, num2)))

    if opcion == num1 * num2:
        print("Has acertado, eres demasiado inteligente no te puedo dejar escapar (La rata te mata)")

    else:
        print("Fallaste lo siento, sigue por este camino (la rata se aparta y deja ver una puerta "
              "la cual sigues)")

        opcion = input("Llegas al final del tunel y esta se desploma tras de ti, quedas atrapado y solo"
                       "ves una alcantarilla por la cual escapar, \n ¿Que haces? (1 == esperar por ayuda,"
                       " 2 == probar la alcantarilla)")
        if opcion == "1":
            print("Aparecen las crias de la rata gigante y te devoran")

        elif opcion == "2":
            print("La alcantarilla esta atascada, si solo tuvieras un palo...")

            if palo == True:
                print("Usas el palo y consigues abrir la alcantarilla, la sigues hasta el final. Esta "
                      "desembocaba en una explanada por fin eres libre")

            else:
                print("Como no tienes palo te toca esperar, pero nunca llega nadie y para colmo "
                      "aparecen las crias de la rata gigante y te devoran")
        else:
            print("Te quedas pensando demasiado tiempo y aparecen las crias de la rata gigante y te devoran")

else:
    print("Te quedas pensando tanto tiempo que te acaban descubriendo (Mueres)")