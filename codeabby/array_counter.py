def count(list_of_num, num):
    count = 0
    for d in list_of_num:
        if d == num:
            count += 1

    return count


if __name__ == "__main__":


    amount, range_of_num = [int(x) for x in input().split()]

    data = [int(x) for x in input().split()]

    result = []

    for i in range(range_of_num):
        result.append(count(data, i+1))

    print(" ".join([str(x) for x in result]))
