# import random as r

# with open("randomNumber.txt","w") as wf :
#     for i in range(3) :
#         for _ in range(100 + r.randint(0,1)) :
#             wf.write(str(r.randint(-100,100)))
#             wf.write(" ")
#         wf.write("\n")

def median_of_array(data):
    data.sort()
    if len(data) % 2 == 1:
        return data[int((len(data)+1)/2)-1]
    else:
        return (data[int((len(data)/2) - 1)] + data[int(len(data)/2)])/2

if __name__ == "__main__":
    rand1 = ""
    rand2 = ""
    rand3 = ""
    with open("randomNumber.txt", "r") as rf:
        rand1 = rf.readline()
        rand2 = rf.readline()
        rand3 = rf.readline()

    rand1 = [x for x in map(int, rand1.split())]
    rand2 = [x for x in map(int, rand2.split())]
    rand3 = [x for x in map(int, rand3.split())]

    print(median_of_array(rand1))
    print(median_of_array(rand2))
    print(median_of_array(rand3))