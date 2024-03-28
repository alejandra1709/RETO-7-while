#Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
if __name__ == "__main__":
    numero:int=int(input("Ingrese un número natural entre 2 y 50: ")) #Solicita un número, lo convierte a entero y lo guarda en 'numero'.
    i:int=1 #Variable de tipo entero que inicia en 1.
    print("Los divisores de",numero,"son:")
    while i<=numero: #Mientras que i sea menor o igual al número que se ingreso...
        if numero%i==0: #Se evalúa si el residuo de el número entre i es 0, si este es 0, i es un divisor de numero.
            print(i) #Se imprimen los divisores.
        i+=1 #Se suma 1 a i para evaluar si el siguiente número es divisor.