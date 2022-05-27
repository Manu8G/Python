vocales = ["a", "e", "i", "o", "u"]
frase = "Hola estoy aprendiendo python"
num_vocales = 0

for item in frase:
    #print(item)
    if item in vocales:
        #print("He encontrado una {}".format(item))
        num_vocales+=1

print(num_vocales)

#------------------
print("\n--------------------------------------------\n")
num_repeticiones = int(input("¿Hasta que numero quieres contar?"))

for i in range(num_repeticiones):
    print(i+1)