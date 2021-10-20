def calculate(li):
    if len(li) != 1:
        s, b = calculate(li[1:])
    else:
        s = 1
        b = 0
    n1, n2 = li[0].split()
    s *= int(n1)
    b += int(n2)
    return s, b

def findMindDiffNew(l):
    if len(l) == 1:
        d1, d2 = calculate(l[0])
        return abs(d1-d2)
    else:
        x = findMindDiffNew(l[1:])
    y1, y2 = calculate(l[0])
    d = abs(y1-y2)
    return min(d, x)

def powerSet(l):
    if l == []:
        return [[]]
    a = powerSet(l[1:])
    return a + [[l[0]] + b for b in a]

sblist = input("Enter Input : ").split(",")
print(findMindDiffNew(powerSet(sblist)[1:]))
