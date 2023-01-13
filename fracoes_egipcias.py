
# Python3 programa que mostra uma fração
# na forma egipcia usando algoritmo guloso
# Algorithm
 
import math
 
def fracaoEgipcia(nr, dr):
    """Funcao que irá mostrar uma função na forma egípcia usando algoritmo guloso.
    Cada fração positiva pode ser representada como soma de frações unitárias únicas. 
    Uma fração é fração unitária se o numerador for 1 e o denominador for um número 
    inteiro positivo, por exemplo, 1/3 é uma fração unitária. Tal representação é 
    chamada de Fração Egípcia, pois era usada pelos antigos egípcios.

    Complexidade: O(n)

    Parameters
    ----------
    nr: numerador da fracao
    dr: denominador da fracao
    """
 
    print("A fracao egipcia de {0}/{1} é ".format(nr, dr))
 
    # lista vazia para armazenar os denominadores
    ef = []
 
    # laco onde ira rodar ate o numerador for 0
    while nr != 0:
 
        # arredondando para cima
        x = math.ceil(dr / nr)
 
        # adicionando valor na lista de denominador
        ef.append(x)
 
        # atualizando novo nr e dr
        nr = x * nr - dr
        dr = dr * x
 
    # mostrando os valores
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print(" 1/{0} +" .
                    format(ef[i]), end = " ")
        else:
            print(" 1/{0}" .
                    format(ef[i]), end = "\n")
 
if __name__ == "__main__":
    fracaoEgipcia(6, 14)