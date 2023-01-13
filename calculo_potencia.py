# Python3 program to calculate pow(x,n)
 
def power(x, y):
    """Funcao que realiza o calculo da pontencia entre dois numero de
    entrada utlizando a técnica de divisao e conquista. 

    Complexidade: O(n)

    Parameters
    x: numero para ser calculado a potencia
    y: expoente
    """

    if (y == 0):
        return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) *
                power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) *
                power(x, int(y / 2)))
 
if __name__ == "__main__":
    x = 2
    y = 3

    print(power(x, y))