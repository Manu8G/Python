
def medir_largos(iterable, *args, sumar_todo=False):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(iterable)

def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "Como", "QUe tal", sumar_todo=True))    # Si le pasaras solo el true lo detectaria como args

if __name__ == '__main__':
    main()