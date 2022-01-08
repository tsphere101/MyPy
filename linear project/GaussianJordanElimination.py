import math


class Matrix():

    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.size = len(matrix)

    def gauss_elemination(self):
        # r1/r11
        result = self.matrix[:]
        v = result[0][0]
        for i in range(self.size):
            result[0],[]
        
        
        

        pass

    def __str__(self):
        output = ''
        for i in range(self.size):
            output += ' '.join(str(x) for x in self.matrix[i]) + '\n'

        return output


if __name__ == "__main__":

    data = input("Enter N x N matrix / size : ").split()

    size = int(data.pop())

    data = [x for x in map(int, data)]

    m = []
    k = 0
    for i in range(size):
        mn = []
        for j in range(size):
            mn.append(data[k])
            k += 1
        m.append(mn)

    print(m)

    mtx = Matrix(m)
    print(mtx)
