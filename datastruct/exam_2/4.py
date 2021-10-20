class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    # def __str__(self):
    #     s = 'Linked data : '
    #     p = self.head
    #     while p != None:
    #         s += str(p.data)+' '
    #         p = p.next
    #     return s

    def __str__(self):
        return " <- ".join(str(d) for d in self)

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None:
            return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def __iter__(self):
        cur = self.head
        while cur != None:
            yield cur.data
            cur = cur.next

    def __add__(self, o: object):
        for data in o:
            self.append(data)
        return self

    def reverse(self) -> None:
        tray = list(self)
        self.head = None
        while tray != []:
            self.append(tray.pop())


def re_order(L):
    result = LinkedList()
    cur = L.head
    while(cur.data != 0):
        cur = cur.next
    result.append(cur.data)

    cur = cur.next

    if cur is not None:
        while(cur.data != 0):
            result.append(cur.data)
            cur = cur.next
            if cur is None:
                break

    cur = L.head
    while(cur.data != 0):
        result.append(cur.data)
        cur = cur.next

    return result


if __name__ == "__main__":

    print(" *** Re order ***")
    numbers = [int(d) for d in input("Enter Input : ").split()]

    my_list = LinkedList()
    my_list += numbers

    print("Before : ", end='')

    print(my_list)

    print("After : ", end='')

    my_list = re_order(my_list)

    print(my_list)
