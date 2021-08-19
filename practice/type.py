def sum(*args):
    print(type(args))
    result = 0
    for d in args:
        result += d
    return result

def foo(*kwargs):
    print(type(kwargs))

foo(name = "Krissada", id = 1234)
print(sum(1,2,3,4,5,6,7,8,9))