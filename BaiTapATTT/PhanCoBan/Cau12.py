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
    return listPrime


def solve(n, k, listPrime):
    listResult = []
    for i in range(0, len(listPrime) - k):
        sum = 0
        k1 = 0
        while k1 < k:
            sum += listPrime[i + k1]
            k1 += 1
        if checkPrime(sum) and sum <= n:
            listTmp = []
            k1 = 0
            while k1 < k:
                listTmp.append(listPrime[i + k1])
                k1 += 1
            listResult.append(listTmp)
    return listResult


def main():
    n = int(input("Nhập N: "))
    k = int(input("Nhập K: "))
    listRes = solve(n, k, sieveOfEratosthenes(n))
    if len(listRes) != 0:
        print(f"Các bộ số nguyên tố thoả mãn yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thấy bộ số thoả mãn yêu cầu")


if __name__ == "__main__":
    main()
