import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def findDivisor(n):
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    return dem


def findPrimeDivisor(n):
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0 and checkPrime(i):
            dem += 1
    return dem


def main():
    n = int(input("Nhập N: "))
    print(f"Số ước của {n} là: ", end="")
    print(findDivisor(n))
    print(f"Số ước nguyên tố của {n} là: ", end="")
    print(findPrimeDivisor(n))


if __name__ == "__main__":
    main()
