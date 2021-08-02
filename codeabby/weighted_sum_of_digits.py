def wsd(value) :

    string_of_value = str(value)
    result = 0
    for i in range(len(string_of_value)) :
        result += int(string_of_value[i]) * (i+1)

    return result


if __name__ == '__main__':

    result = []
    number_of_value = input()

    for data in input().split():
        result.append(wsd(int(data)))

    print(" ".join([str(x) for x in result]))
    