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


def findSNum(n):
    listPr = sieveOfEratosthenes(int(n / 2))
    for i in listPr:
        if n % i == 0 and n % (i ** 2) == 0:
            return n


def main():
    n = int(input("Nhập N: "))
    print(f"Các số S-Num nhỏ hơn hoặc bằng {n} là: ", end="")
    for i in range(1, n):
        if findSNum(i):
            print(i, end=' ')
    print()


if __name__ == "__main__":
    main()
