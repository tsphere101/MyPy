class Stack:
    def __init__(self):
        self.items = [] 
        self.length = 0

    def push(self,data):
        self.items.append(data)
        self.length +=1

    def pop(self):
        self.length -=1
        return self.items.pop()
    
    def isEmpty(self):
        return True if self.size()== 0 else False

    def size(self):
        return self.length

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:
  
    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)