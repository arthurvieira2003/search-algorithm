import time
import random
import string
import matplotlib.pyplot as plt
from search_algorithms import naive_search, rabin_karp_search

def generate_random_text(length):
    """Gera um texto aleatório de tamanho especificado."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def test_performance_by_text_size(pattern_length=5, max_text_length=100000, step=10000):
    """Testa o desempenho dos algoritmos com diferentes tamanhos de texto."""
    text_lengths = list(range(step, max_text_length + step, step))
    naive_times = []
    rabin_karp_times = []
    
    # Gera um padrão fixo
    pattern = generate_random_text(pattern_length)
    
    for length in text_lengths:
        # Gera texto aleatório
        text = generate_random_text(length)
        
        # Inclui o padrão em uma posição aleatória
        pos = random.randint(0, length - pattern_length)
        text = text[:pos] + pattern + text[pos+pattern_length:]
        
        # Mede o tempo para Busca Ingênua
        start_time = time.time()
        naive_search(text, pattern)
        naive_time = time.time() - start_time
        naive_times.append(naive_time)
        
        # Mede o tempo para Rabin-Karp
        start_time = time.time()
        rabin_karp_search(text, pattern)
        rabin_karp_time = time.time() - start_time
        rabin_karp_times.append(rabin_karp_time)
        
        print(f"Texto de {length} caracteres: Naive={naive_time:.6f}s, Rabin-Karp={rabin_karp_time:.6f}s")
    
    # Plota os resultados
    plt.figure(figsize=(10, 6))
    plt.plot(text_lengths, naive_times, 'b-', label='Busca Ingênua')
    plt.plot(text_lengths, rabin_karp_times, 'r-', label='Rabin-Karp')
    plt.xlabel('Tamanho do Texto')
    plt.ylabel('Tempo (segundos)')
    plt.title(f'Desempenho por Tamanho do Texto (Padrão: {pattern_length} caracteres)')
    plt.legend()
    plt.grid(True)
    plt.savefig('performance_by_text_size.png')
    
    return text_lengths, naive_times, rabin_karp_times

def test_performance_by_pattern_size(text_length=100000, max_pattern_length=100, step=10):
    """Testa o desempenho dos algoritmos com diferentes tamanhos de padrão."""
    pattern_lengths = list(range(1, max_pattern_length + step, step))
    naive_times = []
    rabin_karp_times = []
    
    # Gera um texto aleatório fixo
    text = generate_random_text(text_length)
    
    for length in pattern_lengths:
        # Gera um padrão e garante que ele está no texto
        pattern = generate_random_text(length)
        pos = random.randint(0, text_length - length)
        text = text[:pos] + pattern + text[pos+length:]
        
        # Mede o tempo para Busca Ingênua
        start_time = time.time()
        naive_search(text, pattern)
        naive_time = time.time() - start_time
        naive_times.append(naive_time)
        
        # Mede o tempo para Rabin-Karp
        start_time = time.time()
        rabin_karp_search(text, pattern)
        rabin_karp_time = time.time() - start_time
        rabin_karp_times.append(rabin_karp_time)
        
        print(f"Padrão de {length} caracteres: Naive={naive_time:.6f}s, Rabin-Karp={rabin_karp_time:.6f}s")
    
    # Plota os resultados
    plt.figure(figsize=(10, 6))
    plt.plot(pattern_lengths, naive_times, 'b-', label='Busca Ingênua')
    plt.plot(pattern_lengths, rabin_karp_times, 'r-', label='Rabin-Karp')
    plt.xlabel('Tamanho do Padrão')
    plt.ylabel('Tempo (segundos)')
    plt.title(f'Desempenho por Tamanho do Padrão (Texto: {text_length} caracteres)')
    plt.legend()
    plt.grid(True)
    plt.savefig('performance_by_pattern_size.png')
    
    return pattern_lengths, naive_times, rabin_karp_times

def run_comprehensive_test():
    """Executa uma série de testes abrangentes e gera gráficos."""
    print("Testando o desempenho por tamanho do texto...")
    test_performance_by_text_size(pattern_length=5, max_text_length=80000, step=10000)
    
    print("\nTestando o desempenho por tamanho do padrão...")
    test_performance_by_pattern_size(text_length=50000, max_pattern_length=50, step=5)
    
    print("\nTestando o desempenho com padrões longos...")
    test_performance_by_pattern_size(text_length=50000, max_pattern_length=1000, step=100)

if __name__ == "__main__":
    try:
        import matplotlib
        run_comprehensive_test()
    except ImportError:
        print("A biblioteca matplotlib não está instalada. Instalando...")
        import subprocess
        subprocess.call(['pip', 'install', 'matplotlib'])
        
        try:
            import matplotlib
            run_comprehensive_test()
        except ImportError:
            print("Não foi possível instalar matplotlib. Pulando a geração de gráficos.")
            # Executar versão simplificada sem gráficos
            print("Testando o desempenho por tamanho do texto (sem gráficos)...")
            test_performance_by_text_size(pattern_length=5, max_text_length=50000, step=10000)
            
            print("\nTestando o desempenho por tamanho do padrão (sem gráficos)...")
            test_performance_by_pattern_size(text_length=50000, max_pattern_length=50, step=5) 