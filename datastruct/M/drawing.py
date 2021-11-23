print("*** Fun with Drawing ***")
while True:
    try :
        n = int(input("Enter input : "))
        if n < 2:
            raise ValueError
    except ValueError:
        pass
    else:
        break
col,row=4*(n-1)+1,4*(n-1)+1
for r in range(1,row+1):
    for c in range(1,col+1):
        if r==1 or r==row or c==1 or c==col:
            print("#",end="")
        elif r%2==1 and c-r>=0 and c+r<=row+1:
            print("#",end="")
        elif r%2==1 and r-c>=0 and r+c>=row+1:
            print("#",end="")
        elif c%2==1 and r-c>=0 and r+c<=row+1:
            print("#",end="")
        elif c%2==1 and c-r>=0 and c+r>=row+1:
            print("#",end="")
        else:
            print(".",end="")
    print("")