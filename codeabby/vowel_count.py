def vo_count(str_in) :
    count = 0
    for c in str_in:
        if c.lower() in "aeiuoy" :
            count+=1
    return count

result = []
for i in range(int(input())):
    result.append(vo_count(input()))

print(" ".join([str(x) for x in result]))
