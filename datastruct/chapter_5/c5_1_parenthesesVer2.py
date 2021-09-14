class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, iterable=None):
        self.head = Node()
        self.tail = self.head
        self.size = 0

        if iterable != None:
            try:
                for d in iterable:
                    self.append(d)
            except:
                raise TypeError

    def at_node(self, index):
        current_node = self.head
        for _ in range(index+1):
            current_node = current_node.next
        return current_node

    def append(self, *args):
        for data in args:
            new_node = Node(data)
            self.at_node(self.size-1).next = new_node
            self.tail = new_node
            self.size += 1

    def extend(self, iterable):
        for data in iterable:
            self.append(data)

    def pop(self, index=None):
        if index is None:
            index = self.size-1  # last elemnt of the list

        if index < 0:
            index += self.size

        if index >= self.size or index < 0:
            raise IndexError

        previous_node = self.at_node(index-1)
        current_node = previous_node.next
        data = current_node.data
        if current_node.next is None:
            self.tail = previous_node
        previous_node.next = current_node.next  # patch the scar
        self.size -= 1
        return data

    def is_empty(self):
        return True if self.size == 0 else False

    def is_not_empty(self):
        return True if self.size > 0 else False

    def clear(self):
        self = LinkedList()

    def remove(self, data):
        for index, d in enumerate(self):
            if d == data:
                self.pop(index)
        return data

    def set(self, index, data):
        if index >= self.size or index < 0:
            raise IndexError
        self.at_node(index).data = data
        return data

    def index(self, data):
        current_node = self.head
        for i in range(self.size):
            current_node = current_node.next
            if current_node.data == data:
                return i
        return -1

    def remove_at_index(self, *indices):
        to_remove = LinkedList()
        for data in indices:
            to_remove.append(data)

        to_remove = to_remove.sort(reverse=True)
        for i in to_remove:
            self.pop(i)

    def copy(self):
        c = LinkedList()
        for data in self:
            c.append(data)
        return c

    def sort(self, reverse=False):
        result = self.copy()
        if len(result) <= 1:
            return result

        a, b, c = result[0], result[int(
            (len(result)-1)/2)], result[len(result)-1]
        pivot = 0
        if a > b:
            if a < c:
                pivot = a
            elif b > c:
                pivot = b
            else:
                pivot = c
        else:
            if a > c:
                pivot = a
            elif b < c:
                pivot = b
            else:
                pivot = c

        low, equal, high = LinkedList(), LinkedList(), LinkedList()
        for d in result:
            if d == pivot:
                equal.append(d)
            elif d > pivot:
                high.append(d)
            elif d < pivot:
                low.append(d)

        result = low.sort()+equal+high.sort()
        if reverse:
            return result.reverse()
        else:
            return result

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ",".join(str(x) for x in self) + "]"

    def __getitem__(self, index):
        while index < 0:
            index += self.size
        if index >= self.size:
            raise IndexError
        return self.get(index)

    def __setitem__(self, index, data):
        while index < 0:
            index += self.size
        if index >= self.size:
            raise IndexError
        self.set(index, data)

    def __eq__(self, o: object) -> bool:
        if self.size != len(o):
            return False
        for i, data in enumerate(self):
            if o[i] != data:
                return False
        return True

    def __add__(self, o: object):
        for data in o:
            self.append(data)
        return self

    def __iter__(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            yield current_node.data

    def __contains__(self, data):
        for d in self:
            if d == data:
                return True
        return False


if __name__ == "__main__":

    input_data = input("Enter Input : ")
    print("Parentheses :", end="")
    normal_paren = LinkedList()
    square_paren = LinkedList()
    for c in input_data:
        if c == "(":
            normal_paren.append(c)
        elif c == "[":
            square_paren.append(c)

        elif c == ")":
            if normal_paren.is_empty():
                print(" Unmatched ! ! !")
                exit()
            normal_paren.pop()

        elif c == "]":
            if square_paren.is_empty():
                print(" Unmatched ! ! !")
                exit()
            square_paren.pop()

    if normal_paren.is_not_empty() or square_paren.is_not_empty():
        print(" Unmatched ! ! !")
    else:
        print(" Matched ! ! !")
