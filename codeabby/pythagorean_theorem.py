def triangle_type(sides_length):
    short_side = sides_length.pop(sides_length.index(min(sides_length)))
    long_side = sides_length.pop(sides_length.index(max(sides_length)))
    med_side = sides_length[0]

    sid = short_side**2 + med_side**2

    if sid == long_side**2 :
        return "R"
    elif sid < long_side**2 :
        return "O"
    else :
        return "A"

import math

if __name__ == "__main__":

    result = []
    for _ in range(int(input())) :
        sides_length = [float(x) for x in input().split()]
        result.append(triangle_type(sides_length)) 

    print(" ".join([str(x) for x in result]))