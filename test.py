def isUgly(n):
    if n < 0 :
            return False
    if n == 1:
        return True

    count = 0
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,]

    for prime in primes:
        if n % prime == 0:
            if prime >= 7:
                return False
        else:
            print()
            count += 1
    if count == 0:
        print("count is zero")
        return False
    else:
        return True

print(isUgly(101))