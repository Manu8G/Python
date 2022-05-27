
def medir_largos(iterable):
    def avisar(saludo):
        print(saludo)

    avisar("estamos en la funcion interna")

    if args:        # Las tuplas son como listas pero con menos funcionalidades y que ocupan menos memoria
        largos = [len(iterable)]    # Las tuplas son inmutables, no se les puede añadir informacion
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)

def main():
    print(medir_largos("hola"))
    # avisar("Estamos fuera de la funcion interna")
    # Esto daria error ya que la funcion avisar solo existe dentro de meri_largos

if __name__ == '__main__':
    main()