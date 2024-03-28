#Implementar un algoritmo que permita adivinar un número dado de 1 a 100,
#preguntando en cada caso si el número es mayor, menor o igual.
import random #Se importa random, para poder utilizar la función randint.
if __name__ == "__main__":
    numero:int=random.randint(1,100) #Con la función random se solicita un número aleatorio entre 1 y 100 y se guarda en 'numero'.
    intento_numero:int=int(input("Intente adivinar. Escriba un número entre 1 y 100: ")) #Se solicita un número y se convierte en entero.
    while intento_numero!=numero: #Mientras que el número que se ingresa sea diferente al número aleatorio seleccionado, se pregunta lo siguiente:
        if intento_numero<numero:
            print("Ese no es el número, pruebe con uno mayor") #Si el número que se ingreso es menor a 'numero', se sugiere que se escriba uno mayor.
        else:
            print("Ese no es el número, pruebe con uno menor") #Sino, se sugiere que se escriba uno menor.
        intento_numero=int(input("Escriba otro número: ")) #Se pide que se escriba otro número y este ahora se guarda en 'intento_numero', para que ahora sea este quien se evalúe en el while.
    print("¡Felicidades! Adivinaste el número.") #Si el número ingresado no entró al while, es porque este es igual a 'numero'.