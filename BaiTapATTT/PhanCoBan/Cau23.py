import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def solve(a, b):
    sumPr = 0
    for i in range(a, b):
        if checkPrime(i):
            sumPr += i
    if checkPrime(sumPr):
        print("YES")
    else:
        print("NO")


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    solve(a, b)


if __name__ == "__main__":
    main()
