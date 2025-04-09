import time
from typing import List, Tuple

def naive_search(text: str, pattern: str) -> Tuple[List[int], float]:
    """
    Implementação da busca ingênua (força bruta).
    
    Args:
        text: Texto onde buscar
        pattern: Padrão a ser encontrado
        
    Returns:
        Uma tupla com a lista de posições onde o padrão foi encontrado e o tempo de execução
    """
    start_time = time.time()
    positions = []
    
    # Para cada posição possível no texto
    for i in range(len(text) - len(pattern) + 1):
        match = True
        
        # Verifica se o padrão coincide começando na posição i
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
                
        if match:
            positions.append(i)
    
    execution_time = time.time() - start_time
    return positions, execution_time


def rabin_karp_search(text: str, pattern: str) -> Tuple[List[int], float]:
    """
    Implementação do algoritmo Rabin-Karp.
    
    Args:
        text: Texto onde buscar
        pattern: Padrão a ser encontrado
        
    Returns:
        Uma tupla com a lista de posições onde o padrão foi encontrado e o tempo de execução
    """
    start_time = time.time()
    positions = []
    
    if not pattern or not text or len(pattern) > len(text):
        execution_time = time.time() - start_time
        return positions, execution_time
    
    # Valores para o cálculo do hash
    d = 256  # Número de caracteres no alfabeto
    q = 101  # Um número primo
    
    m = len(pattern)
    n = len(text)
    
    # Cálculo de d^(m-1) % q
    h = 1
    for _ in range(m-1):
        h = (h * d) % q
    
    # Cálculo do hash inicial para o padrão e para a primeira janela do texto
    p_hash = 0  # hash do padrão
    t_hash = 0  # hash da primeira janela do texto
    
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    
    # Deslizar a janela pelo texto
    for i in range(n - m + 1):
        # Verificar se os hashes coincidem
        if p_hash == t_hash:
            # Verificar se os caracteres realmente coincidem
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            
            if match:
                positions.append(i)
        
        # Calcular o hash para a próxima janela
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            
            # Garantir que t_hash seja não-negativo
            if t_hash < 0:
                t_hash += q
    
    execution_time = time.time() - start_time
    return positions, execution_time


def display_results(text: str, pattern: str, naive_results: Tuple[List[int], float], 
                   rabin_karp_results: Tuple[List[int], float]) -> None:
    """
    Exibe os resultados das buscas.
    
    Args:
        text: Texto onde a busca foi realizada
        pattern: Padrão buscado
        naive_results: Resultados da busca ingênua
        rabin_karp_results: Resultados da busca Rabin-Karp
    """
    naive_positions, naive_time = naive_results
    rk_positions, rk_time = rabin_karp_results
    
    print(f"Padrão buscado: '{pattern}'")
    print(f"Tamanho do texto: {len(text)} caracteres")
    print(f"Tamanho do padrão: {len(pattern)} caracteres")
    print("\nResultados da busca:")
    
    print(f"\nBusca Ingênua:")
    print(f"- Ocorrências encontradas: {len(naive_positions)}")
    print(f"- Tempo de execução: {naive_time:.6f} segundos")
    
    print(f"\nAlgoritmo Rabin-Karp:")
    print(f"- Ocorrências encontradas: {len(rk_positions)}")
    print(f"- Tempo de execução: {rk_time:.6f} segundos")
    
    # Verificar se os resultados são iguais
    results_match = sorted(naive_positions) == sorted(rk_positions)
    print(f"\nOs resultados são idênticos? {'Sim' if results_match else 'Não'}")
    
    # Calcular a diferença de velocidade
    if naive_time > 0:
        speedup = naive_time / rk_time if rk_time > 0 else float('inf')
        print(f"Rabin-Karp foi {speedup:.2f}x {'mais rápido' if speedup > 1 else 'mais lento'} que a Busca Ingênua") 