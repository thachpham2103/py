import csv

def nhap_sp():
    a = {}
    n = int(input("Số SP: "))
    for _ in range(n):
        a[input("Mã SP: ")] = int(input("Số lượng: "))
    return a

def nhap_loai():
    b = {}
    m = int(input("Số loại SP: "))
    for _ in range(m):
        b[input("Mã loại: ")] = input("Tên loại: ")
    return b

def check_sp(a):
    ma = input("Mã SP cần kiểm tra: ")
    a[ma] = 100 if ma in a else 50
    return a


def xoa_sl_0(a):
    return {k: v for k, v in a.items() if v != 0}


def ghi_csv(a, b):
    with open("san_pham.csv", "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerows([["MaSP", "SoLuong"]] + list(a.items()))

    with open("loai_sp.csv", "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerows([["MaLoai", "TenLoai"]] + list(b.items()))


def doc_csv():
    a, b = {}, {}
    with open("san_pham.csv", encoding="utf-8-sig") as f:
        for i, r in enumerate(csv.reader(f)):
            if i > 0: a[r[0]] = int(r[1])

    with open("loai_sp.csv", encoding="utf-8-sig") as f:
        for i, r in enumerate(csv.reader(f)):
            if i > 0: b[r[0]] = r[1]
    return a, b


def main():
    a = nhap_sp()
    b = nhap_loai()

    a = check_sp(a)
    a = xoa_sl_0(a)

    ghi_csv(a, b)
    a, b = doc_csv()

    print("\nSẢN PHẨM:", a)
    print("LOẠI SP:", b)

if __name__ == "__main__":
    main()