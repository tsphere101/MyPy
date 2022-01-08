class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class HashTable:
    def __init__(self, table_size, max_collision=99999999, rehash_threshold=50) -> None:
        self.table_size = table_size
        self.length = 0
        self.max_collision = max_collision
        self.table = [None for _ in range(self.table_size)]
        self.rehash_threshold = float(rehash_threshold)

    def add_bundle(self, data):
        self.bundle = data
        for d in data:
            H.rrh()
            H.add(d)
            H.print()
            print("------------------------------")

    def add(self, data):
        # if self.length+1 > thd:
        #     print(
        #         f"*** Data over threshold resize from {self.table_size} to {self.table_size*2} ***")
        #     new_table = self.rehash()
        #     self.table = new_table.table
        #     self.table_size = new_table.table_size
        #     self.length = new_table.length

        key_index = self.get_hash(data.key)

        if self.table[key_index] is None:
            self.table[key_index] = data
            self.length += 1

        else:
            for j in range(2, self.max_collision+1):
                new_key = (key_index+((j-1)**1)) % self.table_size
                if self.table[new_key] is None:
                    self.table[new_key] = data
                    self.length += 1
                    return

            new_table = self.rehash()
            new_table.add(data)
            self.table = new_table.table
            self.length = new_table.length
            self.table_size = new_table.table_size
            return

         # Rehash
        # print("self.length",self.length,"thhd",thd)
    def rrh(self):
        thd = self.table_size*self.rehash_threshold/100
        if self.length >= thd:
            print(
                f"*** Data over threshold resize from {self.table_size} to {self.table_size*2} ***")
            new_table = self.rehash()
            self.table = new_table.table
            self.table_size = new_table.table_size
            self.length = new_table.length

    def rehash(self):
        extended_size = self.table_size*2
        new_table = HashTable(
            extended_size, self.max_collision, self.rehash_threshold)

        # for i in range(self.length):
        #     data = self.bundle[i]
        #     new_table.add(data)
        for d in self:
            new_table.add(d)

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
        # sum ascii
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

H = HashTable(table_size)
print("Initial Table")
H.print()
print("------------------------------")

H.add_bundle(dr)

# for d in H:
#     print(type(d))
