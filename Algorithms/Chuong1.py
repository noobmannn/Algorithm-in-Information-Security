import math
'''
w = 8, p = 2147483647
m = log cơ số 2 của p = 31
t = 31/8 = 3.875 làm tròn thành t = 4
'''


# Chuyển số thành mảng W-Bit
def parseIntegerToArray(a, t, w):
    A = [0 for _ in range(t)]
    i = 3
    while a != 0:
        A[i] = int(a / pow(2, i * w))
        a = int(a % pow(2, i * w))
        i -= 1
    return A


# Chuyển mảng W-bit thành số
def parseArrayToInteger(a, w):
    res = 0
    for i in range(len(a)):
        res += pow(2, (i * w)) * a[i]
    return res


# Cộng Chính Xác Bội
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


# Trừ Chính Xác Bội
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


# Cộng trên trường Fp
def AdditionInFp(a, b, p, w):
    m = round(math.log(p, 2))
    t = round(m / w)
    e, C = MultiprecisionAddition(a, b, t, w)
    if e == 1:
        e, C = MultiprecisionSubtraction(parseArrayToInteger(C, w), p, t, w)
    elif parseArrayToInteger(C, w) >= p:
        e, C = MultiprecisionSubtraction(parseArrayToInteger(C, w), p, t, w)
    return e, C


# Trừ trên trường Fp
def SubtractionInFp(a, b, p, w):
    m = round(math.log(p, 2))
    t = round(m / w)
    e, C = MultiprecisionSubtraction(a, b, t, w)
    if e == 1:
        e, C = MultiprecisionAddition(parseArrayToInteger(C, w), p, t, w)
    return e, C


# Nhân trên trường Fp
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


# Thuật toán Euclid thường
def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


# Thuật toán Euclid mở rộng
def ExtendedEuclide(a, b):
    if a == 0:
        return b, 0, 1
    d, x, y = ExtendedEuclide(b % a, a)
    return d, y - (b // a) * x, x


# Tìm nghịch đảo theo molule p
def ModularInverse(a, p):
    d, x, y = ExtendedEuclide(a, p)
    if d != 1:
        return -1
    else:
        return x % p


def main():
    # Chuyển số thành mảng W-Bit
    print(parseIntegerToArray(23456789, 4, 8))
    print()
    # Chuyển mảng W-bit thành số
    print(parseArrayToInteger([21, 236, 101, 1], 8))
    print()
    # Cộng Chính Xác Bội
    print(MultiprecisionAddition(765432, 123456, 4, 8))
    print(MultiprecisionAddition(2147483646, 2147483643, 4, 8))
    print()
    # Trừ Chính Xác Bội
    print(MultiprecisionSubtraction(765432, 123456, 4, 8))
    print(MultiprecisionSubtraction(65324842, 2354, 4, 8))
    print()
    # Cộng trên trường Fp
    print(AdditionInFp(347483646, 474836419, 479001599, 8))
    print(AdditionInFp(2147483645, 2971215070, 2971215073, 8))
    print()
    # Trừ trên trường Fp
    print(SubtractionInFp(1387624979, 1568424364, 2147483647, 8))
    print(SubtractionInFp(333294897, 183494999, 433494437, 8))
    print()
    # Nhân trên trường Fp
    print(IntegerMultiprecision(524647, 32549, 4, 8))
    print()
    # Thuật toán Euclid thường
    print(EuclideForFindGCD(45632454, 23454563))
    print(EuclideForFindGCD(28150488, 10507620))
    print()
    # Thuật toán Euclid mở rộng
    print(ExtendedEuclide(34568734, 487345936))
    print(ExtendedEuclide(45632454, 23454563))
    print()
    # Tìm nghịch đảo theo molule p
    print(ModularInverse(45682375, 489573857))
    print(ModularInverse(5464144, 489573857))
    print()


if __name__ == "__main__":
    main()
