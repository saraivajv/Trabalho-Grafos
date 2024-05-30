import random

def gerar_grafo_bipartido(particao1, particao2, densidade):
    """
    Gera um grafo bipartido.
    
    Args:
        particao1 (int): Número de vértices na primeira partição.
        particao2 (int): Número de vértices na segunda partição.
        densidade (float): Densidade do grafo, valor entre 0 e 1.

    Returns:
        grafo (list): Lista de arestas do grafo bipartido gerado.
    """
    grafo = []
    
    # Adicionar arestas de acordo com a densidade
    for u in range(1, particao1 + 1):
        for v in range(particao1 + 1, particao1 + particao2 + 1):
            # Se o número aleatório gerado for menor ou igual à densidade, adiciona a aresta
            if random.random() <= densidade:
                grafo.append((u, v))
    
    return grafo

# Resto do código permanece o mesmo...


def salvar_grafo_em_arquivo(grafo, nome_arquivo):
    """
    Salva o grafo bipartido em um arquivo.
    
    Args:
        grafo (list): Lista de arestas do grafo bipartido gerado.
        nome_arquivo (str): Nome do arquivo para salvar o grafo.
    """
    with open(nome_arquivo, 'w') as file:
        for aresta in grafo:
            file.write(f'{aresta[0]} {aresta[1]}\n')

def desenhar_grafo_bipartido(particao1, particao2, grafo):
    """
    Desenha o grafo bipartido em uma representação ASCII.
    
    Args:
        particao1 (int): Número de vértices na primeira partição.
        particao2 (int): Número de vértices na segunda partição.
        grafo (list): Lista de arestas do grafo bipartido gerado.
    """
    nodes_U = [f'U{i}' for i in range(particao1)]
    nodes_V = [f'V{i}' for i in range(particao2)]
    
    print("\nGrafo Bipartido (Representação ASCII):")
    for u in nodes_U:
        print(f'{u}: ', end='')
        edges = [f'{v}' for (u_idx, v_idx) in grafo if u_idx == nodes_U.index(u) for v in nodes_V if nodes_V.index(v) == (v_idx - particao1)]
        print(", ".join(edges))

# Receber inputs do usuário
particao1 = int(input("Digite o número de pacientes receptores: "))
particao2 = int(input("Digite o número de doadores de órgãos: "))
densidade = float(input("Digite a densidade do grafo (entre 0 e 1): "))

# Gerar o grafo bipartido
grafo = gerar_grafo_bipartido(particao1, particao2, densidade)

# Imprimir as arestas do grafo gerado
print("Arestas do grafo bipartido gerado:")
for aresta in grafo:
    print(aresta)

# Salvar o grafo em um arquivo
nome_arquivo = 'grafo_bipartido.txt'
salvar_grafo_em_arquivo(grafo, nome_arquivo)
print(f'O grafo foi salvo no arquivo: {nome_arquivo}')

# Desenhar o grafo gerado
desenhar_grafo_bipartido(particao1, particao2, grafo)
