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

# Exemplo de uso
tamanho_cache = 5
pos_memoria = [0,1,2,3,1,4,5,6]
mapeamento_direto(tamanho_cache, pos_memoria)
