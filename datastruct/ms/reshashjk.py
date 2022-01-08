class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class Hash:
    def __init__(self, table_size, max_collision=1000000,rehash_threshold=50) -> None:
        self.table_size = table_size
        self.length = 0
        self.table = [None for _ in range(self.table_size)]
        self.rehash_threshold = float(rehash_threshold)
        self.max_collision = max_collision

    def addLoop(self, data):
        self.bundle = data
        for d in data:
            H.rehash()
            H.insert(d)
            H.print()
            print("------------------------------")

    def insert(self, data):
        key_i = self.get_hash(data.key)

        if self.table[key_i] is None:
            self.table[key_i] = data
            self.length += 1

        else:
            for j in range(2, self.max_collision+1):
                new_key = (key_i+((j-1)**1)) % self.table_size
                if self.table[new_key] is None:
                    self.table[new_key] = data
                    self.length += 1
                    return

            new_table = self._rehash()
            new_table.add(data)
            self.table = new_table.table
            self.length = new_table.length
            self.table_size = new_table.table_size
            return

    def rehash(self):
        thd = self.table_size*self.rehash_threshold/100
        if self.length >= thd:
            print(
                f"*** Data over threshold resize from {self.table_size} to {self.table_size*2} ***")
            new_table = self._rehash()
            self.table = new_table.table
            self.table_size = new_table.table_size
            self.length = new_table.length

    def _rehash(self):
        extended_size = self.table_size*2
        new_table = Hash(
            extended_size, self.max_collision, self.rehash_threshold)

        for d in self:
            new_table.insert(d)

        return new_table

    def __getitem__(self, key):
        return self.table[key]

    def __iter__(self):
        for data in self.table:
            if data is not None:
                yield data

    def __len__(self):
        return self.length

    def get_hash(self, key):
        result = 0
        for c in key:
            result += ord(c)

        return result % self.table_size

    def print(self):
        for i in range(self.table_size):
            print(f"{i}\t{self.table[i]}")


print(" *** Hash Table ***")
info, data = input("Enter Input : ").split("/")
table_size = int(info)

data = data.split(",")
dr = []
for d in data:
    key = d.split()[0]
    value = d.split()[1]
    dr.append(Data(key, value))

H = Hash(table_size)
print("Initial Table")
H.print()
print("------------------------------")

H.addLoop(dr)
