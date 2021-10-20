class Queue:
    def __init__(self):
        self.data_list = []

    def enQueue(self, data):
        self.data_list.append(data)

    def deQueue(self):
        return self.data_list.pop(0)

    def isEmpty(self):
        return self.data_list == []

    def __len__(self):
        return len(self.data_list)

    def __str__(self):
        if self.isEmpty():
            return "Empty Queue"
        else :
            return "Queue data : " + " ".join(str(data) for data in self.data_list)


if __name__ == "__main__":

    input_num = int(input("Enter choice : "))

    if input_num == 1:
        q1 = Queue()
        q1.enQueue(10)
        q1.enQueue(20)
        q1.enQueue(30)
        print(q1)
        q1.deQueue()
        q1.enQueue(40)
        print("Size of Queue :", len(q1))
        print(q1)

    elif input_num == 2:
        q1 = Queue()
        q1.enQueue(100)
        q1.enQueue(200)
        q1.enQueue(300)
        q1.deQueue()
        print(q1)
        print("Queue is Empty :",q1.isEmpty())

    elif input_num == 3:
        q1 = Queue()
        q1.enQueue(11)
        q1.enQueue(22)
        q1.enQueue(33)
        q1.deQueue()
        q1.deQueue()
        q1.deQueue()
        print(q1)
        print("Size of Queue :",len(q1))
        print("Queue is Empty :",q1.isEmpty())