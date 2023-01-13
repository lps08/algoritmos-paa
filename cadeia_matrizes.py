import sys
 
# Função # para encontrar a maneira mais eficiente de multiplicar
# uma determinada sequência de matrizes
def matrixChainMultiplication(dims, i, j, lookup):
    """Função para encontrar a maneira mais eficiente de multiplicar
    uma determinada sequência de matrizes utilizando a técnica de 
    programacao dinamica

    Complexidade: O(n^3)

    Parameters
    ----------
    dimns: dimensao das matrizes para ser calculado o custo
    i: posicao inicial
    j: posicao final
    lookup: tabela para armazenar os resultados da operacoes
    """

    # Caso base: uma matriz
    if j <= i + 1:
        return 0
 
    # armazena o número mínimo de multiplicações escalares (ou seja, custo)
    # necessário para calcular a matriz `M[i+1] … M[j] = M[i…j]`
    min = sys.maxsize
 
    # se o subproblema for visto pela primeira vez, resolva-o e
    # armazena seu resultado em uma tabela de pesquisa
    if lookup[i][j] == 0:
 
        # assume o mínimo em cada posição possível em que o
        # A sequência de matrizes # pode ser dividida
 
        '''
            (M[i+1]) × (M[i+2]………………M[j])
            (M[i+1]M[i+2]) × (M[i+3…………M[j])
            …
            …
            (M[i+1]M[i+2]…………M[j-1]) × (M[j])
        '''
 
        for k in range(i + 1, j):
 
            # recorrente para `M[i+1]…M[k]` para obter uma matriz `i × k`
            cost = matrixChainMultiplication(dims, i, k, lookup)
 
            # recorrente para `M[k+1]…M[j]` para obter uma matriz `k × j`
            cost += matrixChainMultiplication(dims, k, j, lookup)
 
            # custo para multiplicar duas matrizes `i × k` e `k × j`
            cost += dims[i] * dims[k] * dims[j]
 
            if cost < min:
                min = cost
 
        lookup[i][j] = min
 
    # retorna o custo mínimo para multiplicar `M[j+1]…M[j]`
    return lookup[i][j]
 
if __name__ == '__main__':
 
    # Matrix `M[i]` tem dimensão `dims[i-1] × dims[i]` para `i=1…n`
    # A entrada # é matriz 10 × 30, matriz 30 × 5, matriz 5 × 60
    dims = [10, 30, 5, 60]
 
    # Tabela de pesquisa # para armazenar a solução para subproblemas já computados
    lookup = [[0 for x in range(len(dims))] for y in range(len(dims))]
 
    n = len(dims)
    print('The minimum cost is', matrixChainMultiplication(dims, 0, n - 1, lookup))