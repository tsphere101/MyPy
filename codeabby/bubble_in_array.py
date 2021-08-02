def bubble_sort_once(data):
    result = {'swap': 0, 'data': []}
    leng = len(data)
    for j in range(leng-1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            result['swap'] += 1
    result['data'] = data
    return result


def checksum(list_of_num):
    SEED = 113
    LIMIT = 10000007
    result = 0
    for i in range(len(list_of_num)):
        result = ((result+list_of_num[i]) * SEED) % LIMIT
    return result


if __name__ == "__main__":
    data = [int(x) for x in input().split()]
    data.pop()
    result = bubble_sort_once(data)
    print(f"{result['swap']} {checksum(result['data'])}")
