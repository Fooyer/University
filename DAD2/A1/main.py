def copiar_conteudo_sem_comentarios(origem, destino):
    # Abrindo o arquivo de origem para leitura
    with open(origem, 'r') as arquivo_origem:
        # Abrindo o arquivo de destino para escrita
        with open(destino, 'w') as arquivo_destino:
            # Iterando cada linha no arquivo de origem
            for linha in arquivo_origem:
                # Se a linha não começa com "//", escreva-a no arquivo de destino
                if not linha.strip().startswith("//"):
                    arquivo_destino.write(linha)

# Uso para atividade 1
copiar_conteudo_sem_comentarios("controller.cc", "controller_novo.cc")

def gerar_media_notas(arquivo_nomes, arquivo_notas):
    # Ler os nomes dos alunos
    with open(arquivo_nomes, 'r') as f:
        nomes = [nome.strip() for nome in f.readlines()]
    
    # Ler as notas dos alunos
    with open(arquivo_notas, 'r') as f:
        linhas_notas = [list(map(float, linha.split())) for linha in f.readlines()]
    
    # Processar e calcular a média
    medias = [(nome, sum(notas) / len(notas)) for nome, notas in zip(nomes, linhas_notas)]
    
    # Escrever no arquivo de saída
    path_saida = "media_alunos.txt"
    with open(path_saida, 'w') as f:
        for nome, media in medias:
            f.write(f"{nome}: {media:.2f}\n")

# Uso para atividade 2
gerar_media_notas("nomes.txt", "notas.txt")

def alterar_nota(arquivo_nomes, arquivo_notas, nome_aluno, nota_velha, nota_nova):
    # Ler os nomes dos alunos
    with open(arquivo_nomes, 'r') as f:
        nomes = [nome.strip() for nome in f.readlines()]
    
    # Encontrar o índice do aluno
    try:
        indice_aluno = nomes.index(nome_aluno)
    except ValueError:
        return f"Aluno {nome_aluno} não encontrado."
    
    # Ler as notas dos alunos
    with open(arquivo_notas, 'r') as f:
        linhas_notas = f.readlines()
    
    # Substituir a nota velha pela nova
    notas_aluno = list(map(float, linhas_notas[indice_aluno].split()))
    try:
        indice_nota = notas_aluno.index(nota_velha)
        notas_aluno[indice_nota] = nota_nova
    except ValueError:
        return f"Nota {nota_velha} não encontrada para o aluno {nome_aluno}."
    
    # Atualizar a linha com as novas notas
    linhas_notas[indice_aluno] = " ".join(map(str, notas_aluno)) + "\n"
    
    # Salvar as alterações no arquivo de notas
    with open(arquivo_notas, 'w') as f:
        f.writelines(linhas_notas)
    
    return f"Nota do aluno {nome_aluno} alterada com sucesso!"


nome = input("Digite o nome do aluno: ")
nota_velha = float(input("Digite a nota antiga: "))
nota_nova = float(input("Digite a nota nova: "))

# Uso para atividade 3
resultado = alterar_nota("nomes.txt", "notas.txt", nome, nota_velha, nota_nova)
gerar_media_notas("nomes.txt", "notas.txt")

print(resultado)

