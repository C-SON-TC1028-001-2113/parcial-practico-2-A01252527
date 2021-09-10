
def main():
    
    #escribe tu código abajo de esta línea
    numero = int(input("Escribe un numero : "))
    answer = 1

    while answer**2<=numero:
        answer += 1
    
    print(answer)
if __name__=='__main__':
    main()
