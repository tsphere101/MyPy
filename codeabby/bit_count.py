
# Stackoverflow
def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def to_bin(n):
    s = bin(n & 0b11111111111111111111111111111111)[2:]
    return "{0:0>32}".format(s)

def count_bits(strings):
    bits = 0
    for s in strings:
        if s == "1":
            bits += 1
    return str(bits)

if __name__ == "__main__":

    input()
    data = list(map(int, input().split()))
    data = list(map(to_bin, data))
    data = list(map(count_bits, data))

    print(" ".join(data))
