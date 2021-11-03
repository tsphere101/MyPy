def harmonic_sum(n):
    # code here
    if n == 1:
        # Base case
        print(1, end=" ")
        return n

    result = harmonic_sum(n-1) + 1/n

    print(f"+ 1/{n}", end=" ")

    return result


print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : "))
print("= %.8f" % (harmonic_sum(num)))
