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

        for d in deleted:
            self.items.remove(d)
            
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

        for d in deleted:
            self.items.remove(d)

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


def ManageStack(input_command):
    stack = Stack()
    for data in input_command:

        command = data.split()[0]
        arg = ""
        try:
            arg = data.split()[1]
            arg = int(arg)
        except:
            pass

        if command.lower() == "p":
            if not stack.is_empty():
                print("Pop =", int(stack.pop()))
            else:
                print(-1)
        if data[0].lower() == "a":
            adding_value = int(data.split()[1])
            stack.push(adding_value)
            print(f"Add = {adding_value}")
        if command.lower() == "d":
            if stack.is_empty():
                print(-1)
            else:
                deleteing_value = int(data.split()[1])
                deleted_value = [deleteing_value for _ in range(
                    stack.delete(deleteing_value))]
                if deleted_value is not []:
                    for data in deleted_value:
                        print(f"Delete = {data}")

        if command.lower() == "md":
            if stack.is_empty():
                print(-1)
            else:
                reference_value = arg
                deleted_value = stack.delete_more_than(reference_value)
                if len(deleted_value) > 0:
                    for i in range(len(deleted_value)-1,-1,-1):
                        print(
                            f"Delete = {deleted_value[i]} Because {deleted_value[i]} is more than {reference_value}")

        if command.lower() == "ld":
            if stack.is_empty():
                print(-1)
            else:
                reference_value = arg
                deleted_value = stack.delete_lower_than(reference_value)
                if len(deleted_value) > 0:
                    for i in range(len(deleted_value)-1,-1,-1):
                        print(
                            f"Delete = {deleted_value[i]} Because {deleted_value[i]} is less than {reference_value}")

    print("Value in Stack =", stack)


if __name__ == '__main__':
    input_command = input("Enter Input : ").split(",")

    ManageStack(input_command)
