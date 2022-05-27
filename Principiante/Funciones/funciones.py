
def saludo_secreto(nombre):
    print("Hola {}".format(nombre[::-1]))   # El [::-1] le da la vuelta al string

nombre = input("Introduce tu nombre: ")
saludo_secreto(nombre)

# --------------

def largo_string(mi_string):    # esto es lo mismo que len, python built in functions
    largo = 0
    for n in mi_string:
        largo += 1

    return largo

mi_string = input("Introduce la palabra para ver cuantas letras tiene: ")
print("El numero de letras de la palabra es {}".format(largo_string(mi_string)))