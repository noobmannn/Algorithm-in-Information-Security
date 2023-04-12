import math


def parseIntegerToArray(a, t, w):
    A = [0 for _ in range(t)]
    i = t - 1
    while a != 0:
        A[i] = int(a / pow(2, i * w))
        a = int(a % pow(2, i * w))
        i -= 1
    return A


def parseArrayToInteger(a, w):
    res = 0
    for i in range(len(a)):
        res += pow(2, (i * w)) * a[i]
    return res


def MultiprecisionAddition(a, b, t, w):
    A = parseIntegerToArray(a, t, w)
    B = parseIntegerToArray(b, t, w)
    C = [0 for _ in range(t)]
    C[0] = int((A[0] + B[0]) % pow(2, w))
    e = int((A[0] + B[0]) / pow(2, w))
    for i in range(1, t):
        C[i] = int((A[i] + B[i] + e) % pow(2, w))
        e = int((A[i] + B[i]) / pow(2, w))
    return e, C


def MultiprecisionSubtraction(a, b, t, w):
    A = parseIntegerToArray(a, t, w)
    B = parseIntegerToArray(b, t, w)
    C = [0 for _ in range(t)]
    e = 0
    C[0] = A[0] - B[0]
    if C[0] < 0 or C[0] > pow(2, w):
        C[0] = C[0] % pow(2, w)
        e = 1
    for i in range(1, t):
        C[i] = A[i] - B[i] - e
        e = 0
        if C[i] < 0 or C[i] > pow(2, w):
            C[i] = C[i] % pow(2, w)
            e = 1
    return e, C


def AdditionInFp(a, b, p, w):
    m = round(math.log(p, 2))
    t = round(m / w)
    e, C = MultiprecisionAddition(a, b, t, w)
    if e == 1:
        e, C = MultiprecisionSubtraction(parseArrayToInteger(C, w), p, t, w)
    return e, C


def printReverseList(n):
    str = "["
    for i in range(len(n) - 1, -1, -1):
        if i != 0:
            str += f"{n[i]}, "
        else:
            str += f"{n[i]}]"
    return str


def printResult(e, C):
    str = f"({e}, " + printReverseList(C) + ")"
    return str


def main():
    w = 8
    p = 2147483647
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    e2, res2 = AdditionInFp(a, b, p, w)
    print(f"Kết quả phép cộng trên trường Fp với p = {p} là: " + printReverseList(res2))
    print(f"Kết quả dạng số nguyên: {parseArrayToInteger(res2, w)}")


if __name__ == "__main__":
    main()
