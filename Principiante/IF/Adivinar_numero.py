# Adivinar un numero, con version estatica y version random
import random
numero=5
x=int(input("Adivina el numero entre 1 y 10: "))
if numero == x:
    print("Enhorabuena has acertado")
else:
    print("Lo siento has fallado")

print("Ahora el numero sera aleatorio")
numero=random.randint(1, 10)
x=int(input("Introduce el numero entre 1 y 10: "))
if x==numero:
    print("Enhorabuena has acertado")
else:
    print("Lo siento has fallado el numero era {}".format(numero))