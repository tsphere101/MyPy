def find_max(data):
    m = data[0]
    if len(data) == 0 :
        return m

    for d in data:
        if d < m:
            m = d

    return m

def sort_ignore_negatives(data):
    positives = [x for x in data if x >= 0]
    for i in range(len(data)):
        if data[i] >= 0:
            data[i] = positives.pop(positives.index(find_max(positives)))

    return data


if __name__ == "__main__":
    data = [int(x) for x in input("Enter Input : ").split()]

    print(" ".join(str(x) for x in sort_ignore_negatives(data)))