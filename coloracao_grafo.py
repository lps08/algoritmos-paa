class Graph():
    """Classe onde implementa a coloracaoo de vertices de um grafo utilizando backtracking, 
    onde cada vizinho de um grafo deve ser colorido com cores distintas. 

    Complexidade: O(m^V)
    """
  
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph
  
    def isSafe(self, v, colour, c):
        """Função que irá verificar se o colorArray atual do gráfico é seguro ou não.

        Parameters
        ----------
        v: vertice atual para ser analisado se pode colorir
        colour: array de cores
        c: cor para testar se é possivel colorir o certice v
        """
        for i in range(self.V):
            # verifica se os vizinhos do vertice v possui a mesma cor que os vértices vizinhos
            # caso nao possua, significa que a cor i pode ser atribuida ao vertice v
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
  
    def graphColourUtil(self, m, colour, v):
        """Uma função recursiva que usa o índice atual, o número de vértices 
        e a matriz de cores. Se a chamada recursiva retornar true, a coloração 
        será possível. Ele retorna false se as m cores não puderem ser atribuídas.

        Parameters
        ----------
        m: numero de cores (numero inteiro)
        colour: array de cores
        v: vertice atual para ser analisado
        """
        # caso base
        if v == self.V:
            return True
  
        for c in range(1, m + 1):
            # verifica se é possivel colorir o vertice atual com a cor c
            if self.isSafe(v, colour, c):
                # se foi possivel, atribui a cor ao vertice analisado
                colour[v] = c
                # analisa recursivamente os proximos vertices para tentar colorir 
                if self.graphColourUtil(m, colour, v + 1):
                    return True
                    
                #reseta a cor atual pois deu conflito com o vertice v+1
                #testando agora a cor c+1
                colour[v] = 0
  
    def graphColouring(self, m):
        """Funcao que ira realizar a coloracao do grafo utilizando os métodos
        apresentados acima.

        Complexidade: O(m^V)
        """
        # Inicialmente, a matriz de cores é inicializada com 0.
        colour = [0] * self.V

        # Chama graphColoringAlgorithmUtil() para o vértice 0.
        # iniciando a coloracao do grafo a partir da primeira posicao
        # ira rodar a funcao recursivamente até que seja possivel colorir o grafo ou não
        if self.graphColourUtil(m, colour, 0) == None:
            print("Nao é possivel colorir!")
            return False

        print("E possivel colorir!")
        print("As cores atribuídas são as seguintes:")
        for c in range(self.V):
            print("Vertice: ", c, " Cor: ", colour[c])
        return True
  
  
if __name__ == '__main__':
    graph =[[0, 1, 1, 1],
            [1, 0, 1, 0], 
            [1, 1, 0, 1], 
            [1, 0, 1, 0]]

    g = Graph(4, graph)
    m = 3
  
    g.graphColouring(m)