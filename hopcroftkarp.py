def ler_grafo_de_arquivo(nome_arquivo):
    """
    Lê um grafo bipartido de um arquivo.
    
    Args:
        nome_arquivo (str): Nome do arquivo contendo o grafo bipartido.

    Returns:
        grafo (dict): Dicionário com os vértices e suas respectivas arestas.
    """
    grafo = {}
    with open(nome_arquivo, 'r') as file:
        for linha in file:
            u, v = map(int, linha.strip().split())
            if u not in grafo:
                grafo[u] = []
            grafo[u].append(v)
    return grafo

def bfs(grafo, pair_U, pair_V, dist):
    """
    Realiza uma busca em largura (BFS) no grafo bipartido.
    
    Args:
        grafo (dict): O grafo bipartido.
        pair_U (dict): Emparelhamento dos vértices em U.
        pair_V (dict): Emparelhamento dos vértices em V.
        dist (dict): Dicionário das distâncias.

    Returns:
        bool: True se existe um caminho aumentador, False caso contrário.
    """
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
    """
    Realiza uma busca em profundidade (DFS) no grafo bipartido.
    
    Args:
        grafo (dict): O grafo bipartido.
        u (int): O vértice atual.
        pair_U (dict): Emparelhamento dos vértices em U.
        pair_V (dict): Emparelhamento dos vértices em V.
        dist (dict): Dicionário das distâncias.

    Returns:
        bool: True se encontrou um caminho aumentador, False caso contrário.
    """
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
    """
    Encontra o emparelhamento máximo em um grafo bipartido usando o algoritmo de Hopcroft-Karp.
    
    Args:
        grafo (dict): O grafo bipartido.

    Returns:
        pair_U (dict), pair_V (dict): O emparelhamento máximo dos vértices em U e V.
    """
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

# Exemplo de uso
nome_arquivo = 'grafo_bipartido.txt'
grafo = ler_grafo_de_arquivo(nome_arquivo)

pair_U, pair_V = hopcroft_karp(grafo)


# Abra um arquivo para salvar os emparelhamentos
with open('emparelhamentos.txt', 'w') as file:
    file.write("Emparelhamento máximo: \n")
    cont = 0
    # Percorra os emparelhamentos
    for u in pair_U:
        cont+=1
        if pair_U[u] != 0:
            # Escreva o emparelhamento no arquivo
            file.write(f"{u} - {pair_U[u]}\n")

    # Escreva o número de emparelhamentos no arquivo
    file.write(f"Emparelhamentos máximos encontrados: {cont}" )
