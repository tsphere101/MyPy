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

    def extend(self, list_of_iterable):
        for d in list_of_iterable:
            self.append(d)

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
            print(str(cur), f"Data:{cur.data}", f"NextNode:{cur.next}")
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
        return True if self.size == 0 else False

    def is_not_empty(self):
        return True if self.size > 0 else False

    def clear(self):
        data = []
        while not self.is_empty():
            data.append(self.pop())
        return data

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

    def __contains__(self, data):
        return self.contains(data)


class Queue(LinkedList):

    def front(self):
        return self[0]

    def rear(self):
        return self[-1]

    def head(self):
        return self[0]

    def tail(self):
        return self[-1]

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        return self.pop(0)


def exploding(string):
    tray = Queue()
    residue = Queue()
    explodes_position = Queue()
    explodes_color = Queue()

    for i in range(len(string)):
        if len(tray) != 3:  # make up to 3
            tray.enqueue(string[i])

        if len(tray) >= 3:
            if tray[0] == tray[1] == tray[2]:
                # explode
                explodes_position.enqueue(i-1)
                explodes_color.enqueue(string[i])
                tray.clear()
            else:
                residue.enqueue(tray.dequeue())
    residue.extend(tray)

    # calling recursion
    if len(explodes_position) > 0:
        recur = exploding(residue)
        residue = recur[0]
        explodes_position.extend(recur[1])
        explodes_color.extend(recur[2])

    return residue, explodes_position, explodes_color


if __name__ == "__main__":

    inp = input("Enter Input (Normal, Mirror) : ")
    normal, mirror = inp.split()

    mirror = mirror[::-1]
    mir_res, mir_ex_pos, mir_obs = exploding(mirror)

    nor_ex_pos = exploding(normal)[1]

    interrupt_failed = 0
    nor_with_obsted = Queue()
    for i in range(len(normal)):
        nor_with_obsted.enqueue(normal[i])
        if nor_ex_pos.is_not_empty() and mir_obs.is_not_empty():
            if i == nor_ex_pos.front():
                # Interrupting
                if normal[i] == mir_obs.front():
                    interrupt_failed += 1
                nor_with_obsted.enqueue(mir_obs.dequeue())
                nor_ex_pos.dequeue()

    nor_res_after_obsted, nor_ex_pos_after_obsted, nor_ex_color_after_obsted = exploding(
        nor_with_obsted)

    ### DISPLAY ###

    print("NORMAL :")
    print(len(nor_res_after_obsted))
    if nor_res_after_obsted.is_not_empty():
        print("".join(nor_res_after_obsted.reverse()))
    else:
        print("Empty")
    print(len(nor_ex_pos_after_obsted) -
          interrupt_failed, "Explosive(s) ! ! ! (NORMAL)")
    if interrupt_failed > 0:
        print(f"Failed Interrupted {interrupt_failed} Bomb(s)")
    print("------------MIRROR------------")
    print(": RORRIM")
    print(len(mir_res))
    if mir_res.is_not_empty():
        print("".join(mir_res.reverse()))
    else:
        print("ytpmE")
    print("(RORRIM) ! ! ! (s)evisolpxE", len(mir_ex_pos))
