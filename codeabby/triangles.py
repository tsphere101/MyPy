
def can_be_triangle(data) :
    second_shortest = 0
    for d in data :
        if d is not min(data) and d is not max(data) :
            second_shortest = d

    sum_of_two_shortest = second_shortest + min(data)

    if sum_of_two_shortest > max(data) :
        return 1
    else :
        return 0

if __name__ == '__main__':

    result = []
    for _ in range(int(input())) :
        data = [int(x) for x in input().split()]
        result.append(can_be_triangle(data))

    print(" ".join([str(x) for x in result]))