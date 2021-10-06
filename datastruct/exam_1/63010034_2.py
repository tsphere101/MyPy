print(" *** Divisible number ***")

inp = input("Enter a positive number : ")

try:
    num = int(inp)
except:
    print(inp,"is OUT of range !!!")
    exit()

if num <= 0 :
    print(num,"is OUT of range !!!")
    exit()

result = []
for i in range(1,num+1):
    if num % i == 0:
        result.append(i)

print("Output ==> " + " ".join([str(x) for x in result]))

print("Total ==>",len(result))