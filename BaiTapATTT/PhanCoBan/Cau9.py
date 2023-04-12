def sieveOfEratosthenes(n):
    dem = 0
    check = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(2, n):
        if check[p]:
            dem += 1
    return dem


def main():
    n = int(input("Nhập N: "))
    print(f"Số số nguyên tố nhỏ hơn hoặc bằng {n} là: ", end="")
    print(sieveOfEratosthenes(n))
    print()


if __name__ == "__main__":
    main()
