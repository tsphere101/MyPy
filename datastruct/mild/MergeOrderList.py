class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    head = node(None)
    cur = head
    for data in l:
        cur.next = node(data)
        cur = cur.next
    return head


def printList(H):
    cur = H
    data = list()
    while cur.next is not None:
        cur = cur.next
        data.append(cur.data)
    print(" ".join(str(x) for x in data))


def size_of_list(H):
    cur = H
    size = 0

    try :
        size = len(H)
        return size
    except:
        pass

    while cur.next is not None:
        cur = cur.next
        size += 1
    return size


def recursive_sort(H):
    if size_of_list(H) <= 1:
        return H

    result = createList([])
    cur = H
    pivot = cur.next.data

    # low, equal, high = [], [], []
    low,equal,high = createList([]),createList(),createList()
    while cur.next is not None:
        cur = cur.next
        d = cur.data
        if d == pivot:
            mergeList(equal, createList([d]))
        elif d > pivot:
            mergeList(high, createList([d]))
        elif d < pivot:
            mergeList(low, createList([d]))

    result = mergeList(mergeList(recursive_sort(low),recursive_sort(equal)),recursive_sort(high))
    # result = recursive_sort(low) + equal + recursive_sort(high)
    return result

def mergeList(p,q):
    cur = p
    while cur.next is not None:
        cur = cur.next
    cur.next = q.next
    return p

def mergeOrderesList(p, q):
    cur = p
    while cur.next is not None:
        cur = cur.next
    cur.next = q.next

    return recursive_sort(p)

    #################### FIX comand ####################
    # input only a number save in L1,L2
if __name__ == '__main__':
    L1, L2 = input("Enter 2 Lists : ").split()
    L1 = [int(x) for x in L1.split(",")]
    L2 = [int(x) for x in L2.split(",")]
    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ', end='')
    printList(LL1)
    print('LL2 : ', end='')
    printList(LL2)
    m = mergeOrderesList(LL1, LL2)
    print('Merge Result : ', end='')
    printList(m)
