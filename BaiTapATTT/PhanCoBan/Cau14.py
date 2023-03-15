import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def sieveOfEratosthenes(n):
    listPrime = []
    check = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(100, n + 1):
        if check[p]:
            listPrime.append(p)
    return listPrime


def reverse(x):
    rev = 0
    while x > 0:
        rev = (rev * 10) + x % 10
        x = int(x / 10)
    return rev


def findNumber():
    listNum = sieveOfEratosthenes(999)
    listResult = []
    for i in listNum:
        for j in range(1, int(i / 2 + 1)):
            if j * j * j == reverse(i):
                listResult.append(i)
    return listResult


def main():
    print(f"Các số nguyên tố thoả mãn yêu cầu là: ", end="")
    print(findNumber())


if __name__ == "__main__":
    main()
