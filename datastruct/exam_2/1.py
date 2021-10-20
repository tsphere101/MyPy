class Stack:

    def __init__(self):
        self.data_list = []

    def push(self, data):
        self.data_list.append(data)

    def pop(self):
        return self.data_list.pop()

    def isEmpty(self):
        return self.data_list == []

    def size(self):
        return len(self.data_list)

    def peek(self):
        return self.data_list[-1]

    def bottom(self):
        return self.data_list[0]

    def __str__(self):
        return "Data in Stack is : " + " ".join(str(data) for data in self.data_list)

if __name__ == "__main__":

    input_num = int(input("Enter choice : "))

    if input_num == 1:
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())

    elif input_num == 2:
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.isEmpty())

    elif input_num == 3:
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())