import requests
import re
import os
import argparse
from typing import Optional


def download_gutenberg_book(book_id: int, output_file: Optional[str] = None) -> str:
    """
    Baixa um livro do Projeto Gutenberg pelo ID.
    
    Args:
        book_id: ID do livro no Projeto Gutenberg
        output_file: Nome do arquivo de saída (opcional)
        
    Returns:
        Caminho do arquivo baixado
    """
    # URL para download de texto simples
    url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    alt_url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    
    # Tenta primeiro a URL principal
    response = requests.get(url)
    
    # Se falhar, tenta a URL alternativa
    if response.status_code != 200:
        response = requests.get(alt_url)
        
    if response.status_code != 200:
        raise Exception(f"Não foi possível baixar o livro com ID {book_id}. Verifique se o ID está correto.")
    
    # Define o nome do arquivo de saída
    if not output_file:
        # Tenta extrair o título do conteúdo
        title_match = re.search(r"Title: (.+?)[\r\n]", response.text)
        if title_match:
            title = title_match.group(1).strip()
            # Limpa o título para um nome de arquivo válido
            title = re.sub(r'[^\w\s-]', '', title)
            title = re.sub(r'[-\s]+', '_', title).lower()
            output_file = f"{title}.txt"
        else:
            output_file = f"gutenberg_{book_id}.txt"
    
    # Salva o conteúdo no arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(response.text)
    
    print(f"Livro baixado com sucesso: {output_file}")
    return output_file


def main():
    parser = argparse.ArgumentParser(description='Baixar um livro do Projeto Gutenberg')
    parser.add_argument('book_id', type=int, help='ID do livro no Projeto Gutenberg')
    parser.add_argument('--output', '-o', help='Nome do arquivo de saída')
    
    args = parser.parse_args()
    
    try:
        output_file = download_gutenberg_book(args.book_id, args.output)
        print(f"\nPara buscar no livro, use:")
        print(f"python main.py {output_file} \"termo de busca\"")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main() 