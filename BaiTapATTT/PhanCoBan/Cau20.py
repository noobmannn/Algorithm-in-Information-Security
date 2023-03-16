def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


def findAB(m, n, d):
    for i in range(m + 1, n):
        for j in range(i + 1, n):
            if EuclideForFindGCD(i, j) == d:
                print(f"{i} {j}")


def main():
    m = int(input("Nhập M: "))
    n = int(input("Nhập N: "))
    d = int(input("Nhập D: "))
    print(f"Các cặp số nguyên cần tim là: ")
    findAB(m, n, d)


if __name__ == "__main__":
    main()
