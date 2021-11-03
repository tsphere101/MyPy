
# GCD
def gcd(x, y):
    x = abs(x)
    y = abs(y)
    # if x <= 1:
    #     return y
    # if y <= 1:
    #     return x
    if y == 0:
        return x
    if x == 0:
        return y

    if y > x:
        x, y = y, x
        # x must be greather than y

    r = x % y

    return gcd(y, r)


if __name__ == "__main__":

    inp = input("Enter Input : ")

    x, y = map(int, inp.split())
    if x == 0 and y == 0:
        print("Error! must be not all zero.")
        exit()

    if x*y < 0:
        a = max(x, y)
        b = min(x, y)
    elif x*y > 0:
        a = max(abs(x), abs(y))
        b = min(abs(x), abs(y))
        if x < 0:
            a = -a
            b = -b
    else:
        # case of 0
        a = max(x, y)
        b = min(x, y)

    print(f"The gcd of {a} and {b} is :", gcd(x, y))
