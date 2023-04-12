def checkFNumber(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


def main():
    n = int(input("Nhập vào N: "))
    listRes = []
    for i in range(1, n):
        if checkFNumber(i):
            listRes.append(i)
    if len(listRes) != 0:
        print(f"Các số F-Number nhỏ hơn hoặc bằng {n} là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây số F-Number thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
