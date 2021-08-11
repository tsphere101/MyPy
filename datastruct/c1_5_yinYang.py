
def yin_yang(n):
    _top = n*2 + 4
    for row in range(_top):
        for col in range(_top):

            # Edge of .
            if row+col < (_top/2)-1:
                print(".", end="")
            elif row + col >= int(_top*1.5):
                print(".", end="")

            # Drawing the +
            elif row == 0 and col >= _top/2:
                # Top right
                print("+", end="")
            elif col == _top/2:
                # Mid vertical bone
                print("+", end="")
            elif col == _top-1 and row <= _top/2:
                # Right frame
                print("+", end="")
            elif row >= _top/2-1 and col > _top/2 - 1:
                # Right triangle frame
                print("+", end="")
            elif row > _top/2 and col < _top/2 - 1 and col != 0 and row != _top-1:
                # Bottom left square
                print("+", end="")

            # Background
            else:
                print("#", end="")
        print()
    return


if __name__ == '__main__':
    valid = False
    while not valid:
        try:
            n = int(input("Enter Input : "))
            if n < 1:
                raise ValueError
            valid = True
        except Exception as e:
            pass
    yin_yang(n)
