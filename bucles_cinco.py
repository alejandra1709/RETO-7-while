#Imprimir el factorial de un número natural n dado.
if __name__ == "__main__":
    numero:int=int(input("Escriba un número natural: ")) #Se solicita un número.
    n=numero #Se asigna el número a una variable.
    factorial:int=1 #Se inicia factorial en 1
    while n>0: #Mientras que n sea mayor que 0...
        factorial*=n #factorial toma el valor de factorial por n.
        n-=1 #Se le resta 1 a n.
    print("El factorial de",numero,"es",factorial)
