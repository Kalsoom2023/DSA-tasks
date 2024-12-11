class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashTable:
    def __init__(self, hsize):
        self.size = hsize
        self.table = [[] for _ in range(hsize)]
        self.keysOccupied = 0

    def getHashTableSize(self):
        return self.size

    def getNumberOfKeys(self):
        return self.keysOccupied

    def hashFunction(self, key):
        return sum(ord(c) for c in key) % self.size

    def updateKey(self, key, value):
        hash_val = self.hashFunction(key)
        for node in self.table[hash_val]:
            if node.key == key:
                node.value += value
                return
        self.table[hash_val].append(KeyNode(key, value))
        self.keysOccupied += 1
        if self.keysOccupied > self.size * 0.75:  # Trigger rehashing when load factor > 75%
            self.rehash()

    def searchKey(self, key):
        hash_val = self.hashFunction(key)
        for node in self.table[hash_val]:
            if node.key == key:
                return node.value
        return 0

    def rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.keysOccupied = 0
        for bucket in old_table:
            for node in bucket:
                self.updateKey(node.key, node.value)

# Word Count Program
def word_count(file_path):
    hash_table = MyHashTable(128)
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            hash_table.updateKey(word, 1)

    # Print word counts
    for bucket in hash_table.table:
        for node in bucket:
            print(f"{node.key} {node.value}")

# Example Usage
# Replace 'words.txt' with your file path
# word_count('words.txt')
