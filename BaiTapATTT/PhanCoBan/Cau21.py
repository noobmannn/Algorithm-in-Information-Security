import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def checkSuperPrime(n):
    cntPr = 0
    for i in range(1, n):
        if checkPrime(i):
            cntPr += 1
    return checkPrime(cntPr)


def findSuperPrime(a, b):
    listResult = []
    for i in range(a, b):
        if checkSuperPrime(i):
            listResult.append(i)
    return listResult


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    print(f"Các siêu số nguyên tố trong khoảng ({a}, {b}) là: ", end="")
    print(findSuperPrime(a, b))


if __name__ == "__main__":
    main()
