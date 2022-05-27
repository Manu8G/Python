import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_MAP_OBJECTS = 11
my_position = [3,1]
map_objects = []
tail_length = 0
tail = []
end_game = False

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

while not end_game:
    os.system("cls")
    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="") #El end hace que en vez de poner un \n al final, no ponga nada

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    #if (coordinate_x == my_position[POS_X]) and (coordinate_y == my_position[POS_Y]):
                    #   map_objects.remove([coordinate_x, coordinate_y])
                    #Esta es mi version, la que esta comentada
                    #else:
                        #char_to_draw = "*"
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "O"
                    tail_in_cell = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"

            if (coordinate_x == my_position[POS_X]) and (coordinate_y == my_position[POS_Y]):
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length+=1

                if tail_in_cell:
                    end_game = True

            if char_to_draw == "#":
                print("###", end="")

            else:
                print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    #Ask the user where he wants to move
    #direction = input("¿Donde te quieres mover? [WASD]: ")
    if not end_game:
        direction = readchar.readchar().decode()
        new_position = None

        if direction == "w":
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

        elif direction == "a":
            new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

        elif direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

        elif direction == "d":
            new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

        elif direction == "q":
            end_game = True

        if new_position:
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                tail.insert(0, my_position.copy())
                tail = tail[:tail_length]
                my_position = new_position

    '''
    La funcion de readchar te devuelve un b'letra_que_has_metido' la b es de bit, 
    la cual se puede quitar si usamos direction.decode(), con esto te devolveria solo la letraque has metido
    sin las '' y sin la b 
    '''

    '''
    Para la cola lo que hacemos es guardar todas las posiciones por las que ha pasado la cabeza, y con esto
    y el tamaño de la cola ya podemos pintarla. Pero para mejorar esto vamos igualando la cola todo el rato
    a una nueva cola con el tamaño exacto de la misma que es lo que hacemos en el tail =  tail[:tail_length]
    '''

print("Fin del juego")