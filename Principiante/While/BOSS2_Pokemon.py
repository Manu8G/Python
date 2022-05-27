import readchar
import random
import os

POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 2
my_position = [3, 1]
map_objects = []
end_game = False
lose= False
champion = False

obstacle_definition = '''\
### ###             
### ###      ###    
### ###     #####   
###         #####   
#####       #####   
#####        ###    
#####               
#####               
####     ##      ###
###      ##         
##      ####    #   
#     ######    #   
#     ######    #   
#     #######   #   
#    #########      \
'''

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while len(map_objects) < NUM_MAP_OBJECTS:
    new_position = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

    if new_position not in map_objects and new_position != my_position and \
            obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
        map_objects.append(new_position)

while not end_game:
    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    combate = False

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")  # El end hace que en vez de poner un \n al final, no ponga nada

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            if (coordinate_x == my_position[POS_X]) and (coordinate_y == my_position[POS_Y]):
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    os.system("cls")
                    combate = True
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
                            vida_magikarp -= poder * critico

                        elif ataque == 3:
                            ataque = "Bote"
                            critico = random.randint(1, 2)
                            poder = (244 - vida_feebas)

                            if poder == 0:
                                poder = 1

                            print("Feebas uso Bote")
                            vida_magikarp -= poder * critico

                        if vida_magikarp > 0:
                            print("Magikarp [" + "#" * int((vida_magikarp / 244) * 50) + "-" * (
                                    50 - int((vida_magikarp / 244)
                                             * 50)) + "]" + " ({}/244)".format(vida_magikarp))
                            # Turno de Magikarp
                            print("\nEs el turno de Magikarp")
                            ataque = input("¿Que quieres usar? (Salpicadura => S, Placaje => P, Bote => B)")

                            while ataque != "S" and ataque != "P" and ataque != "B":
                                ataque = input(
                                    "Elige un ataque correcto por favor (Salpicadura => S, Placaje => P, Bote => B)")

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
                                vida_feebas -= poder * critico

                            elif ataque == "B":
                                ataque = "Bote"
                                critico = random.randint(1, 2)
                                poder = (244 - vida_magikarp) + 1
                                print("Magikarp uso Bote")
                                vida_feebas -= poder * critico

                            if vida_feebas > 0:
                                print("Feebas [" + "#" * int((vida_feebas / 244) * 50) + "-" * (
                                        50 - int((vida_feebas / 244) * 50))
                                      + "]" + " ({}/244)".format(vida_feebas))
                                input("Pulsa enter para continuar")
                                os.system("cls")  # Esto solo funciona enla ventana de la terminal, y dependiendo del SO
                                # debemos usar un comando u otro (cls, clear...)

                    if vida_feebas > 0:
                        print("Feebas a ganado")
                        end_game = True
                        lose = True

                    else:
                        print("Magikarp a ganado")

                    input("Pulsa enter para continuar")

            if combate:
                break
            elif char_to_draw == "#":
                print("###", end="")

            else:
                print(" {} ".format(char_to_draw), end="")

        if combate:
            break
        else:
            print("|")

    if combate:
        combate = False

        if len(map_objects) == 0:
            end_game = True
            champion = True

    else:
        print("+" + "-" * MAP_WIDTH * 3 + "+")

        if not end_game:
            direction = readchar.readchar().decode()
            directions = ["S", "W", "A", "D", "Q"]

            if direction not in directions:
                input("Para moverte debes usar S, W, A o D, o Q si quieres terminar el programa; pulsa enter para continuar")

            new_position = None

            if direction == "W":
                new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

            elif direction == "A":
                new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

            elif direction == "S":
                new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

            elif direction == "D":
                new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

            elif direction == "Q":
                end_game = True

            if new_position:
                if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                    my_position = new_position

if champion == True:
    print("\n\nEnhorabuena te has convertido en el campeon de la liga Pokemon!!")

elif lose == True:
    print("\n\nLo siento has perdido en la liga Pokemon :(")

else:
    print("\n\nFin del juego")
