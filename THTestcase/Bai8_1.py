def ExtendedEuclide(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = ExtendedEuclide(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def ModularInverse(a, p):
    d, x, y = ExtendedEuclide(a, p)
    if d != 1:
        return -1
    else:
        return x


def main():
    p = int(input("Nhập P: "))
    a = int(input("Nhập A: "))
    print(f"Nghịch đảo của {a} trên Fp với p = {p} là: {ModularInverse(p, a)}")


if __name__ == "__main__":
    main()
