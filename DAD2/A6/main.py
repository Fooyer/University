class HashTable:
    def __init__(self, size=100):
        # Inicializar a tabela hash com um tamanho fixo.
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Função de hashing simples usando o valor ASCII das chaves.
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        # Inserir um par chave-valor na tabela hash.
        index = self._hash(key)
        for pair in self.table[index]:
            # Se a chave já estiver na lista, atualize o valor.
            if pair[0] == key:
                pair[1] = value
                return
        # Se a chave não estiver na lista, adicione-a.
        self.table[index].append([key, value])

    def get(self, key):
        # Buscar um valor pela chave.
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Se a chave não estiver presente, retorne None.

    def delete(self, key):
        # Excluir um par chave-valor pela chave.
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

# Exemplo de aplicação:

# Criar uma tabela hash
hash_table = HashTable()

# Inserir valores
hash_table.insert("nome", "João")
hash_table.insert("idade", "25")

# Buscar valores
print(hash_table.get("nome"))  # Saída: João
print(hash_table.get("idade"))  # Saída: 25

# Excluir valores
hash_table.delete("nome")
print(hash_table.get("nome"))  # Saída: None