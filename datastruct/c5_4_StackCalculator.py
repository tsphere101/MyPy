
class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next  # Default next node is None
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = Node()  # Place holder to the first index of the list, not the data node
        self.tail = Node()  # Place holder to the last index of the list, not the data Node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

        if iterable is not None:
            for data in iterable:
                self.append(data)

    def node_at(self, index):
        if index <= self.size//2:
            cur = self.head
            for _ in range(index+1):
                cur = cur.next
            return cur
        else:
            index = (self.size-1) - index
            cur = self.tail
            for _ in range(index+1):
                cur = cur.prev
            return cur

    def append(self, *args):
        # Insert element at the end of the list
        for data in args:
            cur = self.tail
            cur = cur.prev
            new_node = Node(data, self.tail, cur)
            cur.next = new_node
            self.tail.prev = new_node
            self.size += 1

    def push(self, *args):
        # Insert the element at the first of the list
        for data in args:
            cur = self.head
            cur = cur.next
            new_node = Node(data, cur, self.head)
            cur.prev = new_node
            self.head.next = new_node
            self.size += 1

    def extend(self, list_of_iterable):
        for d in list_of_iterable:
            self.append(d)

    def print_nodes(self):
        cur = self.head
        for _ in range(len(self)+1):
            print(str(cur), f"Data:{cur.data}", f"NextNode:{cur.next}")
            cur = cur.next

    def __get(self, index):
        if index >= len(self) or index < 0:
            raise ValueError
        return self.node_at(index).data

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        if index >= len(self) or index < 0:
            raise ValueError

        cur = self.node_at(index)
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        data = cur.data
        self.size -= 1
        return data

    def is_empty(self):
        return self.size == 0

    def is_not_empty(self):
        return self.size != 0

    def clear(self):
        self = DoublyLinkedList()

    def remove(self, data):
        cur = self.head
        for i, d in enumerate(self):
            if cur.next.data == data:
                cur.next = cur.next.next
                self.size -= 1
            cur = cur.next
        return data

    def removeAll(self, data):
        prev = self.head
        for d in self:
            if d == data:
                prev.next = prev.next.next
                self.size -= 1
            prev = prev.next
        return data

    def contains(self, data):
        for d in self:
            if d == data:
                return True
        return False

    def count(self, data):
        total = 0
        for d in self:
            if data == d:
                total += 1
        return total

    def index(self, data):
        for i, d in enumerate(self):
            if d == data:
                return i
        raise ValueError(f"{data} is not in list.")

    def set(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        self.node_at(index).data = data
        return data

    def insert(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        cur = self.node_at(index-1)
        cur.next = Node(data, cur.next)
        self.size += 1
        return data

    def insertAfter(self, index, data):
        return self.insert(index+1, data)

    def reverse(self):
        result = DoublyLinkedList()
        for i in range(len(self)-1, -1, -1):
            result.append(self[i])
        return result

    def copy(self):
        c = DoublyLinkedList()
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

        low, equal, high = DoublyLinkedList(), DoublyLinkedList(), DoublyLinkedList()
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
        data = []
        cur = self.head
        for _ in range(len(self)):
            cur = cur.next
            data.append(cur.data)
        return str(data)

    def __getitem__(self, index):
        if self.is_empty():
            raise IndexError
        if index < 0:
            index += self.size
        if index >= self.size:
            raise IndexError
        return self.__get(index)

    def __setitem__(self, index, data):
        if self.is_empty():
            raise IndexError
        if index < 0:
            index += self.size
        if index >= self.size:
            raise IndexError
        self.set(index, data)

    def __eq__(self, o: object) -> bool:
        if len(self) != len(o):
            return False
        for i, data in enumerate(self):
            if o.get(i) != data:
                return False
        return True

    def __add__(self, o: object):
        for data in o:
            self.append(data)
        return self

    def __iter__(self):
        cur = self.head
        while cur.next.next != None:
            cur = cur.next
            yield cur.data

    def __contains__(self, data):
        return self.contains(data)


class Stack(DoublyLinkedList):
    def top(self):
        return self[-1]

    def push(self, data):
        # Override push, insert the element at the last of the list instead of the first of the list.
        self.append(data)


class StackCalc:

    def __init__(self):
        self.stack = Stack()
        self.stack.push(0)
        self.bad_instruction = False

    def run(self, arg):
        arg = arg.split()
        for s in arg:
            if s.isnumeric():
                self.stack.push(int(s))

            elif s == "+":
                temp = self.stack.pop() + self.stack.pop()
                self.stack.push(temp)
            elif s == "-":
                temp = self.stack.pop() - self.stack.pop()
                self.stack.push(temp)
            elif s == "*":
                temp = self.stack.pop() * self.stack.pop()
                self.stack.push(temp)
            elif s == "/":
                temp = self.stack.pop() / self.stack.pop()
                if temp.is_integer():
                    temp = int(temp)
                self.stack.push(temp)
            elif s.lower() == "dup":
                self.stack.push(self.stack.top())
            elif s.lower() == "pop":
                self.stack.pop()
            elif s.lower() == "psh":
                # I don't know what to do!
                pass
            else:
                self.invalid_instruction(s)
                return

    def invalid_instruction(self, s):
        self.bad_instruction = True
        self.kw = s

    def getValue(self):
        if self.bad_instruction:
            return "Invalid instruction: " + self.kw

        return str(self.stack.top())


if __name__ == "__main__":


    print("* Stack Calculator *")
    arg = input("Enter arguments : ")
    machine = StackCalc()
    machine.run(arg)
    print(machine.getValue())
