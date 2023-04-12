def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True


def backtrack(n, m, primes, curr, result):
    if n == 0 and m == 0:
        if check_duplicates(curr):
            result.append(curr)
        return
    if n < 0 or m == 0:
        return
    for i in range(len(primes)):
        backtrack(n - primes[i], m - 1, primes[i + 1:], curr + [primes[i]], result)


def prime_sum(n, m):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    result = []
    backtrack(n, m, primes, [], result)
    return result


def main():
    n = int(input("Nhập giá trị của N (1 <= N <= 10000): "))
    m = int(input("Nhập giá trị của M (2 <= M <= 100): "))
    result = prime_sum(n, m)
    if len(result) == 0:
        print(f"Không thể phân tích {n} thành tổng của {m} số nguyên tố.")
    else:
        print(f"Tất cả các cách có thể dể phân tích {n} thành tổng của {m} số nguyên tố khác nhau là:")
        for r in result:
            print(r)


if __name__ == "__main__":
    main()

"""
Giải thích về các hàm và thuật toán:
- Hàm is_prime(n) kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
- Hàm backtrack(n, m, primes, curr, result) sử dụng thuật toán quay lui để tìm cách phân
  tích số n thành tổng của m số nguyên tố. primes là danh sách các số nguyên tố đã được tìm
  thấy trong khoảng từ 2 đến n, curr là danh sách chứa các số nguyên tố đã được chọn cho
  cách phân tích hiện tại và result là danh sách chứa các cách phân tích hợp lệ.
- Trong hàm backtrack(), nếu n bằng 0 và m bằng 0, tức là đã tìm được một cách phân tích hợp lệ,
  thì danh sách curr được thêm vào danh sách result.
- Nếu n âm hoặc m bằng 0, thì cách phân tích hiện tại không hợp lệ và thuật toán tiếp tục tìm kiếm các cách phân tích khác.
- Với mỗi số nguyên tố p trong danh sách primes,
  ta đệ quy gọi hàm backtrack() với các tham số n-p, m-1, primes[i:] (danh sách các số nguyên tố lớn hơn hoặc bằng p), curr + [p] 
  (danh sách các số nguyên t)
"""
