def bubble_sort(data, n=None, k=None, flag=None):
    if len(data) <= 1:
        return data

    if k is None:
        flag = True
        k = 0
    if n is None:
        n = 0
    if flag is None:
        flag = False

    if k == len(data):
        return data
    if n == len(data)-1:
        if flag is True:
            return data
        return bubble_sort(data, 0, k+1, flag)

    if data[n] > data[n+1]:
        data[n], data[n+1] = data[n+1], data[n]  # Perform a swap
        flag = False

    return bubble_sort(data, n+1, k, flag)


if __name__ == "__main__":
    inp = [int(x) for x in input("Enter Input : ").split()]

    print(bubble_sort(inp))
