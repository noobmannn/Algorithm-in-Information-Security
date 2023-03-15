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


def solve(n):
    listPr = sieveOfEratosthenes(n)
    for i in listPr:
        for j in listPr:
            for k in listPr:
                if i + j + k == n and i < j < k:
                    print(i, j, k)


def main():
    n = int(input("Nhập N: "))
    print("Các bộ ba số nguyên tố thoả yêu cầu là: ")
    solve(n)


if __name__ == "__main__":
    main()
