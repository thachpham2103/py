import pandas as pd

def nhap_cong_nhan():
    n = int(input("Nhập số công nhân: "))
    ds = []

    for i in range(n):
        print(f"\nNhập công nhân thứ {i+1}:")
        ma = input("Mã công nhân: ")
        ho_ten = input("Họ tên: ")
        luong_ngay = float(input("Lương ngày: "))
        so_ngay_cong = int(input("Số ngày công: "))
        phu_cap = float(input("Phụ cấp: "))

        tong_luong = luong_ngay * so_ngay_cong + phu_cap
        ds.append([ma, ho_ten, luong_ngay, so_ngay_cong, phu_cap, tong_luong])

    return pd.DataFrame(
        ds,
        columns=["Mã CN", "Họ tên", "Lương/ngày", "Ngày công", "Phụ cấp", "Tổng lương"]
    )


def ghi_csv(df, ten_file="cong_nhan.csv"):
    df.to_csv(ten_file, index=False, encoding="utf-8-sig")


def doc_csv(ten_file="cong_nhan.csv"):
    return pd.read_csv(ten_file)

def xu_ly(df):
    print("\nDANH SÁCH CÔNG NHÂN:")
    print(df)

    cn_max = df.loc[df["Tổng lương"].idxmax()]
    print("\nCông nhân có lương cao nhất:")
    print(cn_max)

    dem = (df["Tổng lương"] >= 10).sum()
    print("\nSố công nhân có lương ≥ 10 triệu:", dem)


def main():
    df = nhap_cong_nhan()
    ghi_csv(df)
    df2 = doc_csv()
    xu_ly(df2)


if __name__ == "__main__":
    main()
