class SinglyNode:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next  # Default next node is None


class TailNode:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev


class SinglyLinkedList:
    def __init__(self, iterable=None):
        # Place holder to the first index of the list, not containing any data.
        self.head = SinglyNode()
        # Place holder to the last index of the list, not containing any data.
        self.tail = TailNode(None, None, self.head)
        self.size = 0

        if iterable is not None:
            for data in iterable:
                self.append(data)

    def node_at(self, index):
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur

    def append(self, *args):
        for data in args:
            cur = self.tail
            cur = cur.prev
            new_node = SinglyNode(data, self.tail)
            cur.next = new_node
            self.tail.prev = new_node
            self.size += 1

    def push(self, *args):
        for data in args:
            cur = self.head
            cur = cur.next
            new_node = SinglyNode(data, cur)
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

        cur = self.node_at(index-1)
        data = cur.next.data
        cur.next = cur.next.next
        if cur.next.next is None:
            # If the removing element is next to the tail
            self.tail.prev = cur
        self.size -= 1
        return data

    def is_empty(self):
        return self.size == 0

    def is_not_empty(self):
        return self.size != 0

    def clear(self):
        self = SinglyLinkedList()

    def remove(self, data):
        cur = self.head
        for _ in range(self.size):
            if cur.next.data == data:
                cur.next = cur.next.next
                if cur.next.next is None:
                    # If the removing element is next to the tail
                    self.tail.prev = cur
                self.size -= 1
                return data
            cur = cur.next

        raise ValueError(f"{data} is not in list.")

    def remove_all(self, data):
        """Remove all occurrences of the data in the list.

        Args:
            data : object to be remove from the list.

        Returns:
            int : number of removed objects.
        """

        to_remove = SinglyLinkedList()
        for i in range(self.size):
            if self[i] == data:
                to_remove.append(i)
        to_remove = to_remove.reverse()
        for index in to_remove:
            self.pop(index)

        return len(to_remove)

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

    def __set(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        self.node_at(index).data = data
        return data

    def insert(self, index, data):
        if index >= len(self) or index < 0:
            raise ValueError
        cur = self.node_at(index-1)
        cur.next = SinglyNode(data, cur.next)
        self.size += 1
        return data

    def insertAfter(self, index, data):
        return self.insert(index+1, data)

    def reverse(self):
        result = SinglyLinkedList()
        for i in range(len(self)-1, -1, -1):
            result.append(self[i])
        return result

    def copy(self):
        c = SinglyLinkedList()
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

        low, equal, high = SinglyLinkedList(), SinglyLinkedList(), SinglyLinkedList()
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
        self.__set(index, data)

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


def createLL(LL):
    return Scramble(LL)


def printLL(head):
    return str(head)


def SIZE(head):
    return len(head)


def scarmble(head, bottomup_percentage, riffleshuffle_percentage):
    scm = Scramble(head)
    scm.set_bottomup_percentage(bottomup_percentage)
    scm.set_riffleshuffle_percentage(riffleshuffle_percentage)

    print(f"BottomUp {bottomup_percentage:.3f} % : ", end="")
    scm.bottomup()
    print(scm)
    print(f"Riffle {riffleshuffle_percentage:.3f} % : ", end="")
    scm.riffleshuffle()
    print(scm)
    print(f"Deriffle {riffleshuffle_percentage:.3f} % : ", end="")
    scm.deriffle()
    print(scm)
    print(f"Debottomup {bottomup_percentage:.3f} % : ", end="")
    scm.debottomup()
    print(scm)


class Scramble:
    def __init__(self, iterable):
        self.pile = SinglyLinkedList(iterable)

    def set_bottomup_percentage(self, value):
        self.bottomup_percentage = value

    def set_riffleshuffle_percentage(self, value):
        self.riffleshuffle_percentage = value

    def bottomup(self):
        percent = self.bottomup_percentage
        n_of_percentage = int(percent*self.pile.size/100)

        old_tail_node = self.pile.tail.prev
        old_head_node = self.pile.head.next
        # traverse to the broken node
        last_node = self.pile.node_at(n_of_percentage-1)
        self.pile.head.next = last_node.next  # Set new head
        last_node.next = self.pile.tail  # Set new tail
        old_tail_node.next = old_head_node  # linked old tail to old head
        self.pile.tail.prev = last_node

        return self.pile

    def riffleshuffle(self):
        percent = self.riffleshuffle_percentage
        n = int((percent*self.pile.size)/100)
        last_node = self.pile.node_at(n-1)
        i = 0
        for _ in range(n-1):
            m = last_node.next
            last_node.next = m.next
            prev = self.pile.node_at(i)
            i += 2
            cur = prev.next
            prev.next = m
            m.next = cur
            if last_node.next is self.pile.tail:
                self.pile.tail.prev = last_node
                break

    # def riffleshuffle(self):
    #     percent = self.riffleshuffle_percentage
    #     n_of_percentage = int((percent*self.pile.size)/100)
    #     cur = self.pile.head.next
    #     before_riff = self.pile.node_at(n_of_percentage-1)
    #     riff = before_riff.next
    #     before_riff.next = self.pile.tail
    #     while cur.next is not self.pile.tail and riff.next is not self.pile.tail:
    #         prev = cur
    #         prev_riff = riff
    #         cur = cur.next
    #         riff = riff.next
    #         prev.next = prev_riff
    #         prev_riff.next = cur
    #     prev = cur
    #     cur = cur.next
    #     prev.next = riff

    #     if cur.next is self.pile.tail:
    #         cur.next = riff
    #     if riff.next is self.pile.tail:
    #         riff.next = cur

    #     # if cur is not self.pile.tail:
    #     #     riff.next = cur
    #     return self.pile

    def debottomup(self):
        percent = self.bottomup_percentage
        n_percent = float(self.pile.size*(1-(percent/100)))

        n_percent = int(n_percent+1) if n_percent - \
            int(n_percent) > 0 else int(n_percent)

        old_tail_node = self.pile.tail.prev
        old_head_node = self.pile.head.next
        # traverse to the broken node
        last_node = self.pile.node_at(n_percent-1)
        self.pile.head.next = last_node.next  # Set new head
        last_node.next = self.pile.tail  # Set new tail
        old_tail_node.next = old_head_node  # linked old tail to old head
        self.pile.tail.prev = last_node

        return self.pile

    def deriffle(self):
        percent = self.riffleshuffle_percentage
        max_swap_index = int(self.pile.size*percent/100)
        # no ceiling
        # Ceiling
        # max_swap_index = int(max_swap_index+1) if max_swap_index-int(max_swap_index) > 0 else int(max_swap_index)

        swap_laps = self.pile.size-self.pile.size*percent/100
        # Ceiling
        swap_laps = int(swap_laps+1) if swap_laps - \
            int(swap_laps) > 0 else int(swap_laps)

        i = 1
        for _ in range(swap_laps):
            self.to_tail(i)
            if i < max_swap_index:
                i += 1

    def to_tail(self, index):
        cur = self.pile.node_at(index-1)
        node_to_be_moved = cur.next
        cur.next = node_to_be_moved.next  # patch
        node_to_be_moved.next = self.pile.tail  # point to tail
        self.pile.tail.prev.next = node_to_be_moved  # set next
        self.pile.tail.prev = node_to_be_moved  # dummyTail approve

    def __str__(self):
        return " ".join(str(x) for x in self.pile)

    def __len__(self):
        return self.pile.size

    def __iter__(self):
        for data in self.pile:
            yield data


if __name__ == "__main__":

    inp1, inp2 = input('Enter Input : ').split('/')
    print('-' * 50)
    h = createLL(int(x) for x in inp1.split())
    for instance_of_scramble in inp2.split('|'):
        print(f"Start : {printLL(h)}")
        k = instance_of_scramble.split(',')
        if k[0][0] == "B" and k[1][0] == "R":
            scarmble(h, float(k[0][2:]), float(k[1][2:]))
        elif k[0][0] == "R" and k[1][0] == "B":
            scarmble(h, float(k[1][2:]), float(k[0][2:]))
        print('-' * 50)
