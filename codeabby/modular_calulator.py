
def calculate(initial):
    result = initial
    while True:
        sign, number = input().split()
        number = int(number)
        if sign == "%":
            return result % number
        elif sign == "+":
            result += number
        elif sign == "*":
            result *= number
        else:
            raise Exception("Bad operation")


def short_calculate():
    print(eval("1+2+34"))


if __name__ == "__main__":

    print(calculate(int(input())))
