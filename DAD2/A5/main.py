# Language: Python 3
#
# Aplicação de Lista Invertida, lê o arquivo texto.txt e cria um arquivo para cada palavras, contendo o índice de cada ocorrência da palavra no texto.txt
# Quando o arquivo já existe, apenas adiciona o índice no final do arquivo, assim possibilitando a contagem de linhas para saber quantas vezes a palavra é repetida
#
# Tentei fazer em um arquivo .db, mas não sei como abrir o arquivo corretamente para validar as informações, então optei por fazer em arquivos de texto
#

import os
import re

# Cria o diretório para armazenar os arquivos de texto
if not os.path.exists('./DAD2/A5/textos'):
    os.makedirs('./DAD2/A5/textos')

# Lê o arquivo de texto e extrai as palavras, ignorando as primeiras 5 linhas
with open('./DAD2/A5/texto.txt', 'r', encoding='utf-8') as f:
    for _ in range(5):
        next(f)  # Pula as primeiras 5 linhas do arquivo, cujo tem o cabeçalho, se for removido, favor remover essa linha e o for acima
    texto = f.read()
palavras = re.findall(r'\w+', texto)

# Processa as palavras
for indice, palavra in enumerate(palavras):
    # Cria o arquivo de texto para a palavra, se ainda não existir
    arquivo_palavra = f"./DAD2/A5/textos/{palavra}.txt"
    if not os.path.exists(arquivo_palavra):
        with open(arquivo_palavra, 'w') as f:
            f.write(f"{indice}\n")
    else:
        with open(arquivo_palavra, 'a') as f:
            f.write(f"{indice}\n")

# Contar as linhas de cada arquivo de palavra
for arquivo in os.listdir('./DAD2/A5/textos'):
    if arquivo.endswith('.txt'):
        nome_arquivo = os.path.splitext(arquivo)[0]  # Remove a extensão .txt
        with open(os.path.join('./DAD2/A5/textos', arquivo), 'r', encoding='utf-8') as f:
            num_linhas = sum(1 for linha in f)
            print(f"Palavra: {nome_arquivo}, Repetições: {num_linhas}")