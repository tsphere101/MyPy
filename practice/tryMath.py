import math

def factorial(number):
    if(number < 1):
        return
    if(number <= 1):
        return 1
    return number*factorial(number-1)


def exponential(base_number, power_number):
    if power_number == 0:
        return base_number
    elif(power_number >= 1):
        result = 1
        for i in range(power_number):
            result *= base_number
        return result

    elif (power_number <= -1):
        result = 1.0
        for i in range(-power_number):
            result = result/base_number
        return result
    return


print(exponential(2, 10))
print(exponential(2, -1))
print(exponential(2,0)) 
print(exponential(4,0.5)) # This case is not being written
print(exponential(4,-0.5)) # This case is not being written

print(math.pow(4,-0.5))
