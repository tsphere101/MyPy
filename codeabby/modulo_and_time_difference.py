def difference(data):
    day1, hour1, minute1, second1, day2, hour2, minute2, second2 = data
    if(day2 < day1):
        raise ValueError
    time1 = day1*24*60*60 + hour1*60*60 + minute1 * 60 + second1
    time2 = day2*24*60*60 + hour2*60*60 + minute2 * 60 + second2
    day = int((time2-time1)/86400)
    hour = int(((time2-time1)/3600) % 24)
    minute = int(((time2-time1)/60) % 60)
    second = int((time2-time1) % 60)
    return  [second, minute, hour, day]

def print_data(data):
    for i in range(len(data)):
        print(f"({data[i][3]} {data[i][2]} {data[i][1]} {data[i][0]})", end=" ")

if __name__ == "__main__":
    result = []
    for _ in range(int(input())):
        result.append(difference([int(x) for x in input().split()]))
    print_data(result)