#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. 
#Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. 
#Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
if __name__ == "__main__":
    poblacion_A:int=25000000
    poblacion_B:int=18900000
    año:int=2022
    while poblacion_B<=poblacion_A: #Mientras que la población de B siga siendo menor o igual a la de A...
        poblacion_A=poblacion_A+0.02*poblacion_A #Se establecen la poblaciones del siguiente año, con base a las tasas de crecimiento.
        poblacion_B=poblacion_B+0.03*poblacion_B
        año+=1 #Se le suma 1 al año.
    print("En el año",año,"la población de B será mayor que la de A") #Cuando la población de B sea mayor a la de A, ya no se entrará al while, se llega a este punto y se escribe el año en el que esto sucedió.
    print("Población A:",poblacion_A,"- Población B:",poblacion_B) #Se imprimen las poblaciones de A y B para comprobar que la de B si es mayor que la de A.