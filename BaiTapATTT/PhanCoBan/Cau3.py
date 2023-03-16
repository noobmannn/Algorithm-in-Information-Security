import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def findK(n):
    k = 0
    for i in range(1, n + 1):
        if n % i == 0 and checkPrime(i):
            k += 1
    return k


def findQ(n):
    q = 0
    for i in range(1, n + 1):
        if n % i == 0 and checkPrime(i):
            q += i
    return q


def findP(n):
    p = 0
    for i in range(1, n + 1):
        if n % i == 0:
            p += i
    return p


def findS(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    return s


def main():
    N = int(input("Nhập N: "))
    print(f"k = {findK(N)}, q = {findQ(N)}, p = {findP(N)}, s = {findS(N)}")
    print("Tổng cần tìm là: N + p + s - q - k = ", end="")
    print(N - findK(N) - findQ(N) + findP(N) + findS(N))


if __name__ == "__main__":
    main()
