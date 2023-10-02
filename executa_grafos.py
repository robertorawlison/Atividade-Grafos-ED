from grafos import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == g.num_vertices):
                break
            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)
            
            c += 1
        l += 1
    return g

cond = True

while(cond):
    caminho_arquivo = input("Digite o caminho do arquivo: ")
    grafo = load_from(caminho_arquivo)
    grafo.print()
    vertice_ini = int(input("Digite o vertice inicial: "))
    vertice_final = int(input("Digite o vertice final, para encontrar o caminho: "))

    dist, ant = grafo.bfs(vertice_ini)
    retorno = grafo.dfs(vertice_ini)
    path = grafo.path_bfs(vertice_ini, vertice_final, ant)

    print("Dist_bfs: ", dist)
    print("Ant_bfs: ", ant)
    print("DFS: ", retorno)
    print("Path: ", path)

    a = input("continuar? (s/n) ")
    if a == "s":
        cond = True
    else:
        cond = False 