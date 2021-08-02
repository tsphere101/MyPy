import math


def roll_dice(value):
    face = math.floor(value * 6) + 1
    return face


if __name__ == "__main__":

    result = []

    for _ in range(int(input())):

        result.append(roll_dice(float(input())))

    print(" ".join([str(x) for x in result]))
