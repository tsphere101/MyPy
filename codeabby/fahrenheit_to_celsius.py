
def convert_to_cel(fah) :

    result = (fah-32)/1.8

    return result

if __name__ == '__main__':

    number_of_data = int(input())

    data = [float(x) for x in input().split()]

    result = [round(convert_to_cel(x)) for x in data]

    print(" ".join([str(x) for x in result]))