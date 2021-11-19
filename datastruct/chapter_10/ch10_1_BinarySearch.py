def bi_search(l, r, arr, x):
    mid = (r+l)//2
    piv = arr[mid]
    if r<l:
        return False
    if piv == x:
        return True
    elif x < piv:
        return bi_search(l,mid-1,arr,x)
    elif x > piv:
        return bi_search(mid+1,r,arr,x)


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))