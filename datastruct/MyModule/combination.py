def combination(L,n):
    if n == 1:
        return [ [x] for x in L]
    if len(L) == n:
        return [L]
    
    sub = combination(L[1:],n)
    f = L[0]
    result = [[f,L[x]] for x in range(1,len(L))] + sub
    return result

def power_set(L) :
    if len(L) == 0:
        return [[]]
    else:
        base = power_set(L[:-1])
        operator = L[-1:]
        return base + [(b + operator) for b in base]
