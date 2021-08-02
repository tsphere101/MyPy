def intercept(data) :
    x1,y1,x2,y2 = data

    result = []

    a = (y2-y1)/(x2-x1)
    b = y1-(a*x1)

    result.append(round(a))
    result.append(round(b))

    return result

def print_data(data) :

    print(f"({data[0]} {data[1]}) ",end = "")

if __name__ == "__main__":

    result = []
    for _ in range(int(input())) :

        data = [int(x) for x in input().split()]

        result.append(intercept(data))

    for d in result:
        print_data(d)
