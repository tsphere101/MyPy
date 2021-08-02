def solv(data):
    result = 0
    init = data[0]
    step = data[1]
    loop = data[2]

    for i in range(loop):
        result += init + (step*i)

    return result


if __name__ == "__main__":
    number_of_data = int(input())
    result = []
    for i in range(number_of_data):

        data = [int(x) for x in input().split()]

        result.append(solv(data))

    print(" ".join([str(x) for x in result]))