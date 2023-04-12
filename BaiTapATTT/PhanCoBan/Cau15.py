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


def findTwinPrime(n):
    listRes = []
    listPrime = sieveOfEratosthenes(n)
    for i in range(len(listPrime)):
        if listPrime[i] - listPrime[i - 1] == 2:
            listTmp = [listPrime[i - 1], listPrime[i]]
            listRes.append(listTmp)
    return listRes


def main():
    n = int(input("Nhập N: "))
    listRes = findTwinPrime(n)
    if len(listRes) != 0:
        print(f"Các cặp số nguyên tố thoả mãn yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây cặp số nguyên tố thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
