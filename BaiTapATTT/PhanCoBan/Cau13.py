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
    for p in range(2, n + 1):
        if check[p]:
            listPrime.append(p)
    for i in range(1, n):
        for j in range(0, i):
            if checkPrime(listPrime[i] + listPrime[j]) and checkPrime(abs(listPrime[i] - listPrime[j])):
                return listPrime[i], listPrime[j]


def main():
    n = int(input("Nhập N: "))
    print(f"Các số nguyên tố thoả mãn yêu cầu là: ", end="")
    print(sieveOfEratosthenes(n))


if __name__ == "__main__":
    main()
