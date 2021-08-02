
inp = int(input())

result = 1
for i in range(inp, 0, -1):
    if i == 1:
        print(1, end="")
    else:
        print("{}x".format(i), end="")
        result *= i

print(" =", str(result))
