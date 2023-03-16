import random
import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def sieveOfEratosthenes(n):
    check = [True for _ in range(n + 1)]
    listPr = []
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(2, n + 1):
        if check[p]:
            listPr.append(p)
    return listPr


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


def Miller_RabinCheckPrimeNumber(n, t):
    s, r = 0, 0
    while r % 2 != 1:
        r = int((n - 1) / pow(2, s))
        s += 1
    s -= 1
    for i in range(t):
        a = random.randint(2, n - 2)
        y = ExponentialSquaring(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y ** 2) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True


def GenerateRandomPrimeNumber(k, t):
    while True:
        res = random.randint(5, 2 ** k - 1)
        flag = True
        listPr = sieveOfEratosthenes(res - 1)
        for i in listPr:
            if res % i == 0:
                flag = False
                break
        if flag:
            if Miller_RabinCheckPrimeNumber(res, t):
                return res


def main():
    listPr = []
    while True:
        p = GenerateRandomPrimeNumber(10, 10)
        q = GenerateRandomPrimeNumber(10, 10)
        if 0 < p < 1000 and 0 < q < 100:
            break
    for i in range(100):
        if checkPrime(ExponentialSquaring(i, p, q)):
            listPr.append(i)
    print(f"p = {p}, q = {q}")
    print(f"Tập các số thoả yêu cầu là: {listPr}")


if __name__ == "__main__":
    main()
