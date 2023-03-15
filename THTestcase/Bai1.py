def parseIntegerToArray(a, t, w):
    A = [0 for _ in range(t)]
    i = 3
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


def printReverseList(n):
    str = "["
    for i in range(len(n) - 1, -1, -1):
        if i != 0:
            str += f"{n[i]}, "
        else:
            str += f"{n[i]}]"
    return str


def inputList():
    n = []
    for i in range(4):
        n.append(int(input(f"Phần tử thứ {4 - i}: ")))
    return n


def main():
    A = int(input("Nhập A: "))
    print(f"Dạng mảng các từ 8 bit của số {A} là: {printReverseList(parseIntegerToArray(A, 4, 8))}")
    print("Nhập một mảng 4 từ 8 bit: ")
    arr = inputList()
    print(f"Giá trị của mảng {printReverseList(arr)} là: {parseArrayToInteger(arr, 8)}")


if __name__ == "__main__":
    main()
