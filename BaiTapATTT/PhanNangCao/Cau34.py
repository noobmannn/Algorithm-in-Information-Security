import random


def convertDecToReverseBin(n):
    binaryList = []
    while n > 0:
        binaryList.append(n % 2)
        n = int(n / 2)
    return binaryList


def ExponentialSquaring(a, k, n):
    A = a
    b = 1
    kList = convertDecToReverseBin(k)
    if kList[0] == 1:
        b = a
    for i in range(1, len(kList)):
        A = (A * A) % n
        if kList[i] == 1:
            b = (A * b) % n
    return b
    # return a^k%n


# Kiểm tra số nguyên tố theo thuật toán Fermat
def FermatCheckPrimeNumber(n, t):
    for i in range(t):
        a = random.randint(2, n - 2)
        r = ExponentialSquaring(a, n - 1, n)
        if r != 1:
            return False
    return True


'''
- Thuật toán sẽ cho kết quả sai khi giá trị n đưa vào là 1 hợp số Carmichael 
  hoặc giá trị a lấy ngẫu nhiên là một giá trị đánh lừa cho tính nguyên tố của n
  Vd: 341 với cơ sở a = 2 nhưng 341 không phải là số Carmichael
- Số Carmichael n là một hợp số nguyên thỏa mãn a^(n-1) đồng dư 1 theo mod n với
  tất cả các số nguyên a thỏa mãn (a, n) = 1
  Vd: 561, 1105, 1729
'''


def main():
    while True:
        n = int(input("Nhập N: "))
        t = int(input("Nhập số lần thử T: "))
        if t > 0:
            break
        else:
            print("Vui lòng nhập N > 0 và T > 0!!!")
    if FermatCheckPrimeNumber(n, t):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")


if __name__ == "__main__":
    main()
