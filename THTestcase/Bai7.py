def EuclideForFindGCD(a, b):
    if a == 0:
        return b
    return EuclideForFindGCD(b % a, a)


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    print("Kết quả thuật toán Euclide là: ")
    print(f"GCD({a}, {b}) = {EuclideForFindGCD(a, b)}")


if __name__ == "__main__":
    main()
