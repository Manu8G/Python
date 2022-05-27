numero = int(input("Introduzca un numero para calcular su tabla de multiplicar: "))

for i in range(1, 11):
    if (numero * i) % 2 == 0:  #Lo mas eficiente seria hacer i % 2 == 0, ya que cualquier cosa por dos es par
        print("{} * {} = {}".format(numero, i, numero*i))