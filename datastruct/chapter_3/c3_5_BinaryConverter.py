class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, *data):
        for d in data:
            self.items.append(d)
            self.length += 1

    def pop(self, index=None):
        if self.length <= 0:
            raise IndexError
        else:
            if index is None:
                self.length -= 1
                return self.items.pop()
            else:
                self.items.pop(index)
                self.length -= 1

    def top(self):
        return self[-1]

    def is_empty(self):
        return True if self.size() == 0 else False

    def size(self):
        return self.length

    def count(self, value):
        """Count occurences of the value in the Stack"""
        count = 0
        for data in self:
            if data == value:
                count += 1
        return count

    def delete(self, value):
        """ Delete all specified value from Stack"""
        count = 0
        i = 0
        while i < self.size():
            if self[i] == value:
                self.pop(i)
                count += 1
                i -= 1
            i += 1
        return count

    def delete_lower_than(self, reference_value):
        """ Delete all values in Stack lower than the reference value

        Args:
            reference_value : the value to be reference

        Returns:
            list : list of values those were deleted
        """
        deleted = list()
        for data in self:
            if data < reference_value:
                deleted.extend([data for _ in range(self.count(data))])
                self.delete(data)
        return deleted

    def delete_one_more_than(self, reference_value):
        for data in self:
            if data > reference_value:
                self.pop(self.items.index(data))
                return data

    def delete_one_less_than(self, reference_value):
        for data in self:
            if data < reference_value:
                self.pop(self.items.index(data))
                return data

    def delete_more_than(self, reference_value):
        """ Delete all values in Stack greater than the reference value

        Args:
            reference_value : the value to be reference

        Returns:
            list : list of values those were deleted
        """
        deleted = list()
        for data in self:
            if data > reference_value:
                deleted.extend([data for _ in range(self.count(data))])
                self.delete(data)
        return deleted

    def __len__(self):
        return self.length

    def __iter__(self):
        for data in self.items:
            yield data

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __str__(self):
        output = "[" + ", ".join([str(data) for data in self]) + "]"
        return output




if __name__ == "__main__":
    print(" ***Decimal to Binary use Stack***")
    num = int(input('Enter decimal number : '))
    stack = Stack()
    while num > 0:
        stack.push(num%2) 
        num = num // 2

    result = ""
    while not stack.is_empty():
        result += str(stack.pop())

    print( "Binary number :", result)