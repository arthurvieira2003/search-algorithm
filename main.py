import os
import argparse
from search_algorithms import naive_search, rabin_karp_search, display_results

def read_text_file(filepath: str) -> str:
    """
    Lê um arquivo de texto.
    
    Args:
        filepath: Caminho para o arquivo
        
    Returns:
        Conteúdo do arquivo como string
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Tente com outra codificação se utf-8 falhar
        with open(filepath, 'r', encoding='latin-1') as file:
            return file.read()


def main():
    parser = argparse.ArgumentParser(description='Comparar algoritmos de busca de texto')
    parser.add_argument('file', help='Arquivo de texto para realizar a busca')
    parser.add_argument('pattern', help='Padrão a ser buscado no texto')
    
    args = parser.parse_args()
    
    # Verificar se o arquivo existe
    if not os.path.exists(args.file):
        print(f"Erro: O arquivo '{args.file}' não foi encontrado.")
        return
    
    # Carregar o texto do arquivo
    text = read_text_file(args.file)
    pattern = args.pattern
    
    print(f"Arquivo carregado: {args.file}")
    print(f"Tamanho do arquivo: {len(text)} caracteres")
    
    # Executar os algoritmos de busca
    naive_results = naive_search(text, pattern)
    rabin_karp_results = rabin_karp_search(text, pattern)
    
    # Exibir os resultados
    display_results(text, pattern, naive_results, rabin_karp_results)
    
    # Mostrar contexto para algumas ocorrências encontradas
    naive_positions = naive_results[0]
    if naive_positions:
        print("\nExemplos de ocorrências encontradas:")
        # Mostrar até 3 exemplos
        for i, pos in enumerate(naive_positions[:3]):
            start = max(0, pos - 20)
            end = min(len(text), pos + len(pattern) + 20)
            context = text[start:end]
            
            # Substitua o padrão por uma versão destacada
            pattern_start = pos - start
            pattern_end = pattern_start + len(pattern)
            highlighted = context[:pattern_start] + "*" + context[pattern_start:pattern_end] + "*" + context[pattern_end:]
            
            print(f"\nOcorrência {i+1} (posição {pos}):")
            print(f"...{highlighted}...")


if __name__ == "__main__":
    main() 