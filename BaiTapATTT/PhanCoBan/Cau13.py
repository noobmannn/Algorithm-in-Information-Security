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
    listRes = []
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
    for i in range(len(listPrime)):
        for j in range(i + 1, len(listPrime)):
            if checkPrime(listPrime[i] + listPrime[j]) and checkPrime(abs(listPrime[i] - listPrime[j])):
                listTmp = [listPrime[i], listPrime[j]]
                listRes.append(listTmp)
    return listRes


def main():
    n = int(input("Nhập N: "))
    listRes = sieveOfEratosthenes(n)
    if len(listRes) != 0:
        print(f"Các cặp số nguyên tố thoả mãn yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây cặp số nguyên tố thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
