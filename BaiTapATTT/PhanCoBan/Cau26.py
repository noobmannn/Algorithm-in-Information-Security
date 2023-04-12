def sieveOfEratosthenes(n):
    check = [True for _ in range(n + 1)]
    listPr = []
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(2, n + 1):
        if check[p]:
            listPr.append(p)
    return listPr


def checkSNum(n):
    listPr = sieveOfEratosthenes(n)
    for i in listPr:
        if n % i == 0 and n % (i ** 2) == 0:
            return True
    return False


def main():
    n = int(input("Nhập vào N: "))
    listRes = []
    for i in range(1, n):
        if checkSNum(i):
            listRes.append(i)
    if len(listRes) != 0:
        print(f"Các số S-Num nhỏ hơn hoặc bằng {n} là: ", end="")
        print(listRes)
    else:
        print("Không tìm thây số S-Num thoả yêu cầu!!!")
    print()


if __name__ == "__main__":
    main()
