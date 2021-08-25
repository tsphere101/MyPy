class Stack:

    def __init__(self, *args):
        self.length = 0
        self.stack_data = []
        for data in args:
            self.stack_data.append(data)
            self.length += 1

    def push(self, *args):
        for data in args:
            self.stack_data.append(data)
            self.length += 1

    def pop(self, *indices):
        if len(indices) == 0:
            self.length -=1
            return self.stack_data.pop()
        else :
            indices = list(indices)
            indices.sort(reverse=True)
            poped = []
            for data in indices:
                poped.append(self.stack_data.pop(data))
                self.length -=1
            return tuple(poped)

    def top(self):
        return self[-1]

    def copy(self):
        copy_of_self = Stack()
        for data in self:
            copy_of_self.push(data)
        return copy_of_self

    def __iter__(self):
        for data in self.stack_data:
            yield data 

    def __getitem__(self,index):
        return self.stack_data[index]

    def __setitem__(self,index,data):
        self.stack_data[index] = data

    def __eq__(self, o: object) -> bool:
        if len(o) != len(self): return False
        for i,data in enumerate(o):
            if self[i] != data: return False
        return True

    def __str__(self):
        return str(self.stack_data)

    def __len__(self):
        return self.length
                
        
if __name__ == '__main__':
    x = Stack(10,20,30,40,50)    
    x.push(1,2,3,4,5,99)
    print(x)





