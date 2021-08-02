
def origino_min():
    result = []

    for i in range(int(input())):
        a, b = input().split()
        result.append(min(int(a), int(b)))

    result = [str(i) for i in result]

    print(" ".join(result))


if __name__ == '__main__':

    my_list = [1,2,3,4,5]
    print("\n".join([str(i) for i in my_list]))

    origino_min()
    


# number_of_data = int(input("Enter the amount of data : "))

# result = []
# for i in range(number_of_data):
#     input_data = input("").split()
#     result.append(min(int(input_data[1]), int(input_data[0])))

# print(" ".join(result))
