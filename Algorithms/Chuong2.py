import math
import random


# Sàng Eratosthenes Nguyên Thuỷ
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


# Sàng Eratosthenes Phân Đoạn
def simpleSieve(n):
    check = [True for _ in range(n + 1)]
    prime = []
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(2, n + 1):
        if check[p]:
            prime.append(p)
    return prime


def segmentedSieveOfEratosthenes(n):
    p = int(math.sqrt(n))
    check = [True for _ in range(n + 1)]
    subCheck = simpleSieve(2 + p)
    for i in range(2, n - (n - 2) % p, p):
        for j in range(i, i + p):
            for pr in subCheck:
                if j != pr and j % pr == 0:
                    check[j] = False
                    break
    for i in range(n - (n - 2) % p, n + 1):
        for pr in subCheck:
            if i != pr and i % pr == 0:
                check[i] = False
                break
    for p in range(2, n + 1):
        if check[p]:
            print(p, end=' ')


# Thuật toán Pollard's Rho tìm thừa số không tầm thường
def pollardsRhoAlgorithm(n):
    a = 2
    b = 2
    d = 1
    while d == 1:
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        d = math.gcd(abs(a - b), n)
    if d == n:
        return -1
    else:
        return d


# Nhân Bình Phương Có Lặp
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
    # return a^k%n


# Kiểm tra số nguyên tố theo thuật toán Fermat
def FermatCheckPrimeNumber(n, t):
    for i in range(t):
        a = random.randint(2, n - 2)
        r = ExponentialSquaring(a, n - 1, n)
        if r != 1:
            return False
    return True


# Kiểm tra số nguyên tố theo thuật toán Miller_Rabin
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


# Sinh số nguyên tố ngẫu nhiên K-Bit
def GenerateRandomPrimeNumber(k, t):
    while True:
        res = random.randint(0, 2 ** k - 1)
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
    # Sàng Eratosthenes Nguyên Thuỷ
    for i in sieveOfEratosthenes(2003):
        print(i, end=" ")
    print()
    # Sàng Eratosthenes Phân Đoạn
    segmentedSieveOfEratosthenes(2003)
    print()
    # Thuật toán Pollard's Rho tìm thừa số không tầm thường
    print(pollardsRhoAlgorithm(455459))
    print()
    # Nhân Bình Phương Có Lặp
    print(ExponentialSquaring(10, 191, 383))
    print()
    # Kiểm tra số nguyên tố theo thuật toán Fermat
    print(FermatCheckPrimeNumber(383, 2))
    print()
    # Kiểm tra số nguyên tố theo thuật toán Miller_Rabin
    print(Miller_RabinCheckPrimeNumber(383, 10))
    print()
    # Sinh số nguyên tố ngẫu nhiên K-Bit
    print(GenerateRandomPrimeNumber(8, 5))
    print()


if __name__ == "__main__":
    main()
