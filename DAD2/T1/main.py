import time

def word_to_ascii_list(word):
    return [ord(char) for char in word]

def counting_sort_for_words(words):
    # Convertendo cada palavra em uma lista de valores ASCII
    ascii_values = [word_to_ascii_list(word) for word in words]
    
    # Ordenando as palavras pelo valor ASCII de seus caracteres
    sorted_words = [word for _, word in sorted(zip(ascii_values, words))]
    
    return sorted_words

def counting_sort(arr):
    start_time = time.time()
    
    # Se o primeiro item da lista é uma string, usamos o counting_sort_for_words
    if isinstance(arr[0], str):
        sorted_values = counting_sort_for_words(arr)
    else:
        max_val = max(arr)
        min_val = min(arr)
        count = [0] * (max_val - min_val + 1)
        for num in arr:
            count[num - min_val] += 1
        i = 0
        for j in range(len(count)):
            while count[j] > 0:
                arr[i] = j + min_val
                i += 1
                count[j] -= 1
        sorted_values = arr
        
    end_time = time.time()
    return sorted_values, end_time - start_time

def read_and_sort(filename):
    with open(filename, 'r') as file:
        values = [line.strip() for line in file]
    
    try:
        # Tentando converter os valores para inteiros
        values = [int(val) for val in values]
    except ValueError:
        # Se não conseguir, os valores são tratados como strings
        pass
    
    sorted_values, elapsed_time = counting_sort(values)
    
    with open(filename, 'w') as file:
        for value in sorted_values:
            file.write(str(value) + '\n')
    
    print(f"Arquivo {filename} ordenado em {elapsed_time:.5f} segundos!")

# Lista de arquivos
filenames = ["1000valores.txt", "10000valores.txt", "100000valores.txt", "1000words.txt", "10000words.txt", "100000words.txt"]

for filename in filenames:
    read_and_sort(filename)
