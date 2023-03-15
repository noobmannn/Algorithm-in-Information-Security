def sieveOfEratosthenes(n):
    sum = 0
    check = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    for p in range(2, n + 1):
        if check[p]:
            sum += p
    return sum


def main():
    n = int(input("Nhập N: "))
    print(f"Tổng các số nguyên tố nhỏ hơn hoặc bằng {n} là: ", end="")
    print(sieveOfEratosthenes(n))


if __name__ == "__main__":
    main()
