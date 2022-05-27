

def string_mas_larga( *argv):
    solucion = ""
    for i in argv:
        if len(solucion) < len(i):
            solucion = i

    return solucion

def main():
    print(string_mas_larga("Hola", "que tal, yo bien y tu", "biluliluloly", "Adios", "Pato"))

if __name__ == '__main__':
    main()