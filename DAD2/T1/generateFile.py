import random
import string

# Abrir o arquivo para escrita
with open('1000valores.txt', 'w') as f:
    # Escrever 1000 valores aleatórios no arquivo
    for i in range(1000):
        valor = random.randint(0, 1000)
        f.write(str(valor) + '\n')

# Abrir o arquivo para escrita
with open('10000valores.txt', 'w') as f:
    # Escrever 1000 valores aleatórios no arquivo
    for i in range(10000):
        valor = random.randint(0, 10000)
        f.write(str(valor) + '\n')

# Abrir o arquivo para escrita
with open('100000valores.txt', 'w') as f:
    # Escrever 1000 valores aleatórios no arquivo
    for i in range(100000):
        valor = random.randint(0, 100000)
        f.write(str(valor) + '\n')


# Define a function to generate random words
def generate_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Generate 3 files of random words
for n in [1000,10000,100000]:
    with open(f'{n}words.txt', 'w') as f:
        for i in range(n):
            word = generate_word(random.randint(1, 10))
            f.write(word + '\n')
