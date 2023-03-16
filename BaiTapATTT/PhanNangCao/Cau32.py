import math
import random


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
                if i == 1:
                    return False
                j += 1
            if y != n - 1:
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


def ExtendedEuclide(a, b):
    if a == 0:
        return b, 0, 1
    d, x, y = ExtendedEuclide(b % a, a)
    return d, y - (b // a) * x, x


def ModularInverse(a, p):
    d, x, y = ExtendedEuclide(a, p)
    if d != 1:
        return -1
    else:
        return x


def RSA():
    while True:
        p = GenerateRandomPrimeNumber(9, 5)
        q = GenerateRandomPrimeNumber(9, 5)
        if 100 < p < 500 and 100 < q < 500:
            break
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1 and ModularInverse(e, phi) > 0:
            break
    d = ModularInverse(e, phi)
    m = int(input("Nhập SBD: "))
    m += 123
    c = ExponentialSquaring(m, e, n)
    print(f"Bản mã C là: {c}")
    m = ExponentialSquaring(c, d, n)
    print(f"Giải mã m: {m}")
    print(f"p = {p}, q = {q}, n = {n}, phi = {phi}, d = {d}, e = {e}")


def main():
    RSA()


if __name__ == "__main__":
    main()
