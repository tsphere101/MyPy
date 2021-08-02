import math

number_of_data = int(input())

result = []
for i in range(number_of_data) :
    a,b = [float(x) for x in input().split()]
    if (a/b*10)%10 == 5 :
        result.append(math.ceil(a/b))
    else :
        result.append(round(a/b))


result = [str(x) for x in result]

print(" ".join(result))