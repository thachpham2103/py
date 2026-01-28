
def nhap():
    n = int(input("Nhập vào số lượng công nhân: "))
    ds_cn = []

    for i in range(n):
        print(f"\nNhập thông tin cho công nhân thứ {i+1}")
        ma = input("Nhập vào mã công nhân: ")
        hoTen = input("Nhập vào họ tên công nhân: ")
        tuoi = int(input("Nhập vào tuổi công nhân: "))
        luongCB = float(input("Nhập vào lương cơ bản: "))
        diemTb= int(input("Nhập vào điểm tb"))

        # mỗi công nhân là 1 list
        ds_cn.append([ma, hoTen, tuoi, luongCB, diemTb])

    return ds_cn

def hien_thi(a):
    print("\n---------------- THÔNG TIN CÔNG NHÂN ----------------")
    print("{:<10} | {:<15} | {:<10} | {:<10} | {:<10}".format(
        "ID", "HoTen", "Tuoi", "LuongCB", "Điểm TB"))
    print("-" * 55)

    for cn in a:
        print("{:<10} | {:<15} | {:<10} | {:<10} | {:<15}".format(
            cn[0], cn[1], cn[2], cn[3], cn[4]))


def tim_max(a):
    diem_tb = a[0][4]   # lấy phần tử thứ 3 của công nhân đầu tiên 

    for cn in a:
        if cn[4] > diem_tb:
            diem_tb = cn[4]

    return diem_tb

def search_thong_tin(a):
    found = False
    for cn in a:
        if 0 <= cn[3] <= 150000:
            print("Công nhân hợp lệ:", cn)
            found = True

    if not found:
        print("Không tìm thấy công nhân phù hợp")

def main():
    cn = nhap()
    hien_thi(cn)

    diem_tb = tim_max(cn)
    print("\nLương cơ bản lớn nhất:", diem_tb)

    print("\n--- Công nhân có lương cơ bản lớn nhất ---")
    for c in cn:
        if c[4] == diem_tb:
            print(c)
    
    search_thong_tin(cn)

# ---------------------------------
if __name__ == "__main__":
    main()
