# Realizando pruebas con los print

var1 = int(input("Introduce el primer numero: "))
var2 = int(input("Introduce el segundo numero: "))
var3 = int(input("Introduce el tercer numero: "))

print("El maximo de los tres numero es " + str(max(var1, var2, var3)))
print("El minimo de los tres numero es " + str(min(var1, var2, var3)))

print(max(var1, var2, var3))
print(min(var1, var2, var3))

print("El maximo de los tres numero es {}".format(max(var1, var2, var3)))
print("El minimo de los tres numero es {}".format(min(var1, var2, var3)))

print("El maximo numero entre {}, {} y {} es {}".format(var1, var2, var3, max(var1, var2, var3)))
print("El minimo numero entre {}, {} y {} es {}".format(var1, var2, var3, min(var1, var2, var3)))

# Si en la primera serie de prints no ponemos el str(), nos dara un fallo pero en la segunda no hace falta
# ya que no se une int con string
