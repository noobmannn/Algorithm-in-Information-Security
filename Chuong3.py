# Đối Sánh Mẫu theo thuật toán Boyer_Moore
def lastOccur(p, c):
    i = len(p) - 1
    while i >= 0:
        if p[i] == c:
            return i
        i = i - 1
    return -1


def boyerMooreSearch(T, P):
    i = len(P) - 1
    j = len(P) - 1
    while i <= len(T) - 1:
        if T[i] == P[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i = i + len(P) - min(j, 1 + lastOccur(P, T[i]))
            j = len(P) - 1
    return -1


# Đối Sánh Mẫu theo thuật toán KMP (Knuth-Morris-Pratt)
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
    # Đối Sánh Mẫu theo thuật toán Boyer_Moore
    print(boyerMooreSearch("rippleapple.", "apple"))
    print(boyerMooreSearch("appstoreapple.", "apple"))
    print()
    # Đối Sánh Mẫu theo thuật toán KMP (Knuth-Morris-Pratt)
    print(KMPSearch("appstoreapple", "apple"))
    print(KMPSearch("ABAAABCD", "ABC"))
    print(KMPSearch("rippleapple.", "apple"))
    print()


if __name__ == "__main__":
    main()
