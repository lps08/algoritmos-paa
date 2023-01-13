V = 4

def printConfiguration(colorArray):
    """Função para imprimir a configuração de cores.
    """
    print("As cores atribuídas são as seguintes:")
    for i in range(4):
        print("Vertice: ", i, " Cor: ", colorArray[i])

def isSafe(v, colorArray, vertex):
    """Uma função que irá verificar se o colorArray atual do gráfico é seguro ou não.
    """
    for i in range(V):
        if graph[v][i] == 1 and colorArray[i] == vertex:
            return False
        return True

def graphColoringAlgorithmUtil(m, colorArray, currentVertex):
    """Uma função recursiva que usa o índice atual, o número de vértices 
    e a matriz de cores. Se a chamada recursiva retornar true, a coloração 
    será possível. Ele retorna false se as m cores não puderem ser atribuídas.
    """
    # caso base
    if currentVertex == V:
        return True

    for i in range(1, m + 1):
        if isSafe(currentVertex, colorArray, i) == True:
            colorArray[currentVertex] = i
            if graphColoringAlgorithmUtil(m, colorArray, currentVertex + 1):
                return True

            # backtrack
            colorArray[currentVertex] = 0

def graphColoringAlgorithm(colorArray, m):
    """Funcao que ira realizar a coloracao do grafo utilizando backtracking

    Complexidade: O(m^V)
    """
    # Inicialmente, a matriz de cores é inicializada com 0.
    colorArray = [0] * V

    # Chama graphColoringAlgorithmUtil() para o vértice 0.
    if graphColoringAlgorithmUtil(m, colorArray, 0) == None:
        print("Nao é possivel colorir!")
        return False

    print("E possivel colorir!")
    printConfiguration(colorArray)
    return True

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3

    graphColoringAlgorithm(graph, m)