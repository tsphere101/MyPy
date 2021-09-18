def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def arrange(a,b):
    a_ = abs(a)
    b_ = abs(b)
    if a == 0 and abs(b) - b > 0:
        return a,b
    if b == 0 and abs(a) - a > 0:
        return b,a
    if (max(a_,b_) == a_) : return a,b
    else : return b,a

if __name__ == "__main__":
    x,y = input("Enter Input : ").split()
    x,y = int(x),int(y)
    if x == 0 and y == 0 : print("Error! must be not all zero.")
    else:
        result = abs(gcd(x, y))
        x,y = arrange(x,y)
        print(f"The gcd of {x} and {y} is : {result}")