
if __name__ == "__main__":
    max_value = int(input().split()[1])
    data = [int(x) for x in input().split()]
    result = [0 for x in range(max_value)]
    print(result)

    for i in range(len(data)):
        try :
            result[data[i]-1] += 1
        except IndexError:
            pass
            
    print(" ".join([str(x) for x in result]))