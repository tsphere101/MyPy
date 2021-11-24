global count
count = 0

def bubble_sort(data):
    ce = False
    global count
    flag = True
    l = len(data)-1
    y = 0 
    print(l)
    for i in range(len(data)-1):
        y+= l-i
        # print(l,i)
        print(data)
        if flag:
            flag = False
            t = 0
            f = 0
            for j in range(len(data)-1):
                t+=1
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    flag = True
                if flag is True:
                    f+=1
                # print(f)
                # print(j,i)
            count+=f 
            if flag is False:
                if i == 0:
                    count = t

                return data
        else:
            break
    print("im' OUT T",y)
    return data



print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bubble_sort(A)
print()
print(A)
print("Data comparison =", count)