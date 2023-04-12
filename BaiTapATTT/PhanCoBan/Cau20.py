def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


def findAB(m, n, d):
    listRes = []
    for i in range(m + 1, n):
        for j in range(i + 1, n):
            if EuclideForFindGCD(i, j) == d:
                listTmp = [i, j]
                listRes.append(listTmp)
    return listRes


def main():
    while True:
        m = int(input("Nhập M: "))
        n = int(input("Nhập N: "))
        if m < n:
            break
        else:
            print("Vui lòng nhập M < N")
    d = int(input("Nhập D: "))
    listRes = findAB(m, n, d)
    if len(listRes) != 0:
        print(f"Các cặp số nguyên thoả mãn yêu cầu là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây cặp số nguyên thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
