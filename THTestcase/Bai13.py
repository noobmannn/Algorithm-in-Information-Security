import random


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
    # return a^k%n


# Kiểm tra số nguyên tố theo thuật toán Fermat
def FermatCheckPrimeNumber(n, t):
    for i in range(t):
        a = random.randint(2, n - 2)
        r = ExponentialSquaring(a, n - 1, n)
        if r != 1:
            return False
    return True


def main():
    n = int(input("Nhập N: "))
    if FermatCheckPrimeNumber(n, 7):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")


if __name__ == "__main__":
    main()
