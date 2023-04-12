def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


def pollardsRhoAlgorithm(n):
    a = 2
    b = 2
    d = 1
    while d == 1:
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        d = EuclideForFindGCD(abs(a - b), n)
    if 1 < d < n:
        return d
    if d == n:
        return -1


def main():
    n = int(input("Nhập N: "))
    d = pollardsRhoAlgorithm(n)
    if d != -1:
        print(f"Thừa số không tầm thường của {n} là: d = {d}")
    else:
        print("Không tìm thấy thừa số không tầm thường")


if __name__ == "__main__":
    main()
