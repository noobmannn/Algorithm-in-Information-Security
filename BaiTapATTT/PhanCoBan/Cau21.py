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
    cnt = 0
    for i in range(a, b + 1):
        if checkSuperPrime(i):
            cnt += 1
    return cnt


def main():
    while True:
        a = int(input("Nhập A: "))
        b = int(input("Nhập B: "))
        if a < b:
            break
        else:
            print("Vui lòng nhập A < B")
    print(f"Số các siêu số nguyên tố trong đoạn [{a}, {b}] là: ", end="")
    print(findSuperPrime(a, b))


if __name__ == "__main__":
    main()
