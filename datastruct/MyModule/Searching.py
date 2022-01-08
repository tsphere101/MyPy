def binary_search_product(arr, x, low=None, high=None):
    if not low:
        low = 0

    if not high:
        high = len(arr)-1

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_product(arr, low, mid - 1, x)
        else:
            return binary_search_product(arr, mid + 1, high, x)

    # Base case
    else:
        return -1


class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.id) + '-' + str(self.name)

class ProductTree:
    def __init__(self) :
        self.data_container = 
    
    def get(self,**kwargs):
        
        


def get(products, id):
    # search for that specified id



    binary_search_product(products,id)


if __name__ == "__main__":

    xs = []

    for i in range(100):
        xs.append(Product(i, str(i) + '-item'))

    for data in xs:
        print(data)
