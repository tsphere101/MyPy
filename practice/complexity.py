n = int(input("Enter input amount : "))

data = [i for i in range(1,n+1)]




# O of 1 Constant Order
def o1():
    print(data) # 1 Operation done

# O of n Linear Order
def on():
    for x in data:
        print(x) # n operation done

# O of n^2 Quadratic Order
def on2():
    for x in data:
        for y in data:
            print(x,y) # n*n operation done

# O of logn Logarithmic Order
def ologn():
    i = len(data)-1
    while(i > 0):
        print(data[i])
        i = int(i/2)
    
# O of nlogn Linearithmic Order
def onlogn():
    i = len(data)-1
    while(i > 0):
        x = len(data)-1
        while(x > 0):
            print(data[x])
            x = int(x/2)
        i-=1