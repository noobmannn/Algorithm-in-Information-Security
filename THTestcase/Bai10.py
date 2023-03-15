import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


# Vét Cạn
def completeSearch(n):
    for i in range(2, n):
        if checkPrime(i):
            print(i, end=" ")
    print()


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
    listPr = []
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
            listPr.append(p)
    return listPr


def printList(n):
    for i in n:
        print(i, end=" ")
    print()


def main():
    n = int(input("Nhập n: "))
    print("Các số nguyên tố từ 1 đến n: ")
    print("1. Vét Cạn: ")
    completeSearch(n)
    print("2. Sàng Eratosthenes Nguyên Thuỷ: ")
    printList(sieveOfEratosthenes(n))
    print("3. Sàng Eratosthenes Phân Đoạn: ")
    printList(segmentedSieveOfEratosthenes(n))


if __name__ == "__main__":
    main()
