def findQPrime(n):
    d = 2
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            d += 1
    return d == 3


def main():
    n = int(input("Nhập N: "))
    print(f"Các số T-Prime nhỏ hơn hoặc bằng {n} là: ", end="")
    for i in range(1, n):
        if findQPrime(i):
            print(i, end=' ')
    print()


if __name__ == "__main__":
    main()
