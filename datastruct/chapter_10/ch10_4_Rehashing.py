import math
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{1}".format(self.key, self.value)


class HashTable:
    def __init__(self, table_size, max_collision,rehash_threshold) -> None:
        self.table_size = table_size
        self.length = 0
        self.max_collision = max_collision
        self.table = [None for _ in range(self.table_size)]
        self.rehash_threshold = float(rehash_threshold)

    def add(self, data):
        # Check if reached the threshold
        thd = self.table_size*self.rehash_threshold/100
        if self.length+1 > thd:
            self = self.rehash()

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
            new_table = self.rehash()
            new_table.add(data)
            self.table = new_table.table
            self.length = new_table.length
            self.table_size = new_table.table_size
            return

    def rehash(self):
        print("R")
        extended_size = self.nextPrime(self.table_size*2)
        new_table = HashTable(extended_size,self.max_collision,self.rehash_threshold)
        for data in self:
            new_table.add(Data(data,data))

        return new_table

    def isPrime(self,n):
        if(n <= 1):
            return False
        if(n <= 3):
            return True
        
        if(n % 2 == 0 or n % 3 == 0):
            return False
        
        for i in range(5,int(math.sqrt(n) + 1), 6):
            if(n % i == 0 or n % (i + 2) == 0):
                return False
        return True
 
    def nextPrime(self,N):
        if (N <= 1):
            return 2
        prime = N
        found = False
    
        while(not found):
            prime = prime + 1
    
            if(self.isPrime(prime) == True):
                found = True
        return prime

    def __getitem__(self, key):
        return self.table[key]

    def __iter__(self):
        for data in self.table:
            if data is not None:
                yield data.value

    def __len__(self):
        return self.length

    def _get_hash(self, key):
        # result = 0
        # for c in key:
        #     result += ord(c)
        # return result % self.table_size
        return key%self.table_size

    def print(self):
        for i in range(self.table_size):
            print(f"#{i+1}\t{self.table[i]}")


if __name__ == "__main__":

    print(" ***** Rehashing *****")
    info, data = input("Enter Input : ").split("/")
    table_size, max_collision, threshold = info.split()
    data = [int(x) for x in data.split()]

    H = HashTable(int(table_size),int(max_collision),float(threshold))
    print("Initial Table : ")
    H.print()

    for d in data:
        print("Add :",d)
        d = Data(d,d)
        H.add(d)
        H.print()
        print("----------------------------------------")
    