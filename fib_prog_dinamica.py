def fibonacciTopDown(n, table = {1:1, 0:0}):
    """Algoritmo de fibonacci utilizando a técnica de programacao dinamica com
    TopDown(iniciando do maior valor para o caso base).Nela, para cada operação 
    feita, salva o resultado em uma tabela e antes de realizar um cálculo, verifica 
    na tabela se essa operação já foi realizada.
    
    abordagem padrão: O(2^n) ou exponential
    programação dinamica: θ(n)

    Parameters
    ----------
    n: sequencia para ser calculado
    table: tabela que armazena as operações
    """
    # if n == 1 or n == 0:
    #     return n
    try:
        return table[n]
    except:
        table[n] = fibonacciTopDown(n-1) + fibonacciTopDown(n-2)
        return table[n]

if __name__ == "__main__":
    t = fibonacciTopDown(5)
    print(f"Fib {t}")