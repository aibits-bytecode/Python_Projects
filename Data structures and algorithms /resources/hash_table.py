class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __setitem__(self, key, value):
        # this works as : ht['abc'] = 10
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __getitem__(self, key):
        # this works as : ht['abc']
        h = self.get_hash(key)
        for element in self.arr[h]:
            if len(element) == 2 and element[0] == key:
                return element[1]
        return 'Not found'

    def __delitem__(self, key):
        # this works as : del ht['abc']
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                del self.arr[h][idx]
                return
        return 'Not found'


if __name__ == '__main__':
    ht = HashTable()
