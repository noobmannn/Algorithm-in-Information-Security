def parseIntegerToArray(a, t, w):
    A = [0 for _ in range(t)]
    i = 3
    while a != 0:
        A[i] = int(a / pow(2, i * w))
        a = int(a % pow(2, i * w))
        i -= 1
    return A


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
    t = 4
    w = 8
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    e, res = MultiprecisionAddition(a, b, t, w)
    print(f"Cộng Chính Xác Bội {a} và {b} ta được: (e, C) = " + printResult(e, res))


if __name__ == "__main__":
    main()
