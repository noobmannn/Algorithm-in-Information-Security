import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


def findAB(a, b):
    listRes = []
    for i in range(a, b):
        for j in range(i + 1, b):
            if checkPrime(EuclideForFindGCD(i, j)):
                listTmp = [i, j]
                listRes.append(listTmp)
    return listRes


def main():
    while True:
        a = int(input("Nhập A: "))
        b = int(input("Nhập B: "))
        if 0 < a < b < 1000:
            break
        else:
            print("Đầu vào sai, hãy nhập lại!!!")
    listRes = findAB(a, b)
    if len(listRes) != 0:
        print(f"Các cặp số thoả yêu cầu là: {listRes}")
    else:
        print(f"Không tìm thây cặp số thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
