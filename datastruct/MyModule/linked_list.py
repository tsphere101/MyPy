
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, iterable=None):
        self.head = Node()
        self.tail = Node(None,self.head)
        self.size = 0

        if iterable is not None:
            for data in iterable:
                self.append(data)

    def node_at(self, index):
        if index == self.size-1:
            return self.tail.next
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur

    def append(self, data):
        cur = self.node_at(self.size-1)
        new_node = Node(data,self.tail) # สร้าง Node ใหม่
        cur.next = new_node # เพิ่มข้อมูลสุดท้าย 
        self.tail.next = new_node # Tail ชี้ย้อนกลับมา
        self.size += 1

    def extend(self, iterable):
        for d in iterable:
            self.append(d)

    def pop(self, index=None):
        if index is not None:
            if self.size == 0 or index >= self.size:
                raise IndexError(f"Index out of range.")
            cur = self.node_at(index-1)
            data = cur.next.data
            cur.next = cur.next.next
            self.size -= 1
            return data

        else:
            index = self.size-1
            return self.pop(index)

    def is_empty(self):
        return self.size == 0

    def is_not_empty(self):
        return self.size != 0

    def clear(self):
        self = LinkedList()

    def remove(self, data):
        cur = self.head
        for _ in range(self.size):
            if cur.next.data == data:
                cur.next = cur.next.next
                self.size -= 1
                return data
        raise ValueError(f"{data} is not in the list.")

    def contains(self, data):
        for d in self:
            if d == data:
                return True
        return False

    def index(self, data):
        for i, d in enumerate(self):
            if d == data:
                return i
        raise ValueError(f"{data} is not in the list.")

    def __set(self, index, data):
        if index >= len(self) or index < 0:
            raise IndexError
        self.node_at(index).data = data
        return data

    def __get(self, index):
        if index >= len(self) or index < 0:
            raise IndexError
        return self.node_at(index).data

    def insert(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError

        cur = self.node_at(index-1)
        cur.next = Node(data, cur.next)
        self.size += 1
        return data

    def copy(self):
        c = LinkedList()
        for data in self:
            c.append(data)
        return c

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ", ".join(str(data) for data in self) + "]"

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

        self.__set(index, data)

    def __eq__(self, o: object):
        if len(self) != len(o):
            return False
        for i, data in enumerate(self):
            if o.get(i) != data:
                return False
        return True

    def __add__(self,o:object):
        for data in o:
            self.append(data)
        return self

    def __iter__(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            yield cur.data

    def __contains__(self,data):
        return self.contains(data)

class Queue(LinkedList):
    def enqueue(self,data):
        self.append(data)

    def dequeue(self):
        return self.pop()

if __name__ == "__main__":
    
    x = Queue()
    x.enqueue(5)
    x.enqueue(5)
    x.enqueue(5)
    print(x)