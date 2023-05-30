def inicializar_cache(tamanho_cache):
    cache = {}
    for i in range(tamanho_cache):
        cache[i] = -1
    return cache

def imprimir_cache(cache):
    print("Tamanho da cache:", len(cache))
    print("\nPosição cache\tPosição Memória")
    for chave, valor in cache.items():
        print(f"{chave}\t\t{valor}")

def mapeamento_direto(tamanho_cache, pos_memoria):
    cache = inicializar_cache(tamanho_cache)
    imprimir_cache(cache)
    
    hits = 0
    misses = 0
    
    for pos in pos_memoria:
        posicao_cache = pos % tamanho_cache
        
        if cache[posicao_cache] == pos:
            hits += 1
            print(f"\nHit! Endereço {pos} encontrado na cache.")
        else:
            misses += 1
            print(f"\nMiss! Endereço {pos} não encontrado na cache.")
            cache[posicao_cache] = pos
        
        imprimir_cache(cache)
    
    total_acessos = len(pos_memoria)
    taxa_cache_hit = hits / total_acessos * 100

    print("\nResumo:")
    print(f"Total de posições de memórias acessadas: {total_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Taxa de cache hit: {taxa_cache_hit}%")

def inicializar_cache_associativa(tamanho_cache, tamanho_conjunto):
    cache = [[] for _ in range(tamanho_cache)]
    for conjunto in cache:
        for _ in range(tamanho_conjunto):
            conjunto.append([-1, 0])  # [endereço, contador]
    return cache

def imprimir_cache_associativa(cache):
    print("Tamanho da cache:", len(cache))
    print("\nConjunto\tPosição Cache\tPosição Memória")
    for i, conjunto in enumerate(cache):
        for j, (endereco, _) in enumerate(conjunto):
            print(f"{i}\t\t{j}\t\t{endereco}")

def substituir_LRU(conjunto):
    min_contador = float("inf")
    posicao_substituir = -1
    for i, (endereco, contador) in enumerate(conjunto):
        if contador < min_contador:
            min_contador = contador
            posicao_substituir = i
    return posicao_substituir

def substituir_LFU(conjunto):
    min_contador = float("inf")
    posicao_substituir = -1
    for i, (endereco, contador) in enumerate(conjunto):
        if contador < min_contador:
            min_contador = contador
            posicao_substituir = i
        elif contador == min_contador and endereco < conjunto[posicao_substituir][0]:
            posicao_substituir = i
    return posicao_substituir

def substituir_FIFO(conjunto):
    posicao_substituir = 0
    return posicao_substituir

def substituir(endereco, conjunto, substituicao):
    if substituicao == "LRU":
        posicao_substituir = substituir_LRU(conjunto)
    elif substituicao == "LFU":
        posicao_substituir = substituir_LFU(conjunto)
    elif substituicao == "FIFO":
        posicao_substituir = substituir_FIFO(conjunto)

    conjunto[posicao_substituir] = [endereco, conjunto[posicao_substituir][1] + 1]

def mapeamento_associativo_conjunto(tamanho_conjunto, pos_memoria, substituicao):
    tamanho_cache = len(pos_memoria) // tamanho_conjunto
    cache = inicializar_cache_associativa(tamanho_cache, tamanho_conjunto)

    hits = 0
    misses = 0
    contador = 0

    for pos in pos_memoria:
        conjunto_atual = pos % tamanho_cache
        conjunto = cache[conjunto_atual]

        if [pos, contador] in conjunto:
            hits += 1
            print(f"\nHit! Endereço {pos} encontrado na cache.")
        else:
            misses += 1
            print(f"\nMiss! Endereço {pos} não encontrado na cache.")
            if len(conjunto) < tamanho_conjunto:
                conjunto.append([pos, contador])
            else:
                substituir(pos, conjunto, substituicao)

        imprimir_cache_associativa(cache)

        contador += 1

    total_acessos = len(pos_memoria)
    taxa_cache_hit = hits / total_acessos * 100

    print("\nResumo:")
    print(f"Total de posições de memórias acessadas: {total_acessos}")
    print(f"Total de hits: {hits}")
    print(f"Total de misses: {misses}")
    print(f"Taxa de cache hit: {taxa_cache_hit}%")

# Exemplo de uso
tamanho_cache = 4
pos_memoria = [1, 2, 3, 1, 4, 2, 5, 3]
mapeamento_direto(tamanho_cache, pos_memoria)

tamanho_conjunto = 2
substituicao = "FIFO"
mapeamento_associativo_conjunto(tamanho_conjunto, pos_memoria, substituicao)

