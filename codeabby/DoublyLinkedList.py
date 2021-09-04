class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self,data= None):
        self.head = None
        self.tail = None
        self.size = 0

        if data is not None:
            self.append(data)

    def append(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else :
            new_node = Node(data)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.size +=1
        return None


    def node_at(self,index):
        # Traverse to the node at the index
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node


    def get_data(self,index):
        data = self.node_at(index).data
        return data
        

    def pop(self,index=None):
        if index is None:
            self.tail.next = None
            self.size -=1
        else :
            cur = self.node_at(index)
            data = cur.get_data()
            cur.previous.next = cur.next
            cur.next.previous = cur.previous
            self.size -=1
        return data

    def __len__(self):
        return self.size

    def __getitem__(self,index):
        return self.get_data(index)

    def __setitem__(self,index):
        pass

    def __str__(self):
        output = ""
        for d in len(self):
            output += "[" + str(d) + ","
        output += "]"
        return output

    def __iter__(self):
        cur = self.head
        yield cur.data
        while cur.next != None:
            cur = cur.next
            yield cur.data



if __name__ == "__main__":
    a = DoublyLinkedList(1)
    a.append(2)
    a.append(2)
    a.append(2)
    print(a[0])

