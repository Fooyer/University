from collections import defaultdict

# Lendo o conteúdo do arquivo trace.txt
with open("trace.txt", 'r') as f:
    log_lines = f.readlines()

# Inicializando contadores e listas
total_solicitacoes = len(log_lines)
solicitacoes_por_metodo = defaultdict(int)
solicitacoes_bem_sucedidas = 0
solicitacoes_com_erros = 0
tamanho_total_respostas = 0

# Processando cada linha do log
for line in log_lines:
    parts = line.split('"')
    metodo, _, _ = parts[1].split(' ', 2)
    codigo_resposta = int(parts[2].split()[0])
    tamanho_resposta = int(parts[2].split()[1])
    
    # Atualizando contadores e listas
    solicitacoes_por_metodo[metodo] += 1
    if 200 <= codigo_resposta < 300:
        solicitacoes_bem_sucedidas += 1
    elif 400 <= codigo_resposta < 600:
        solicitacoes_com_erros += 1
    tamanho_total_respostas += tamanho_resposta

# Calculando o tamanho médio das respostas
tamanho_medio_respostas = tamanho_total_respostas / total_solicitacoes

total_solicitacoes, dict(solicitacoes_por_metodo), solicitacoes_bem_sucedidas, solicitacoes_com_erros, tamanho_medio_respostas

#Print mais formatado e bonito para as informações

print("======================================")
print(" RELATÓRIO DE ANÁLISE DO ARQUIVO LOG ")
print("======================================")
print(f"1) Total de solicitações: {total_solicitacoes}")
print("--------------------------------------")
print("2) Solicitações por método:")
for metodo, quantidade in solicitacoes_por_metodo.items():
    print(f"   - {metodo}: {quantidade} solicitações")
print("--------------------------------------")
print(f"3) Solicitações bem-sucedidas: {solicitacoes_bem_sucedidas}")
print(f"4) Solicitações com erros: {solicitacoes_com_erros}")
print("--------------------------------------")
print(f"5) Tamanho médio das respostas: {tamanho_medio_respostas:.2f} bytes")
print("======================================")