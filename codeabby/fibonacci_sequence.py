def fibo_index(num):

    prev = 0
    fi = 0

    if num == 0:
        return 0

    for i in range(1000):
        if i == 0:
            fi += 1

        nextFi = prev+fi
        prev = fi
        fi = nextFi

        if num == fi:
            return i+2

    return -1


if __name__ == "__main__":

    result = []

    for _ in range(int(input())):

        result.append(fibo_index(int(input())))

    print(" ".join([x for x in map(str, result)]))
