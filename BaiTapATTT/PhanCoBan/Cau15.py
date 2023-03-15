def sieveOfEratosthenes(n):
    listPrime = []
    check = [True for i in range(n + 1)]
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
    listPrime = sieveOfEratosthenes(n)
    for i in range(len(listPrime)):
        if listPrime[i] - listPrime[i - 1] == 2:
            print(f"{listPrime[i - 1]} {listPrime[i]}")


def main():
    n = int(input("Nhập N: "))
    print(f"Các cặp số nguyên tố thoả mãn yêu cầu là: ")
    findTwinPrime(n)


if __name__ == "__main__":
    main()
