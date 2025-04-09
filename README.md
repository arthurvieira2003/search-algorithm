# Algoritmos de Busca de Texto

**Projeto desenvolvido por:**

- Arthur Henrique Tscha Vieira
- Rafael Rodrigues Ferreira de Andrade

## Sobre o Projeto

Este projeto implementa e compara dois algoritmos de busca de texto:

- **Busca Ingênua (Naive Search)**: uma implementação de força bruta que verifica cada posição possível no texto.
- **Algoritmo Rabin-Karp**: um algoritmo de busca de padrões mais eficiente que utiliza hashing para acelerar o processo de busca.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas: requests (para download de livros) e matplotlib (opcional, para gráficos de desempenho)

## Instalação

1. Clone o repositório ou baixe os arquivos
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

### 1. Baixar um Livro

Use o script `download_book.py` para baixar um livro do Projeto Gutenberg:

```bash
python download_book.py <ID_DO_LIVRO> --output <NOME_DO_ARQUIVO_DE_SAIDA>
```

Exemplos:

```bash
# Baixar Romeo and Juliet
python download_book.py 1513 --output romeo_and_juliet.txt

# Baixar Hamlet
python download_book.py 1524 --output hamlet.txt

# Baixar Frankenstein
python download_book.py 84 --output frankenstein.txt
```

Alternativamente, baixe manualmente um arquivo .txt da internet, como do [Projeto Gutenberg](https://www.gutenberg.org/)

### 2. Realizar uma Busca

Use o script `main.py` para buscar um padrão no texto e comparar os algoritmos:

```bash
python main.py <ARQUIVO_DE_TEXTO> "<PADRAO_A_BUSCAR>"
```

Exemplos:

```bash
# Buscar "love" em Romeo and Juliet
python main.py romeo_and_juliet.txt "love"

# Buscar "To be, or not to be" em Hamlet
python main.py hamlet.txt "To be, or not to be"

# Buscar "monster" em Frankenstein
python main.py frankenstein.txt "monster"

# Buscar "Capitu" em Dom Casmurro
python main.py dom_casmurro.txt "Capitu"
```

### 3. Executar Testes de Desempenho

Para executar testes de desempenho mais abrangentes, use o script `performance_test.py`:

```bash
python performance_test.py
```

Isso gerará gráficos comparando o desempenho dos algoritmos com diferentes tamanhos de texto e padrões.

## Arquivos do Projeto

- `search_algorithms.py`: Implementações dos algoritmos de busca (Rabin-Karp e Busca Ingênua)
- `main.py`: Script principal para realizar buscas em arquivos de texto
- `download_book.py`: Script para baixar livros do Projeto Gutenberg
- `performance_test.py`: Script para testar e comparar o desempenho dos algoritmos

## IDs de Livros Populares no Projeto Gutenberg

- **1513**: Romeo and Juliet (Shakespeare)
- **1524**: Hamlet (Shakespeare)
- **84**: Frankenstein (Mary Shelley)
- **1342**: Pride and Prejudice (Jane Austen)
- **55752**: The Art of South American Cookery
- **19002**: Machado de Assis - Várias Histórias (Português)
- **10**: A Bíblia

## Dicas

- Para padrões que contêm espaços ou caracteres especiais, use aspas: `"to be or not to be"`
- Para textos muito grandes, o tempo de execução pode ser significativo
- Experimente buscar padrões de diferentes tamanhos para observar o comportamento dos algoritmos

---

# Resultados da Análise

## Testes Realizados

Foram realizados testes com diferentes livros e padrões:

1. **Romeo and Juliet** (Shakespeare)

   - Busca pelo termo "love": 162 ocorrências encontradas
   - Busca Ingênua: 0.037942 segundos
   - Rabin-Karp: 0.041209 segundos (0.92x mais lento)

2. **Hamlet** (Shakespeare)

   - Busca pelo termo "To be, or not to be": 1 ocorrência encontrada
   - Busca Ingênua: 0.056955 segundos
   - Rabin-Karp: 0.069821 segundos (0.82x mais lento)

3. **Trecho de Dom Casmurro** (Machado de Assis)

   - Busca pelo termo "Capitu": 8 ocorrências encontradas
   - Busca Ingênua: 0.000528 segundos
   - Rabin-Karp: 0.001625 segundos (0.33x mais lento)

4. **Frankenstein** (Mary Shelley)
   - Busca pelo termo "monster": 33 ocorrências encontradas
   - Busca Ingênua: 0.115915 segundos
   - Rabin-Karp: 0.129119 segundos (0.90x mais lento)
   - Busca pela frase "It was on a dreary night of November": 1 ocorrência encontrada
   - Busca Ingênua: 0.120199 segundos
   - Rabin-Karp: 0.135095 segundos (0.89x mais lento)

## Testes de Desempenho

Foram realizados testes sistemáticos variando o tamanho do texto e o tamanho do padrão:

1. **Variação do tamanho do texto** (com padrão fixo)

   - Para textos maiores, ambos os algoritmos tendem a ter tempo de execução linear, mas o Rabin-Karp mostrou-se ligeiramente mais lento nos testes realizados.

2. **Variação do tamanho do padrão** (com texto fixo)
   - Para padrões curtos, a Busca Ingênua foi geralmente mais rápida
   - Para padrões longos, o Rabin-Karp mostrou desempenho competitivo

## Respostas às Perguntas de Reflexão

1. **Os dois algoritmos retornaram os mesmos resultados?**

   - Sim, em todos os testes realizados, ambos os algoritmos encontraram exatamente as mesmas ocorrências. Isso era esperado, pois ambos os algoritmos são determinísticos e realizam uma busca exata.

2. **Qual algoritmo foi mais rápido?**

   - Nos testes realizados, a Busca Ingênua foi geralmente mais rápida, o que pode ser surpreendente. No entanto, isso pode ser explicado pelo fato de que:
     - A implementação da Busca Ingênua é muito simples e eficiente em Python
     - O Rabin-Karp tem um overhead inicial para calcular os hashes
     - Para textos de tamanho moderado, como os livros testados, o overhead do Rabin-Karp não é compensado por sua eficiência teórica
     - Python tem otimizações internas para operações de string que beneficiam a Busca Ingênua

3. **O tamanho do texto ou do trecho buscado influencia no tempo de execução?**

   - **Tamanho do texto**: Ambos os algoritmos têm complexidade O(n) para o tamanho do texto, ou seja, o tempo aumenta linearmente com o tamanho do texto.
   - **Tamanho do padrão**: Para a Busca Ingênua, o tempo tende a aumentar com o tamanho do padrão. Para o Rabin-Karp, o tamanho do padrão afeta menos o desempenho final, pois após o cálculo inicial do hash, as comparações são mais eficientes.

4. **Em que situações um algoritmo pode ser preferido ao outro?**

   - **Busca Ingênua é preferível quando**:

     - O texto é pequeno ou moderado
     - O padrão é curto
     - Simplicidade de implementação é uma prioridade
     - Não há padrões patológicos que possam causar muitas verificações

   - **Rabin-Karp é preferível quando**:
     - O texto é muito grande
     - Múltiplos padrões precisam ser buscados simultaneamente
     - O padrão é muito longo
     - Há preocupação com padrões que causariam muitas verificações na Busca Ingênua

## Conclusão

Os resultados dos testes mostram que, para aplicações típicas de busca em arquivos de texto como livros, a Busca Ingênua pode ser surpreendentemente eficiente. No entanto, o algoritmo Rabin-Karp oferece vantagens teóricas que podem ser importantes em cenários mais complexos ou com textos extremamente grandes.

A escolha entre os algoritmos deve levar em consideração não apenas o desempenho, mas também a natureza específica do problema, como o tamanho dos textos, a frequência das buscas e os tipos de padrões que serão buscados.

Vale ressaltar que outras implementações ou linguagens de programação podem apresentar resultados diferentes, e que existem algoritmos ainda mais eficientes para busca de padrões, como o algoritmo Knuth-Morris-Pratt e o algoritmo Boyer-Moore.
