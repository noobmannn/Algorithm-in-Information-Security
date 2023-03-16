import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def F(n):
    if checkPrime(n):
        return n
    else:
        return 0


def sum(l, r):
    s = 0
    for i in range(l + 1, r):
        for j in range(i + 1, r):
            s += F(i) * F(j)
    return s


def main():
    l = int(input("Nhập L: "))
    r = int(input("Nhập R: "))
    print(f"Tổng cần tim là: ", end="")
    print(sum(l, r))


if __name__ == "__main__":
    main()
