# Stack Overflow
def sieve_for_prime_to(n):
    size = n // 2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1)-i)//val
            sieve[i+val::val] = [0]*tmp
    return [2]+[i*2+1 for i, v in enumerate(sieve) if v and i > 0]

if __name__ == "__main__":
    result = []
    primes = sieve_for_prime_to(200000)
    print(primes[199998])
    n = int(input())
    inp = [int(x) for x in input().split()]

    for d in inp:
        result.append(primes[d+1])

    print(" ".join(str(x) for x in result))