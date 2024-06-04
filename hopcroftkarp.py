def ler_grafo_de_arquivo(nome_arquivo):
    grafo = {}
    with open(nome_arquivo, 'r') as file:
        for linha in file:
            u, v = map(int, linha.strip().split())
            if u not in grafo:
                grafo[u] = []
            grafo[u].append(v)
    return grafo

def bfs(grafo, pair_U, pair_V, dist):
    queue = []
    for u in grafo:
        if pair_U[u] == 0:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    dist[0] = float('inf')
    
    for u in queue:
        if dist[u] < dist[0]:
            for v in grafo[u]:
                if dist[pair_V[v]] == float('inf'):
                    dist[pair_V[v]] = dist[u] + 1
                    queue.append(pair_V[v])
    return dist[0] != float('inf')

def dfs(grafo, u, pair_U, pair_V, dist):
    if u != 0:
        for v in grafo[u]:
            if dist[pair_V[v]] == dist[u] + 1:
                if dfs(grafo, pair_V[v], pair_U, pair_V, dist):
                    pair_V[v] = u
                    pair_U[u] = v
                    return True
        dist[u] = float('inf')
        return False
    return True

def hopcroft_karp(grafo):
    pair_U = {u: 0 for u in grafo}
    pair_V = {v: 0 for u in grafo for v in grafo[u]}
    dist = {}
    
    matching = 0
    while bfs(grafo, pair_U, pair_V, dist):
        for u in grafo:
            if pair_U[u] == 0:
                if dfs(grafo, u, pair_U, pair_V, dist):
                    matching += 1
    return pair_U, pair_V

nome_arquivo = 'grafo_bipartido.txt'
grafo = ler_grafo_de_arquivo(nome_arquivo)

pair_U, pair_V = hopcroft_karp(grafo)


with open('emparelhamentos.txt', 'w') as file:
    file.write("Emparelhamento máximo: \n")
    cont = 0
    for u in pair_U:
        cont+=1
        if pair_U[u] != 0:
            file.write(f"{u} - {pair_U[u]}\n")

    file.write(f"Emparelhamentos máximos encontrados: {cont}" )
