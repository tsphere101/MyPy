
def avg(data):
    data.pop(-1)
    sum = 0
    for d in data:
        sum += d

    result = sum/len(data)
    return round(result)


if __name__ == '__main__':

    result = []

    for _ in range(int(input())):

        data = [int(x) for x in input().split()]

        result.append(avg(data))

    print(" ".join([str(x) for x in result]))
