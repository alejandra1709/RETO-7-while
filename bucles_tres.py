#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
if __name__ == "__main__":
    num:int=int(input("Ingrese un número natural ≥ 2 desde el cual se iniciará la lista de números pares de forma descendente hasta 2: ")) #Se solicita un número 'num'.
    if (num%2!=0): #Si num es impar se le resta 1 para que sea el número par anterior a este.
        num-=1
    while (num>=2): #Mientras que num es mayor o igual a 2...
            print(num) #Se imprime num.
            num-=2 #Se resta dos a num para pasar al anterior número par.