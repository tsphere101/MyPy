def quicksort(data):
    if len(data) <= 1:
        return data

    pivot_ind = len(data)//2
    pivot = data[pivot_ind]

    left = []
    mid = []
    right = []
    for d in data:
        if d < pivot:
            left.append(d)
        elif d > pivot:
            right.append(d)
        else:
            mid.append(d)

    return quicksort(left) + mid + quicksort(right)


def sort_dict_by_key(data: dict) -> dict:
    sorted_keys = quicksort([x for x in data.keys()])
    result = {}
    for k in sorted_keys:
        result.update({k: data[k]})
    return result


if __name__ == "__main__":
    data = input("Enter Input : ").split()

    dictionary = {}

    for d in data:
        for c in d:
            if c.isalpha():
                dictionary.update({c: d})

    dictionary = sort_dict_by_key(dictionary)

    for d in dictionary:
        print(dictionary[d], end=' ')
