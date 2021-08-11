
print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
width = 4*n-3
for i in range(width):
    for j in range(width):
        if i == 0 or i == width-1:
            print("#", end="")
        elif i+j <= width-1 and j % 2 == 0 and j <= i or j % 2 == 0 and j >= i and i+j > width-1:
            print("#", end="")
        elif i+j < width and i % 2 == 0 and j >= i :
            print("#", end="")
        elif i+j > width-2 and j <= i and i > (int(width/2))+1 and i % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print("")
