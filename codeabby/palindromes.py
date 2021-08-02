def check_palin(data):

    data = data.lower()

    leng = len(data)

    for i in range(1 + round(leng/2)):

        if data[i] != data[leng-i-1]:

            print(data[i], " and ", data[leng-i-1], " is not the same")

            return "N"

        return "Y"


if __name__ == "__main__":

    result = []

    for _ in range(int(input())):

        data = input()

        result.append(check_palin(data))

    print(" ".join([x for x in result]))

