
def medir_largos(iterable, *args):  # Un numero de argumentos indefinidos y opcionales. Esta variable es una tupla
    if args:        # Las tuplas son como listas pero con menos funcionalidades y que ocupan menos memoria
        largos = [len(iterable)]    # Las tuplas son inmutables, no se les puede añadir informacion
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)

def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "como", "estas", "yo bien")) #
    print(medir_largos(""))

if __name__ == '__main__':
    main()