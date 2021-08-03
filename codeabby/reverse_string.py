
def reverse_me(string):
    result = ""
    length = len(string)
    for i in range(length):
        result += (string[(length - i - 1)])

    return result


def reverse_me2(string):
    return string[-1::-1]


if __name__ == '__main__':

    print(reverse_me2(input()))
    # print(reverse_me(input()))