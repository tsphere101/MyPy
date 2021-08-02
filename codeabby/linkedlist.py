
from median_of_array import median_of_array


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next  # Default next node is None

    def __str__(self):
        return f"data:{self.data} next_node: {self.next}"


class LinkedList:
    def __init__(self, *args):
        self.head = Node()  # Place holder to the first index of the list, not the date node
        for d in args:
            self.append(d)

    def append(self, *args):
        cur = self.head
        while cur.next != None:
            cur = cur.next

        for d in args:
            cur.next = Node(d)
            cur = cur.next

    def push_back(self, *args):
        for d in args:
            new_node = Node(d)
            new_node.next = self.head.next
            self.head.next = new_node

    def print_elems(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        if index >= len(self) or index < 0:
            raise ValueError
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.data

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        if index >= len(self) or index < 0:
            raise ValueError
        cur = self.head
        for _ in range(index):
            cur = cur.next
        data = cur.next.data
        cur.next = cur.next.next
        return data

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def empty(self):
        data = []
        while not self.is_empty():
            data.append(self.pop())
        return data

    def set(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        cur.data = data
        return data

    def reverse(self):
        result = LinkedList()
        for i in range(len(self)-1, -1, -1):
            result.append(self[i])
        return result

    def sort(self, reverse=False):
        pass

    def copy(self):
        c = LinkedList()
        for data in self:
            c.append(data)
        return c

    def sort(self):
        result = self.copy()
        if len(result) <= 1:
            return result
        
        a,b,c = result[0],result[int((len(result)-1)/2)],result[len(result)-1]
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
        return low.sort()+equal+high.sort()

    def __len__(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

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


def quicksort(data):
    def median_of_three(data):
        a, b, c = data
        median = 0
        if a > b:
            if a < c:
                median = a
            elif b > c:
                median = b
            else:
                median = c
        else:
            if a > c:
                median = a
            elif b < c:
                median = b
            else:
                median = c

        return median
    if len(data) <= 1:
        return data
    pivot = median_of_three(
        (data[0], data[len(data)-1], data[int((len(data)-1)/2)]))
    low, equal, high = LinkedList(), LinkedList(), LinkedList()
    for d in data:
        if d == pivot:
            equal.append(d)
        elif d > pivot:
            high.append(d)
        elif d < pivot:
            low.append(d)

    return quicksort(low)+equal+quicksort(high)


if __name__ == '__main__':
    x = LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9)
    y = LinkedList(65, 42, 18, 50, 22, 54)

    x.sort()
    print(x)