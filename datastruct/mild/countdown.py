def count_ones(list_, num):
    result = 0
    for d in list_:
        if num == d:
            result += 1
    return result


if __name__ == '__main__':
    prompt = "Enter List : "
    data = [int(x) for x in input(prompt).split()]
    data.sort()
    print(data)

    groups_amount = count_ones(data,1)

    list_of_result = []
    for i in range(groups_amount):
        list_of_result.append(list())

    for i in range(len(list_of_result)):
        for j in range(len(data)):
            if list_of_result[i] == []:
                list_of_result[i].append(data[j])
            elif data[j] == list_of_result[i][-1] +1 :
                list_of_result[i].append(data[j])

        for k in range(len(list_of_result[i])):
            data.pop(data.index(list_of_result[i][k]))

        list_of_result[i].reverse()

    list_of_result.insert(0,len(list_of_result))

    print(list_of_result)
