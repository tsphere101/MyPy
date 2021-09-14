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


if __name__ == "__main__":
    # Enter Input : 0:0 2:0,1:3 3:3,2:1 2:1
    # My   Queue = 0:0, 1:3, 2:1
    # Your Queue = 2:0, 3:3, 2:1
    # My   Activity:Location = Eat:Res., Game:Home, Learn:ClassR.
    # Your Activity:Location = Learn:Res., Movie:Home, Learn:ClassR.
    # Yes! You're my love! : Score is 8.
    days = input("Enter Input : ").split(",")
    
    my_queue = Queue()
    your_queue = Queue()
    activity_dict = {"0":"Eat","1":"Game","2":"Learn","3":"Movie"}
    location_dict = {"0":"Res.","1":"ClassR.","2":"SuperM.","3":"Home"}
    score_lookup = {"7+":"Yes! You're my love!","7-":"Umm.. It's complicated relationship!","0":"No! We're just friends."}
    score = 0

    for day in days:
        # activity
        me= day.split(" ")[0]
        my_activity = me.split(":")[0]
        my_location = me.split(":")[1]

        # you
        you = day.split(" ")[1]
        u_activity = you.split(":")[0]
        u_location = you.split(":")[1]

        my_queue.enqueue(me)
        your_queue.enqueue(you)

        if (my_activity == u_activity) and (my_location != u_location):
            score +=1
        elif (my_location == u_location) and (my_activity != u_activity):
            score +=2
        elif (my_activity == u_activity) and (my_location == u_location):
            score +=4
        else :
            score -=5

    print("My   Queue =", ", ".join(day for day in my_queue))
    print("Your Queue =", ", ".join(day for day in your_queue))
    print("My   Activity:Location =", ", ".join(str(activity_dict[day[0]]+":"+location_dict[day[2]]) for day in my_queue )) 
    print("Your Activity:Location =", ", ".join(str(activity_dict[day[0]]+":"+location_dict[day[2]]) for day in your_queue)) 



    if score >=7 :
        print(score_lookup["7+"] + f" : Score is {score}.")
    elif score < 7 and score > 0 :
        print(score_lookup["7-"] + f" : Score is {score}.")
    else : 
        print(score_lookup["0"] + f" : Score is {score}.")
