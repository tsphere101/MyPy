def bubble(data):

    result = {"data": [], "passes": 0, "swaps": 0}
    sorted = False

    while not sorted:
        sorted = True
        result["passes"] += 1
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                sorted = False
                result["swaps"] += 1

    result["data"] = data

    return result


if __name__ == "__main__":

    input()
    data = [x for x in map(int, input().split())]
    result = bubble(data)
    print(f"{result['passes']} {result['swaps']}")
