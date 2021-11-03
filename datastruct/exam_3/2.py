def max_recur(data):

    if len(data) <= 1:
        return data

    if len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]
    

    t = max_recur(data[1:])
    if data[0] > t:
        result = data[0]
    else:
        result = t

    return result


if __name__ == "__main__":
    inp = input("Enter Input : ")

    data = [int(x) for x in inp.split()]

    print("Max :",max_recur(data))