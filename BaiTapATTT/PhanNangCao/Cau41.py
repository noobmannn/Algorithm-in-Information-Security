import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def convertDecToReverseBin(n):
    binaryList = []
    while n > 0:
        binaryList.append(n % 2)
        n = int(n / 2)
    return binaryList


def ExponentialSquaring(a, k, n):
    A = a
    b = 1
    kList = convertDecToReverseBin(k)
    if kList[0] == 1:
        b = a
    for i in range(1, len(kList)):
        A = (A * A) % n
        if kList[i] == 1:
            b = (A * b) % n
    return b


def main():
    a = int(input("Nhập A: "))
    k = int(input("Nhập K: "))
    n = int(input("Nhập N: "))
    if checkPrime(ExponentialSquaring(a, k, n)):
        print(f"{a}^{k} mod {n} là số nguyên tố!!!")
    else:
        print(f"{a}^{k} mod {n} không phải là số nguyên tố!!!")


if __name__ == "__main__":
    main()
