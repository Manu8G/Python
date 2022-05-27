tipo = input("¿Prefieres IOS o Android?")

if tipo == "Android":
    dinero = input("¿Tienes dinero?")

    if dinero == "Si":
        camara = input("¿Te importa la camara?")

        if camara == "Si":
            print("Google Pixel supercamara")

        elif camara == "No":
            print("Android calidad-precio")

        else:
            print("Lo siento las opciones son Si o No")

    elif dinero == "No":
        print("Android chino 100€")

    else:
        print("Lo siento las opciones son Si o No")

elif tipo == "IOS":
    dinero = input("¿Tienes dinero?")

    if dinero == "Si":
        print("Iphone Ultra Pro Max")

    elif dinero == "No":
        print("Iphone segunda mano")

    else:
        print("Lo siento las opciones son Si o No")

else:
    print("Lo siento las opciones que tenemos son IOS o Android")