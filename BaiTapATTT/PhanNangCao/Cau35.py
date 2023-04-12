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


def Miller_RabinCheckPrimeNumber(n, t):
    s, r = 0, 0
    while r % 2 != 1:
        r = int((n - 1) / pow(2, s))
        s += 1
    s -= 1
    for i in range(t):
        a = random.randint(2, n - 2)
        y = ExponentialSquaring(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y ** 2) % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True


def main():
    while True:
        n = int(input("Nhập N: "))
        t = int(input("Nhập số lần thử T: "))
        if t > 0:
            break
        else:
            print("Vui lòng nhập N >= 4 và T > 0!!!")
    if Miller_RabinCheckPrimeNumber(n, t):
        print(f"{n} là số nguyên tố")
        print(f"Xác xuất để {n} đúng là số nguyên tố là: {1 - 1 / 4 ** t}")
    else:
        print(f"{n} không phải là số nguyên tố")


if __name__ == "__main__":
    main()
