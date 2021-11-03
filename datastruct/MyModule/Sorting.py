
class BubbleSort:
    def sort(data):
        for i in range(len(data)):
            flag_unfinished = True
            if flag_unfinished:
                for j in range(len(data)-1):
                    flag_unfinished = False
                    if data[j] > data[j+1]:
                        data[j], data[j+1] = data[j+1], data[j]
                        flag_unfinished = True
            else:
                break
        return data


class StraightSelectionSort:
    def max(a, b=None):
        try:
            result = a[0]
            for d in a:
                if d > result:
                    result = d
            return result
        except TypeError:
            return a if a > b else b

    def min(a, b=None):
        try:
            result = a[0]
            for d in a:
                if d < result:
                    result = d
            return result
        except TypeError:
            return a if a < b else b

    def sort(data):
        data = list(data)
        result = []

        while len(data) != 0:
            element = min(data)
            data.pop(data.index(element))
            result.append(element)

        return result


class InsertionSort:
    def sort(data):
        for i in range(len(data)):
            element = data[i]

            for j in range(i, -1, -1):
                if element < data[j-1] and j > 0:
                    data[j] = data[j-1]  # Shift right
                else:
                    data[j] = element
                    break

        return data


class QuickSort:
    def sort(data):
        if len(data) == 1:
            return data
        elif len(data) == 2:
            if data[0] < data[1]:
                return data
            else:
                data[0], data[1] = data[1], data[0]
                return data

        pivot = data[int(len(data)/2)]

        left_partition = []
        middle_partition = []
        right_partition = []

        for d in data:
            if d < pivot:
                left_partition.append(d)
            elif d > pivot:
                right_partition.append(d)
            else:
                middle_partition.append(d)

        return QuickSort.sort(left_partition) + middle_partition + QuickSort.sort(right_partition)


class BinarySearchTreeSort:
    class Node:
        def __init__(self, data):
            self.data = [data]
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)

        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data[0]:
            if node.left:
                node.left = self._insert(data, node.left)
                return node
            else:
                node.left = self.Node(data)
                return node
        elif data > node.data[0]:
            if node.right:
                node.right = self._insert(data, node.right)
                return node
            else:
                node.right = self.Node(data)
                return node
        else:
            # Equal case
            node.data.append(data)
            return node

    def in_order_traversal(self, node=None):
        if node is None:
            node = self.root

        elements = []
        if node.left:
            elements += self.in_order_traversal(node.left)

        elements += node.data

        if node.right:
            elements += self.in_order_traversal(node.right)

        return elements

    def sort(data):
        tree = BinarySearchTreeSort()
        for d in data:
            tree.insert(d)

        return tree.in_order_traversal()

import random
import time

if __name__ == "__main__":
    data = [6, 5, 4, 3, 2, 1, 0]
    # data = [1,2,2,3,3,4,4,5,5]

    data = [random.randint(0,999) for _ in range(50000)]

    t1 = time.time()
    data = BinarySearchTreeSort.sort(data)
    t2 = time.time()

    print(t1-t2)
    # print(data)
