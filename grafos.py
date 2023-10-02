import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for i in range(n)] for i in range(n)]
        self.list = [[] for i in range(n)]

    def print(self):
        print("Matriz_adj:\n",self.matrix)
        print("Lista_adj:\n", self.list)
        print("\n")
        
    def bfs(self, inicio):
        fila = queue.Queue()
        dist = [-1 for i in range(self.num_vertices)]
        ant = [-1 for i in range(self.num_vertices)]
        isVisited = [False for i in range(self.num_vertices)]

        fila.put(inicio)
        isVisited[inicio] = True
        dist[inicio] = 0

        while fila.empty() != True:
            p = fila.get()
            print("Vertice: " + str(p))

            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    fila.put(v)
                    isVisited[v] = True

        return dist, ant
    
    def path_bfs(self, s, t, ant):
        path = []

        if ant[t] == -1:
            return f"Não há caminho entre {s} e {t}"
        
        while t != s:
            path.append(t)
            t = ant[t]
        path.append(s)
        path.reverse()

        return " -> ".join(map(str,path))
        
    def dfs(self, inicio):
        isVisited = [False for i in range(self.num_vertices)]
        resultado = []
        pilha = []

        pilha.append(inicio)
        isVisited[inicio] = True

        while pilha:
            vertice = pilha.pop()
            resultado.append(vertice)

            for vizinho in self.list[vertice]:
                if not isVisited[vizinho]:
                    pilha.append(vizinho)
                    isVisited[vizinho] = True
        
        return resultado