import random

def gerar_grafo_bipartido(particao1, particao2, densidade):
    grafo = []

    for u in range(1, particao1 + 1):
        for v in range(particao1 + 1, particao1 + particao2 + 1):
            # Se o número aleatório gerado for menor ou igual à densidade, adiciona a aresta
            if random.random() <= densidade:
                grafo.append((u, v))
    
    return grafo

def salvar_grafo_em_arquivo(grafo, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        for aresta in grafo:
            file.write(f'{aresta[0]} {aresta[1]}\n')

def desenhar_grafo_bipartido(particao1, particao2, grafo):
    nodes_U = [f'U{i}' for i in range(particao1)]
    nodes_V = [f'V{i}' for i in range(particao2)]


particao1 = int(input("Digite o número de pacientes receptores: "))
particao2 = int(input("Digite o número de doadores de órgãos: "))
densidade = float(input("Digite a densidade do grafo (entre 0 e 1): "))

grafo = gerar_grafo_bipartido(particao1, particao2, densidade)

print("Arestas do grafo bipartido gerado:")
for aresta in grafo:
    print(aresta)

nome_arquivo = 'grafo_bipartido.txt'
salvar_grafo_em_arquivo(grafo, nome_arquivo)
print(f'O grafo foi salvo no arquivo: {nome_arquivo}')

desenhar_grafo_bipartido(particao1, particao2, grafo)
