def lastOccur(p, c):
    i = len(p) - 1
    while i >= 0:
        if p[i] == c:
            return i
        i = i - 1
    return -1


def boyerMooreSearch(T, P):
    listRes = []
    i = len(P) - 1
    j = len(P) - 1
    while i <= len(T) - 1:
        if T[i] == P[j]:
            if j == 0:
                listRes.append(i)
                i += 1
            else:
                i -= 1
                j -= 1
        else:
            i = i + len(P) - min(j, 1 + lastOccur(P, T[i]))
            j = len(P) - 1
    return listRes


def stringResult(listRes):
    s = ""
    for i in listRes:
        s += str(i) + " "
    return s


def main():
    T = input("Nhập chuỗi T: ")
    P = input("Nhập chuỗi P: ")
    listRes = boyerMooreSearch(T, P)
    print("Bảng giá trị lần xuất hiện cuối cùng: ")
    for i in P:
        print(f"{i}: {lastOccur(P, i)}")
    if len(listRes) != 0:
        print(f"Vị trí xuất hiện của chuỗi \"{P}\" trong chuỗi \"{T}\" là: " + stringResult(listRes))
    else:
        print(f"Chuỗi \"{P}\" không nằm trong chuỗi \"{T}\"!")


if __name__ == "__main__":
    main()
