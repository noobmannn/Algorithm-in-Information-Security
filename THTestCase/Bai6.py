"""
w = 8, p = 2147483647
m = log cơ số 2 của p = 31
t = 31/8 = 3.875 làm tròn thành t = 4
"""


def parseIntegerToArray(a, t, w):
    A = [0 for _ in range(t)]
    i = 3
    while a != 0:
        A[i] = int(a / pow(2, i * w))
        a = int(a % pow(2, i * w))
        i -= 1
    return A


def cutBit(n):
    u = n >> 8
    v = n - u * 256
    return u, v


def IntegerMultiprecision(a, b, t, w):
    A = parseIntegerToArray(a, t, w)
    B = parseIntegerToArray(b, t, w)
    C = [0 for _ in range(2 * t)]
    for i in range(t):
        U = 0
        for j in range(t):
            UV = C[i + j] + A[i] * B[j] + U
            U, V = cutBit(UV)
            C[i + j] = V
        C[i + t] = U
    return C


def printReverseList(n):
    str = "["
    for i in range(len(n) - 1, -1, -1):
        if i != 0:
            str += f"{n[i]}, "
        else:
            str += f"{n[i]}]"
    return str


def parseArrayToInteger(a, w):
    res = 0
    for i in range(len(a)):
        res += pow(2, (i * w)) * a[i]
    return res


def main():
    t = 4
    w = 8
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    C = IntegerMultiprecision(a, b, t, w)
    print("Kết quả phép tính nhân theo thuật toán Integer Multiplication (Operand Scanning Form) là: ")
    print(f"{a} * {b} = " + printReverseList(C))
    print(f"Dạng số nguyên: {parseArrayToInteger(C, w)}")


if __name__ == "__main__":
    main()
