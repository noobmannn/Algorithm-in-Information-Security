def checkFNumber(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


def main():
    n = int(input("Nhập vào N: "))
    print(f"Các số F-Number nhỏ hơn hoặc bằng {n} là: ", end="")
    for i in range(1, n):
        if checkFNumber(i):
            print(i, end=' ')
    print()


if __name__ == "__main__":
    main()
