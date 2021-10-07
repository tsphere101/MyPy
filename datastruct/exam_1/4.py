
def rotate_a(s):
    result = s[-1]
    result += s[:-1]
    return result

def rotate_b(s):
    result = s[1:]
    result += s[0]
    return result

print("*** String Rotation ***")

msg = input("Enter 2 strings : ").split()
A,B = msg

counter = 0
accum = []

a = rotate_a(A)
b = rotate_b(B)
counter +=1
print("1",a,b)
accum.append(a + " " + b)

while(a != A or b != B):
    a = rotate_a(a)
    b = rotate_b(b)
    accum.append(a + " " + b)
    counter += 1

    if counter <= 5:
        print(counter,a,b)
    
if counter > 5:
    if counter > 6:
        print(" . . . . .")
    print(counter,accum[-1])

print("Total of ",counter,"rounds.")