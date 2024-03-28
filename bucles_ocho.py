#Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

def primo (num:int)->bool: #función que recibe un entero y devuelve un boleano.
    j:int=2 #variable entera que inicia en 2 pero irá aumentando y se comportará como divisor.
    if num==2: #Si el número que se recibe es 2, se devuelve un True, porque 2 sí es primo pero no se puede evaluar al igual que los demás.
        return True
    while j<num: #Mientras que el divisor sea menor al número...
        if num%j==0:
            break #Si el residuo de la división entre el número y j es 0, se sale del bucle, porque ya se sabe que no es primo.
        j+=1 #Se suma 1 a j para que se evalúe el siguiente número.
        if j==num: #Si se llegó a este punto y j es igual al número, significa que ya se evaluaron todos los números naturales menores que número y ninguno es su divisor, por lo cual el número es primo.
            return True #Se devuelve el True.

if __name__ == "__main__":
    i:int=1 #variable entera que inicia en 1 e irá aumentando.
    while i<=100: #Mientras que i sea menor o igual que 100...
        p=primo(i) #Se evalúa la función primo con el argumento i y se guarda en p.
        if p==True:
            print(i) #Si lo que retornó la función es True, el número es primo, así que se imprime.
        i+=1 #Se suma 1 a i para continuar con el siguiente número.