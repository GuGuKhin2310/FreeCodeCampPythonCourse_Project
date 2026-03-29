class HashTable:
    def __init__(self):
        self.collection = dict()
    
    def hash(self, key= ""):
        return sum(ord(char) for char in key)

    def add(self,key,value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value
        return self.collection
            
    def remove(self,key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
        return None
        
    def lookup(self,key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        return None

my_table = HashTable()
print(my_table.hash('golf'))
print(my_table.add('golf', 'sport'))
print(my_table.add('dear', 'friend'))
print(my_table.add('read', 'book'))
my_table.add('rose', 'flower')
my_table.add('fcc', 'coding')
my_table.add('cfc','chemical')
print(my_table.remove('cfc'))
print(my_table.lookup('golf'))
print(my_table.collection)
