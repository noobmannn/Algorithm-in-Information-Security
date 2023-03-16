import math


def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def inputArray(n):
    listArr = []
    for i in range(n):
        listArr.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
    return listArr


def main():
    n = int(input("Nhập kích thước mảng A: "))
    print("Nhập các phần tử cho mảng A: ")
    A = inputArray(n)
    print("Các cặp số thoả yêu cầu là: ")
    for i in range(n):
        for j in range(i + 1, n):
            if checkPrime(EuclideForFindGCD(A[i], A[j])):
                print(f"{A[i]} {A[j]}")


if __name__ == "__main__":
    main()
