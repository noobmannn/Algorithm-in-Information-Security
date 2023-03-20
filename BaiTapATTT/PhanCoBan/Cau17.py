import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def findX(n, A, B, C):
    for i in range(1, n):
        if checkPrime(A * (i ** 2) + B * i + C):
            return i
    return -1


def main():
    n = int(input("Nhập N: "))
    A = int(input("Nhập A: "))
    B = int(input("Nhập B: "))
    C = int(input("Nhập C: "))
    if findX(n, A, B, C) != -1:
        print(f"Số nguyên cần tim là: ", end="")
        print(findX(n, A, B, C))
    else:
        print("Không tìm thấy số nguyên thoả mãn yêu cầu!!!")


if __name__ == "__main__":
    main()
