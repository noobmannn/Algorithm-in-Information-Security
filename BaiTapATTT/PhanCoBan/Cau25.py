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
    listRes = []
    listPr = sieveOfEratosthenes(n)
    for i in listPr:
        for j in listPr:
            for k in listPr:
                if i + j + k == n and i < j < k:
                    listTmp = [i, j, k]
                    listRes.append(listTmp)
    return listRes


def main():
    n = int(input("Nhập N: "))
    listRes = solve(n)
    if len(listRes) != 0:
        print(f"Các bộ ba số nguyên tố thoả yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây bộ ba số nguyên tố thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
