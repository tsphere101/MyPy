print("*** multiplication or sum ***")
num1, num2 = map(int, input("Enter num1 num2 : ").split())
mul = num1*num2
if mul > 1000:
    result = num1+num2
else:
    result = mul
print(f"The result is {result}")
