import pandas as pd

def tao_dataframe():
    data = {
        "MaSV":  ["SV01", "SV02", "SV03", "SV04", "SV05"],
        "HoTen": ["An",   "Bình", "Chi",  "Dũng", "Hà"],
        "Tuoi":  [19,     20,     21,     19,     22],
        "DiemTB":[7.5,    8.2,    6.0,    9.0,    6.8]
    }
    df = pd.DataFrame(data)
    return df

def truy_xuat(df):
    print("\n--- Toàn bộ danh sách sinh viên ---")
    print(df)

    # print("\n--- Chỉ cột Họ tên và Điểm TB ---")
    # print(df[["HoTen", "DiemTB"]])

    # print("\n--- Thông tin sinh viên ở dòng thứ 2 (index = 1) ---")
    # print(df.iloc[1])

def them_cot_xeploai(df):
    def xep_loai(diem):
        if diem >= 8.0:
            return "Giỏi"
        elif diem >= 6.5:
            return "Khá"
        else:
            return "Trung bình"

    df["XepLoai"] = df["DiemTB"].apply(xep_loai)

    print("\n--- Sau khi thêm cột XepLoai ---")
    print(df)
    return df

def loc_sinh_vien(df):
    dk = (df["DiemTB"] >= 7.0) & (df["Tuoi"] >= 20)
    df_loc = df.loc[dk]

    print("\n--- Sinh viên có DiemTB >= 7.0 và Tuoi >= 20 ---")
    print(df_loc)
    return df_loc

def xoa_du_lieu(df):
    # Xóa sinh viên có MaSV = "SV03"
    df_xoa_sv = df[df["Tuoi"] != "SV03"]

    print("\n--- Sau khi xóa sinh viên MaSV = 'SV03' ---")
    print(df_xoa_sv)
    return df_xoa_sv

    # Xóa cột Tuoi
    # df_xoa_cot = df_xoa_sv.drop(columns=["Tuoi"])

    # print("\n--- Sau khi xóa cột Tuoi ---")
    # print(df_xoa_cot)

    # return df_xoa_cot

def sap_xep_theo_diem(df):
    df_sorted = df.sort_values(by="DiemTB", ascending=False)

    print("\n--- Sinh viên sắp xếp theo DiemTB giảm dần ---")
    print(df_sorted)

    return df_sorted

def ghi_file_csv(df, ten_file):
    df.to_csv(ten_file, index=False, encoding="utf-8-sig")
    print(f"\nĐã ghi dữ liệu ra file: {ten_file}")

def main():
   
    df = tao_dataframe()
    truy_xuat(df)
    df = them_cot_xeploai(df)
    df_loc = loc_sinh_vien(df)
    df_sap_xep = sap_xep_theo_diem(df)
    df_sau_xoa = xoa_du_lieu(df_sap_xep)
    ghi_file_csv(df_sau_xoa, "SINHVIEN.csv")

if __name__ == "__main__":
    main()