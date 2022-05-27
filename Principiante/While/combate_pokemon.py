import random
import os

vida_feebas = 244
vida_magikarp = 244
VIDA_INICIAL_FEEBAS = 244
VIDA_INICIAL_MAGIKARP = 244

while vida_magikarp > 0 and vida_feebas > 0:

    # Turno de Feebas
    print("Turno de Feebas")
    ataque = random.randint(1, 3)

    if ataque == 1:
        poder = 0
        critico = 0
        print("Feebas uso Salpicadura")
        print("No paso nada...")

    elif ataque == 2:
        ataque = "Placaje"
        critico = random.randint(1, 2)
        poder = 40
        print("Feebas uso Placaje")
        vida_magikarp-=poder*critico

    elif ataque == 3:
        ataque = "Bote"
        critico = random.randint(1, 2)
        poder = (244 - vida_feebas)

        if poder == 0:
            poder = 1

        print("Feebas uso Bote")
        vida_magikarp -= poder * critico

    if vida_magikarp > 0:
        print("Magikarp [" + "#" * int((vida_magikarp / 244) * 50) + "-" * (50 - int((vida_magikarp / 244)
                * 50))+"]" + " ({}/244)".format(vida_magikarp))
        # Turno de Magikarp
        print("\nEs el turno de Magikarp")
        ataque = None
        ataque = input("¿Que quieres usar? (Salpicadura => S, Placaje => P, Bote => B)")

        while ataque != "S" and ataque != "P" and ataque != "B":
            ataque = input("Elige un ataque correcto por favor (Salpicadura => S, Placaje => P, Bote => B)")

        if ataque == "S":
            poder = 0
            critico = 0
            print("Magikarp uso Salpicadura")
            print("No paso nada...")

        elif ataque == "P":
            ataque = "Placaje"
            critico = random.randint(1, 2)
            poder = 40
            print("Magikarp uso Placaje")
            vida_feebas-=poder*critico

        elif ataque == "B":
            ataque = "Bote"
            critico = random.randint(1, 2)
            poder = (244 - vida_magikarp)+1
            print("Magikarp uso Bote")
            vida_feebas -= poder * critico

        if vida_feebas > 0:
            print("Feebas [" + "#" * int((vida_feebas / 244) * 50) + "-" * (50 - int((vida_feebas / 244) * 50))
                  + "]" + " ({}/244)".format(vida_feebas))
            input("Pulsa enter para continuar")
            os.system("cls") #Esto solo funciona enla ventana de la terminal, y dependiendo del SO
                            #debemos usar un comando u otro (cls, clear...)

if vida_feebas > 0:
    print("Feebas a ganado")

else:
    print("Magikarp a ganado")
