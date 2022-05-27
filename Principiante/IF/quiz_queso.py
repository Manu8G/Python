texto = "Bienvenido al quiz de queso"
print(texto + "\n" + "-" * len(texto) + "\n")

puntuacion = 0
opcion = input("""Pregunta 1: ¿Que haces cuando ves una tabla de quesos?
A - No hago nada
B - Pruebo uno o varios
C - La devoro        
""")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones validas son A, B y C")
    exit()

# Pregunta DOS  ----       -----         -----           -----               -----               -----

opcion = input("""Pregunta 2: ¿Como te gustan las hamburguesas?
A - Sin queso
B - Con queso
C - Con queso y mas queso        
""")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones validas son A, B y C")
    exit()

# Pregunta TRES    ----       -----         -----           -----               -----               -----

opcion = input("""Pregunta 3: ¿Eres intolerante a la lactosa?
A - Si
B - A veces
C - No        
""")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones validas son A, B y C")
    exit()

if puntuacion >= 25:
    print("Eres un fanatico del queso")
elif puntuacion >= 15
    print("Te gusta el queso")
else:
    print("Felicidades no te gusta el queso")