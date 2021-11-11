
def insertion_sort_recur(data, n=None):
    if len(data) <= 1:
        return data

    if n is None:
        return insertion_sort_recur(data, len(data))

    if n <= 1:
        return data

    result = insertion_sort_recur(data, n-1)
    index_to_insert = find_index_to_insert(data, data[n-1], n-1)
    result.insert(index_to_insert, result.pop(result.index(data[n-1])))

    print(
        f"insert {result[index_to_insert]} at index {index_to_insert}", end=' : ')
    print(result[:n], end=" ")
    if len(data[n:]) != 0:
        print(data[n:])

    return result


def find_index_to_insert(data, x, n=None):
    if n is None:
        n = len(data)-1

    if n < 0:
        return 0

    if data[n-1] < x:
        return n
    else:
        return find_index_to_insert(data, x, n-1)


if __name__ == "__main__":
    inp = [int(x) for x in input("Enter Input : ").split()]

    inp = insertion_sort_recur(inp)
    print()
    print("sorted")
    print(inp)
