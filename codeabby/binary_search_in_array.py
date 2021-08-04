def binary_search(data,left,right,target):
    if right >= left:
        mid = int((left+right ) /2)

        if data[mid] == target:
            # Found
            return mid

        elif data[mid] > target:
            return binary_search(data,left,mid-1,target)
        else :
            return binary_search(data,mid+1,right,target)

    else :
        # Not found
        return right

def ask_ips(ips):
    result = []    
    ips = [int(str(x),36) for x in ips]

    # Loading
    countries,start_ip,offsets = [],[],[]
    with open("db-ip.txt","r") as file:
        for line in file:
            start,offset,country = line.split()
            start = int(str(start),36)
            offset= int(str(offset),36)
            start_ip.append(start)
            offsets.append(offset)
            countries.append(country)

    for d in ips:
        target = d
        inrange = binary_search(start_ip,0,len(start_ip)-1,target)
            # Found at the edge
            # result.append(countries[inrange])
        if target >= start_ip[inrange] and target <= start_ip[inrange]+offsets[inrange]:
            result.append(countries[inrange])
        else : result.append("UNKNOWN")

    return result

if __name__ == '__main__':

    n = int(input())
    ips = []
    for _ in range(n):
        ips.append(input())
    result = ask_ips(ips)
    print(" ".join(result))