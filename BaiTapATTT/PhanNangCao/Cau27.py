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
    for i in range(a, b):
        for j in range(i + 1, b):
            if checkPrime(EuclideForFindGCD(i, j)):
                print(f"{i} {j}")


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    print(f"Các cặp số thoả yêu cầu là: ")
    findAB(a, b)


if __name__ == "__main__":
    main()
