def check_sum(list_of_num) :
    SEED = 113
    LIMIT = 10000007
    result = 0
    for i in range(len(list_of_num)) :
        result = ((result+list_of_num[i]) * SEED)%LIMIT
    return result


if __name__ == "__main__":
    input()
    print(check_sum([x for x in map(int,input().split())]))