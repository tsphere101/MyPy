def winner(n, step):

    soldier = [x for x in range(1, n+1)]
    leng = len(soldier)
    pop_pos = step-1
    i = 0
    while(len(soldier) > 1):
        if pop_pos >= leng:
            pop_pos -= leng
            leng = len(soldier)
            i = 0
        else:
            soldier.pop(pop_pos-i)
            pop_pos += step
            i += 1

    return soldier[0]


if __name__ == "__main__":
    n, step = [x for x in map(int, input().split())]
    print(winner(n, step))
