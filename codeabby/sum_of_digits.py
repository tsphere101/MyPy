import math


def sum_of_dig(list_):
    sum = list_[0] * list_[1] + list_[2]
    sum_of_dig = 0
    while(sum >= 1):
        sum_of_dig += sum % 10
        sum = math.floor(sum/10)

    return sum_of_dig


if __name__ == '__main__':

    result = []

    for i in range(int(input())):
        data = [int(x) for x in input().split()]
        result.append(sum_of_dig(data))

    print(" ".join([str(x) for x in result]))
