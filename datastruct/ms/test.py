# def sum(a,b):
#     return a+b
# num1= int(input("num 1 : "))
# num2= int(input("num 2 : "))
# print(sum(num1,num2))
# --------------------------------
# sum = 0
# count = int(input("count : "))
# for i in range(count+1):
#     sum += i
# print(sum)
# --------------------------------
# numlist = []
# count = int(input("count : "))
# for i in range(count):
#     numlist.append(i+1)
#     print(numlist[i],end=" ")
# --------------------------------
# numlist = []
# mul=1
# count = int(input("count : "))
# for i in range(count,0,-1):
#     numlist.append(i)
# --------------------------------
# for i in range(count-1):
#     print(numlist[i],end="x")
#     mul*=numlist[i]
# print("1 = " + str(mul),end="")
# --------------------------------
# haiku = """The old pond,
# A frog jumps in:
# Plop!"""
# print(haiku)
# --------------------------------
# float_1 = 0.25
# float_2 = 40.0
# product = int(float_1*float_2)
# print("The product was",product)
# print("The product was " + str(product))
# print("{:.2f} was the product".format(product))
# print("{num:} was the product".format(num=int(float_1*float_2)))
# print("{:,} was the product".format(10000)) #Use a comma as a thousand separator
# print("{:b} was the product".format(10))    #Binary format
# print("{:o} was the product".format(10))    #Octal format
# print("{:x} was the product".format(10))    #Hex format, lower case
# print("{:e} was the product".format(10))    #Scientific format, with an lower case e
# --------------------------------
# fifth_letter = "World"[4]
# print(fifth_letter)
# --------------------------------
# string_1 = "Camelot"
# string_2 = "place"
# print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# --------------------------------Sum in Loop#1-----------------------------------
# sum = 0
# count = int(input("count : "))
# for i in range(count):
#     sum += int(input())
# print(sum)

# sum = 0
# count = int(input("count : "))
# numstrlist = input().split()
# for i in range(count):
#     sum += int(numstrlist[i])
# print(sum)

# --------------------------------Sum in Loop#2-----------------------------------
# sum = 0
# sumlist = []
# count = int(input("List count : "))
# for i in range(count):
#     numstrlist = input().split()
#     for j in range(2):
#         sum += int(numstrlist[j])
#     sumlist.append(sum)
#     sum = 0
# for num in sumlist:
#     print(num, end=" ")

# --------------------------------Minimum of Two-----------------------------------
# minlist = []
# count = int(input("List count : "))
# for i in range(count):
#     numstrlist = input().split()
#     if int(numstrlist[0]) < int(numstrlist[1]):
#         minnum = int(numstrlist[0])
#     else:
#         minnum = int(numstrlist[1])
#     minlist.append(minnum)
#     numstrlist.clear()
# for num in minlist:
#     print(num, end=" ")

# --------------------------------Minimum of Three-----------------------------------
# minlist = []
# numlist = []
# count = int(input("List count : "))
# for i in range(count):
#     numstrlist = input().split()
#     for j in range(3):
#         numlist.append(int(numstrlist[j]))
#     minlist.append(min(numlist))
#     numlist.clear()
#     numstrlist.clear()
# for num in minlist:
#     print(num, end=" ")

# --------------------------------Maximum of array-----------------------------------
# numlist = []
# numstrlist = input().split()
# for num in numstrlist:
#     numlist.append(int(num))
# print(max(numlist), min(numlist))

# --------------------------------Rounding-----------------------------------
# import math

# roundlist = []
# numlist = []
# count = int(input("List count : "))
# for i in range(count):
#     numstrlist = input().split()
#     for j in range(2):
#         numlist.append(float(numstrlist[j]))
#     div = numlist[0]/numlist[1]
#     if (div % 1) == 0.5:
#         if div >= 0:
#             div = math.ceil(div)
#         else:
#             div = math.floor(div)
#     else:
#         div = round(div)
#     roundlist.append(div)
#     numlist.clear()
#     numstrlist.clear()
# for num in roundlist:
#     print(num, end=" ")

# --------------------------------Fahrenheit to Celsius-----------------------------------
# import math

# roundlist = []
# numlist = []
# count = int(input("Amount of data : "))
# numstrlist = input().split()
# for i in range(count):
#     faren = float(numstrlist[i])
#     celsius = float(((faren-32)*5)/9)
#     if (celsius % 1) == 0.5:
#         if celsius >= 0:
#             celsius = math.ceil(celsius)
#         else:
#             celsius = math.floor(celsius)
#     print(round(celsius), end=" ")

# --------------------------------Vowel Count-----------------------------------
# vowel = "aeiouy"
# count = 0
# vowelcountlist = []
# amount = int(input("Amount of data : "))
# for i in range(amount):
#     words = input()
#     words = words.lower()
#     for vw in vowel:
#         count += words.count(vw)
#     vowelcountlist.append(count)
#     count = 0

# for i in vowelcountlist:
#     print(i, end=" ")

# --------------------------------Sum of digits-----------------------------------
# sumlist = []
# sum = 0
# count = int(input("Amount of data : "))
# for i in range(count):
#     numstrlist = input().split()
#     multi = int(numstrlist[0])*int(numstrlist[1])+int(numstrlist[2])
#     for num in str(multi):
#         sum += int(num)
#     sumlist.append(sum)
#     sum = 0
# for num in sumlist:
#     print(num, end=" ")

# --------------------------------Arithmetic Progression-----------------------------------
# sumlist = []
# sum = 0
# amount = int(input("Amount of data : "))
# for i in range(amount):
#     numstrlist = input().split()
#     for count in range(int(numstrlist[2])):
#         sum += int(numstrlist[0]) + (count*int(numstrlist[1]))
#     sumlist.append(sum)
#     sum = 0
# for num in sumlist:
#     print(num, end=" ")

# --------------------------------Median of Three-----------------------------------
# 1
# import statistics

# medlist = []
# numlist = []
# amount = int(input("Amount of data : "))
# for i in range(amount):
#     numstrlist = input().split()
#     for j in range(3):
#         numlist.append(int(numstrlist[j]))
#     medlist.append(statistics.median(numlist))
#     numlist.clear()
#     numstrlist.clear()
# for num in medlist:
#     print(num, end=" ")

# 2
# medlist = []
# numlist = []
# amount = int(input("Amount of data : "))
# for am in range(amount):
#     numlist = list(map(int, input().split()))
#     numlist.sort()
#     medlist.append(numlist[1])
#     numlist.clear()
# for num in medlist:
#     print(num, end=" ")

# 3
# def findMed(numlist):
#     numlist.sort()
#     if len(numlist) % 2:
#         num = numlist[int((len(numlist)-1)/2)]
#     else:
#         num = (numlist[int(len(numlist)/2)] + numlist[(int(len(numlist)/2)-1)])/2
#     return num

# print("Number : ", end="")
# numlist = list(map(int, input().split()))
# print("Median :", findMed(numlist))

# ----------------------------convert decimal to binary---------------------------------
# import math
# num = int(input())
# binary = []
# print("{:b}".format(num))
# print(f"{num:b}")
# while num > 0:
#     binary.insert(0, num % 2)
#     num /= 2
#     num = math.floor(num)
# for bit in binary:
#     print(bit, end="")

# --------------------------------Triangles-----------------------------------
# anslist = []
# numlist = []
# amount = int(input("Amount of data : "))
# for am in range(amount):
#     numlist = list(map(int, input().split()))
#     side1 = (numlist[0]+numlist[1])-numlist[2]
#     side2 = (numlist[0]+numlist[2])-numlist[1]
#     side3 = (numlist[1]+numlist[2])-numlist[0]
#     if side1 > 0 and side2 > 0 and side3 > 0:
#         anslist.append(1)
#     else:
#         anslist.append(0)

# for num in anslist:
#     print(num, end=" ")

# --------------------------------Body Mass Index-----------------------------------
# anslist = []
# amount = int(input("Amount of data : "))
# for am in range(amount):
#     datalist = list(map(float, input().split()))
#     BMI = float(datalist[0]/(datalist[1]*datalist[1]))
#     if BMI < 18.5:
#         anslist.append("under")
#     elif BMI < 25.0:
#         anslist.append("normal")
#     elif BMI < 30.0:
#         anslist.append("over")
#     else:
#         anslist.append("obese")

# for ans in anslist:
#     print(ans, end=" ")

# --------------------------------Average of an array-----------------------------------
# anslist = []
# sum = 0
# amount = int(input("Amount of data : "))
# for am in range(amount):
#     numlist = list(map(int, input().split()))
#     for num in numlist:
#         sum += num
#     ans = sum/(len(numlist)-1)
#     if ans % 1 == 0.5:
#         if ans >= 0:
#             ans += 0.5
#         else:
#             ans -= 0.5
#     anslist.append(round(ans))
#     sum = 0

# for ans in anslist:
#     print(ans, end=" ")

# --------------------------------Dice Rolling-----------------------------------
# anslist = []
# amount = int(input("Amount of data : "))
# for am in range(amount):
#     num = float(input())
#     num = int(num*6)+1
#     anslist.append(num)

# for ans in anslist:
#     print(ans, end=" ")

# --------------------------------Reverse String-----------------------------------
# print(input()[::-1])

# --------------------------------Array Counters-----------------------------------
# count = 0
# numlist = []
# amount = int(input("Amount of data : "))
# rangenum = int(input("Range of data : "))
# allnum = list(map(int, input().split()))
# for num in range(rangenum):
#     numlist.append(num+1)
# for num in numlist:
#     for num2 in allnum:
#         if num == num2:
#             count += 1
#     for c in range(count):
#         allnum.remove(num)
#     print(count, end=" ")
#     count = 0

# --------------------------------test case-----------------------------------
# n=int(input())
# col,row=4*(n-1)+1,4*(n-1)+1
# for r in range(1,row+1):
#     for c in range(1,col+1):
#         if r==1 or r==row or c==1 or c==col:
#             print("#",end="")
#         elif r%2==1 and c-r>=0 and c+r<=row+1:
#             print("#",end="")
#         elif r%2==1 and r-c>=0 and r+c>=row+1:
#             print("#",end="")
#         elif c%2==1 and r-c>=0 and r+c<=row+1:
#             print("#",end="")
#         elif c%2==1 and c-r>=0 and c+r>=row+1:
#             print("#",end="")
#         else:
#             print(".",end="")
#     print("")

# --------------------------------yin yang-----------------------------------
# while True:
#     try:
#         n = int(input())
#         if type(n) == int and n > 0:
#             break
#     except ValueError as e:
#         print("Enter number pls")
#         pass
# col, row = 2*n+4, 2*n+4
# for r in range(1, row+1):
#     for c in range(1, col+1):
#         if r+c <= row/2 or r+c >= 2*row-n:
#             print(".", end="")
#         elif c == row/2 or (r >= row/2 and c == 1) or (r+c >= n+3 and c <= row/2 and r <= row/2+1) or (r == row and c <= row/2) or (r >= 2 and r <= n+1 and c <= row-1 and c >= row/2+2):
#             print("#", end="")
#         else:
#             print("+", end="")
#     print("")

# ----------------------- Comprehension List -----------------

# liar_=[1,2,3,4,5]
# liar_2 = [x for x in liar_]
# liar_3 = liar_.copy()
# print(liar_)
