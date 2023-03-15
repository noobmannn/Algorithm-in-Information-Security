import math


def reverse(x):
    rev = 0
    while x > 0:
        rev = (rev * 10) + x % 10
        x = int(x / 10)
    return rev


def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, (int(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


def checkEmirpNumber(n):
    return checkPrime(n) and checkPrime(reverse(n))


def main():
    n = int(input("Nhập vào N: "))
    print(f"Các số Emirp nhỏ hơn hoặc bằng {n} là: ", end="")
    for i in range(1, n):
        if checkEmirpNumber(i):
            print(i, end=' ')
    print()


if __name__ == "__main__":
    main()
