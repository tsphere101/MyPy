def quicksort(data):
    if len(data) <= 1:
        return data

    left = []
    right = []
    mid = []

    mid_index = len(data)//2
    pivot = data[mid_index]

    for d in data:
        if d < pivot:
            left.append(d)
        elif d > pivot:
            right.append(d)
        else:
            mid.append(d)

    return quicksort(left) + mid + quicksort(right)


def find_first_greater_value(data, x):

    data = quicksort(data)
    for d in data:
        if d > x:
            return d
    raise ValueError("Not exist.")


if __name__ == "__main__":

    data, xs = input("Enter Input : ").split('/')

    data = [int(x) for x in data.split()]
    xs = [int(x) for x in xs.split()]

    for x in xs:
        try:
            print(find_first_greater_value(data, x))
        except:
            print("No First Greater Value")
