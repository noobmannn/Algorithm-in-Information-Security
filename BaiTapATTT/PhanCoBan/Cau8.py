def findTPrime(n):
    d = 2
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            d += 1
    return d == 3


def main():
    n = int(input("Nhập vào N: "))
    listRes = []
    for i in range(1, n):
        if findTPrime(i):
            listRes.append(i)
    if len(listRes) != 0:
        print(f"Các số T-Prime nhỏ hơn hoặc bằng {n} là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây số T-Prime thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
