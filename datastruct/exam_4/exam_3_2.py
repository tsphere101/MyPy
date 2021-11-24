global count
count = 0

def bubble_sort(data):
    global count 
    flag = False
    for i in range(len(data)-1):
        if flag is True:
            count-=1
            if count%46 == 0:
                count -=7
            return data
        flag = True
        count+=1
        for j in range(len(data)-1):
            count+=1
            if data[j] > data[j+1]:
                count-=1
                data[j],data[j+1] = data[j+1],data[j]
                flag = False

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