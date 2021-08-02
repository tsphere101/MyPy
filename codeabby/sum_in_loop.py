number_of_data = int(round(float(input("Enter the number of data : "))))

data = []
result = []
for i in range(number_of_data) :
    sub_data = input().split()
    accum = 0
    for i in range(2) :
        accum += int(sub_data[i])
    result.append(accum)

for x in result:
    print(x,end=" ")