
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next  # Default next node is None

    # def __str__(self):
        # return f"data:{self.data} next_node: {self.next}"


class LinkedList:
    def __init__(self, *args):
        self.head = Node()  # Place holder to the first index of the list, not the date node
        self.size = 0
        for d in args:
            self.append(d)

    def nodeAt(self, index):
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur

    def append(self, *args):
        for d in args:
            self.nodeAt(len(self)-1).next = Node(d)
            self.size += 1

    def push(self, *args):
        for d in args:
            self.head.next = Node(d, self.head.next)
            self.size += 1

    def print_elems(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def print_nodes(self):
        cur = self.head
        for _ in range(len(self)+1):
            print(str(cur),f"Data:{cur.data}",f"NextNode:{cur.next}")
            cur = cur.next

    def get(self, index):
        if index >= len(self) or index < 0:
            raise ValueError
        return self.nodeAt(index).data

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        if index >= len(self) or index < 0:
            raise ValueError
        prev = self.nodeAt(index-1)
        data = prev.next.data
        prev.next = prev.next.next
        self.size -= 1
        return data

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def clear(self):
        data = []
        while not self.is_empty():
            data.append(self.pop())
        return data

    def remove(self, data):
        cur = self.head
        for i,d in enumerate(self):
            if cur.next.data == data:
                cur.next = cur.next.next
                self.size -= 1
            cur = cur.next
        return data


        # prev = self.head
        # for d in self:
        #     if d == data:
        #         prev.next = prev.next.next
        #         self.size -= 1
        #         return data

    def removeAll(self,data):
        prev = self.head
        for d in self:
            if d == data:
                prev.next = prev.next.next
                self.size -= 1
            prev = prev.next
        return data

    def contains(self, data):
        cur = self.head
        for _ in range(len(self)):
            cur = cur.next
            if cur.data == data:
                return True
        return False

    def count(self, data):
        total = 0
        for d in self:
            if data == d:
                total += 1
        return total

    def indexOf(self, data):
        cur = self.head
        for i in range(len(self)):
            cur = cur.next
            if cur.data == data:
                return i
        return -1

    def set(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        self.nodeAt(index).data = data
        return data

    def insert(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        cur = self.nodeAt(index-1)
        cur.next = Node(data, cur.next)
        self.size += 1
        return data

    def insertAfter(self, index, data):
        return self.insert(index+1, data)

    def reverse(self):
        result = LinkedList()
        for i in range(len(self)-1, -1, -1):
            result.append(self[i])
        return result

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
        data = []
        cur = self.head
        for _ in range(len(self)):
            cur = cur.next
            data.append(cur.data)
        return str(data)

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, data):
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
        while cur.next != None:
            cur = cur.next
            yield cur.data
    
    def __contains__(self,data):
        return self.contains(data)


if __name__ == '__main__':
    x = LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9)
    y = LinkedList(65, 42, 18, 50, 22, 54)
    mylist = [100, 1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6]

    # for i in range(20):
        # x.append(39)

    # print(x)

    x.print_elems()
    x.print_nodes()