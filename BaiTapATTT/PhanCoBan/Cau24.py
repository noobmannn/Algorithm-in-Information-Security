import math


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def check(n, S):
    b = len(S)
    for i in range(1, b):
        for j in range(0, i):
            if i ** 2 + j ** 2 == n:
                return True
    return False


def solve(a, b):
    listResult = []
    S = [i ** 2 for i in range(b)]
    for i in range(a, b):
        if checkPrime(i) and check(i, S):
            listResult.append(i)
    return listResult


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    print(f"Các số nguyên tố thoả yêu cầu là: ", end="")
    print(solve(a, b))


if __name__ == "__main__":
    main()
