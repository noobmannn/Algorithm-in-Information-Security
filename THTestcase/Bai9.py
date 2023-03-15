def convertDecToReverseBin(n):
    binaryList = []
    while n > 0:
        binaryList.append(n % 2)
        n = int(n / 2)
    return binaryList


def ExponentialSquaring(a, k, n):
    A = a
    b = 1
    kList = convertDecToReverseBin(k)
    if kList[0] == 1:
        b = a
    for i in range(1, len(kList)):
        A = (A * A) % n
        if kList[i] == 1:
            b = (A * b) % n
    return b


def main():
    a = int(input("Nhập A: "))
    k = int(input("Nhập K: "))
    n = int(input("Nhập N: "))
    print(f"A^K mod N = {ExponentialSquaring(a, k, n)}")


if __name__ == "__main__":
    main()
