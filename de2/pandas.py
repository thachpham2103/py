import pandas as pd

def nhap_san_pham():
    n = int(input("Nhập số lượng sản phẩm: "))
    ds = []
    for i in range(n):
        print(f"\nSản phẩm thứ {i+1}:")
        maSP = input("Nhập mã SP: ")
        soLuong = int(input("Nhập số lượng: "))
        ds.append([maSP, soLuong])

    return pd.DataFrame(ds, columns=["Mã SP", "Số lượng"])

def nhap_loai_san_pham():
    m = int(input("Nhập số lượng loại sản phẩm: "))
    ds = []
    for i in range(m):
        print(f"\nLoại sản phẩm thứ {i+1}:")
        maLoai = input("Nhập mã loại SP: ")
        tenLoai = input("Nhập tên loại SP: ")
        ds.append([maLoai, tenLoai])

    return pd.DataFrame(ds, columns=["Mã loại SP", "Tên loại SP"])

def xuat(df_sp, df_loai):
    print("\n------ THÔNG TIN SẢN PHẨM ------")
    print(df_sp)

    print("\n------ THÔNG TIN LOẠI SẢN PHẨM ------")
    print(df_loai)

def check_sp(df_sp):
    ma = input("\nNhập mã SP cần kiểm tra: ")

    if ma in df_sp["Mã SP"].values:
        df_sp.loc[df_sp["Mã SP"] == ma, "Số lượng"] = 100
    else:
        df_sp.loc[len(df_sp)] = [ma, 50]

    return df_sp

def delete_sp_so_luong_0(df_sp):
    return df_sp[df_sp["Số lượng"] != 0]

def chuyen_sang_list(df_sp):
    return df_sp["Mã SP"].tolist(), df_sp["Số lượng"].tolist()

def ghi_csv(df_sp, df_loai):
    df_sp.to_csv("san_pham.csv", index=False, encoding="utf-8-sig")
    df_loai.to_csv("loai_san_pham.csv", index=False, encoding="utf-8-sig")

def doc_csv():
    df_sp = pd.read_csv("san_pham.csv")
    df_loai = pd.read_csv("loai_san_pham.csv")
    return df_sp, df_loai

def main():
    df_sp = nhap_san_pham()
    df_loai = nhap_loai_san_pham()

    xuat(df_sp, df_loai)

    df_sp = check_sp(df_sp)
    print("\nSau khi kiểm tra mã SP:")
    xuat(df_sp, df_loai)

    df_sp = delete_sp_so_luong_0(df_sp)
    print("\nSau khi xóa sản phẩm có số lượng = 0:")
    xuat(df_sp, df_loai)

    ghi_csv(df_sp, df_loai)
    print("\n Đã ghi dữ liệu ra file CSV")

    df_sp, df_loai = doc_csv()
    print("\n Dữ liệu đọc lại từ file CSV:")
    xuat(df_sp, df_loai)

    ma, sl = chuyen_sang_list(df_sp)
    print("\nChuyển DataFrame sang list:")
    print("Mã SP:", ma)
    print("Số lượng:", sl)

if __name__ == "__main__":
    main()
