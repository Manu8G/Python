import string

texto = input("Introduce un texto")
num_mayusculas = 0

for i in texto:
    if i in string.ascii_uppercase:         #Esta funcion devuelve una lista con todas las letras mayusculas
        num_mayusculas+=1

print("El numero de mayusculas en el texto es de {}".format(num_mayusculas))