
def seguro():
    var = input("¿Estas seguro (S/N)?: ")
    if var == 'S':
        return True

    elif var == 'N':
        return False

    else:
        return -1

def main():
    print(seguro())

if __name__ == '__main__':
    main()