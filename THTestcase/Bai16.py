def completeSearching(T, P):
    listRes = []
    for i in range(len(T)):
        flag = True
        for j in range(len(P)):
            if i + j < len(T):
                if P[j] != T[i + j]:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            listRes.append(i)
    return listRes


def stringResult(listRes):
    s = ""
    for i in listRes:
        s += str(i) + " "
    return s


def main():
    T = input("Nhập chuỗi T: ")
    P = input("Nhập chuỗi P: ")
    listRes = completeSearching(T, P)
    if len(listRes) != 0:
        print(f"Vị trí xuất hiện của chuỗi \"{P}\" trong chuỗi \"{T}\" là: " + stringResult(listRes))
    else:
        print(f"Chuỗi \"{P}\" không nằm trong chuỗi \"{T}\"!")


if __name__ == "__main__":
    main()
