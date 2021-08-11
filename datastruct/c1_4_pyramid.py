
def pyramid(n):
    _top = 4*(n-1)+1
    for row in range(_top):  # ROW
        for col in range(_top):  # COL
            if row == 0 or row == _top-1:
                print("#", end="")
            elif row % 2 == 0 and col >= row and row+col < _top:
                print("#", end="")
            elif row+col > _top-2 and col <= row and row > (_top // 2)+1 and row % 2 == 0:
                print("#", end="")
            elif col % 2 == 0 and col <= row and row + col <= _top-1:
                print("#", end="")
            elif col % 2 == 0 and col >= row and row+col > _top-1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    return


if __name__ == "__main__":
    print("*** Fun with Drawing ***")
    valid = False
    while not valid:
        try:
            n = int(input("Enter input : "))
            if n < 2:
                raise ValueError
            valid = True
        except Exception as e:
            pass

    pyramid(n)
