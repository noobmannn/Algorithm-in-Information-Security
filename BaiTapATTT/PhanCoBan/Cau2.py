import math


def sieveOfEratosthenes(m, n):
    check = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    if m < 2:
        m = 2
    for p in range(m, n + 1):
        if check[p]:
            print(p, end=' ')
    print()


def main():
    n = int(input("Nhập N: "))
    d1 = int(math.pow(10, n - 1))
    d2 = int(math.pow(10, n) - 1)
    print(f"Các số nguyên tố có {n} chữ số là: ", end="")
    sieveOfEratosthenes(d1, d2)


if __name__ == "__main__":
    main()
