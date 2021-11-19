def hash_ascii_sum(key, moder):
    result = 0
    for c in key:
        result += ord(c)

    return result % moder


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class HashTable:
    def __init__(self, table_size, max_collision) -> None:
        self.table_size = table_size
        self.length = 0
        self.max_collision = max_collision
        self.table = [None for _ in range(self.table_size)]

    def add(self, data):
        key_index = self._get_hash(data.key)

        # Allocate the cell
        if self.table[key_index] is None:
            self.table[key_index] = data
            self.length += 1

        # Collision handling
        else:
            print("collision number 1 at", key_index)
            for j in range(2, self.max_collision+1):
                new_key = (key_index+((j-1)**2)) % self.table_size
                if self.table[new_key] is None:
                    self.table[new_key] = data
                    self.length += 1
                    return

                print("collision number", j, "at", new_key)
            # Discard
            print("Max of collisionChain")

    def __getitem__(self, key):
        return self.table[key]

    def __len__(self):
        return self.length

    def _get_hash(self, key):
        result = 0
        for c in key:
            result += ord(c)
        return result % self.table_size

    def print(self):
        for i in range(self.table_size):
            print(f"#{i+1}\t{self.table[i]}")


if __name__ == "__main__":

    print(" ***** Fun with hashing *****")
    a, kvs = input("Enter Input : ").split("/")
    table_size, max_coll = a.split()
    table_size = int(table_size)
    max_coll = int(max_coll)

    H = HashTable(table_size, max_coll)
    kvs = kvs.split(",")
    for kv in kvs:
        if len(H) >= H.table_size:
            print("This table is full !!!!!!")
            break
        key, value = kv.split()
        data = Data(key, value)
        H.add(data)
        H.print()
        print("---------------------------")
