
def median(data) :

    for d in data :
        if d is not min(data) and d is not max(data) :
            return d


if __name__ == "__main__":

    result = []    
    for i in range(int(input())) :
        result.append(median([int(x) for x in input().split()]))

    print(" ".join([str(x) for x in result]))
