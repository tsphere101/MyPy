def selectionsort(data):
    
    result = []
    while len(data) != 0:
        result.append(data.pop(data.index(min(data))))

    return result

def insertionsort(data):

    for i in range(len(data)):
        j = i
        while j >0:
            if data[j] < data[j-1]:
                data[j],data[j-1] = data[j-1],data[j]
                j-=1
            else:
                break
    return data

def mergesort(data):
    if len(data) <= 1:
        return data

    mid_pos = len(data)//2
    left = data[:mid_pos]
    right = data[mid_pos:]

    left = mergesort(left)
    right = mergesort(right)

    result = []
    while len(left)!=0:
        if len(right)!= 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    while len(right)!=0:
        result.append(right.pop(0))
    
    return result

    

if __name__ == "__main__":
    
    nums = [5,3,6,7,2,8,5,15,23,32]

    print(mergesort(nums))