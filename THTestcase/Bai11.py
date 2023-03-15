import math


def pollardsRhoAlgorithm(n):
    a = 2
    b = 2
    d = 1
    while d == 1:
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        d = math.gcd(abs(a - b), n)
    if d == n:
        return -1
    else:
        return d


def main():
    n = int(input("Nhập N: "))
    print(f"Thừa số không tầm thường của {n} là: d = {pollardsRhoAlgorithm(n)}")


if __name__ == "__main__":
    main()
