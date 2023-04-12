def failureFunc(P):
    lps = [0] * len(P)
    lps[0] = 0
    i = 1
    ln = 0
    while i < len(P):
        if P[i] == P[ln]:
            ln += 1
            lps[i] = ln
            i += 1
        else:
            if ln != 0:
                ln = lps[ln - 1]
            else:
                lps[i] = ln
                i += 1
    lps.insert(0, -1)
    return lps


def KMPSearch(T, P):
    i = 0
    j = 0
    F = failureFunc(P)
    while i <= len(T) - 1:
        if T[i] == P[j]:
            i += 1
            j += 1
            if j == len(P):
                return i - j
        else:
            i = i + j - F[j]
            if F[j] != -1:
                j = F[j]
            else:
                j = 0
    return -1


def main():
    T = input("Nhập chuỗi T: ")
    P = input("Nhập chuỗi P: ")
    if KMPSearch(T, P) != -1:
        print(f"Vị trí xuất hiện của chuỗi \"{P}\" trong chuỗi \"{T}\" là: {KMPSearch(T, P)}")
    else:
        print(f"Chuỗi \"{P}\" không nằm trong chuỗi \"{T}\"!")


if __name__ == "__main__":
    main()
