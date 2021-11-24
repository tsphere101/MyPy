global count
count = 0
def mergesort(data):
    global count
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
            count += 1
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    while len(right)!=0:
        result.append(right.pop(0))
    
    return result

print(" *** Merge sort ***")
data = input("Enter some numbers : ").split()
data = [int(x) for x in data]
print()

print("Sorted ->"," ".join(str(x) for x in mergesort(data)))
print("Data comparison = ",count)
