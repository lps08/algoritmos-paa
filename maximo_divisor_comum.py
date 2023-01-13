def mdc(a, b):
    """Funcao recursiva para encontrar o maximo divisor comum
    utilizando recursividade. MDC de dois números é o maior número 
    que os divide. Uma maneira simples de encontrar o MDC é fatorar
     os dois números e multiplicar os fatores primos comuns.

    Complexidade: O(log N)

    Parameters
    ----------
    a: numero 1 inteiro
    b: numero 2 inteiro
    """
 
    # Caso base
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = mdc(b % a, a)
 
    # Atualizando x e y usando os resultados da recursao
    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y

if __name__ == "__main__":
    a, b = 9, 3
    g, x, y = mdc(a, b)
    print("gcd(", a, ",", b, ") = ", g)