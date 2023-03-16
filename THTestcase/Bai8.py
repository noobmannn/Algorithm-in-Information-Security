def ExtendedEuclide(a, b):
    if a == 0:
        return b, 0, 1
    d, x, y = ExtendedEuclide(b % a, a)
    return d, y - (b // a) * x, x


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    d, x, y = ExtendedEuclide(a, b)
    print("Kết quả thuật toán Euclide mở rộng là: ")
    print(f"GCD({a}, {b}) = {d}")
    print(f"{a}^-1 mod {b} = {x}")
    print(f"{b}^-1 mod {a} = {y}")


if __name__ == "__main__":
    main()
