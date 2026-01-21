import csv

def nhap_thong_tin():
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    a = []
    for i in range(n):
        print(f'\nNhập phần tử thứ {i+1}:')
        id = input("Nhập mã công nhân: ")
        hoTen = input("Nhập họ tên công nhân: ")
        luongNgay = float(input("Nhập lương ngày: "))
        soNgayCong = int(input("Nhập số ngày công: "))
        phuCap = float(input("Nhập phụ cấp: "))

        tong_luong = luongNgay * soNgayCong + phuCap
        a.append([id, hoTen, luongNgay, soNgayCong, phuCap, tong_luong])
    return a


def xuat(a):
    print("\n------------------------------- THÔNG TIN CÔNG NHÂN -----------------------------------------")
    print("{:<10}|{:<25}|{:>12}|{:>12}|{:>12}|{:>15}".format(
        "ID", "Họ tên", "Lương/ngày", "Ngày công", "Phụ cấp", "Tổng lương"
    ))
    print("-" * 90)

    for cn in a:
        print("{:<10}|{:<25}|{:>12.2f}|{:>12}|{:>12.2f}|{:>15.2f}".format(
            cn[0], cn[1], cn[2], cn[3], cn[4], cn[5]
        ))

def timMax(a):
    max_cn = a[0]
    for cn in a:
        if cn[5] > max_cn[5]:
            max_cn = cn
    return max_cn


def count(a):
    dem = 0
    for cn in a:
        if cn[5] >= 10:
            dem += 1
    return dem

# def ghi_file(a):
#     with open("congnhan.csv", "w", newline="", encoding="utf-8-sig") as f:
#         writer = csv.writer(f)
#         writer.writerow(["ID", "HoTen", "LuongNgay", "SoNgayCong", "PhuCap", "TongLuong"])
#         writer.writerows(a)

# def doc_file():
#     a = []
#     with open("congnhan.csv", encoding="utf-8-sig") as f:
#         reader = csv.reader(f)
#         next(reader)
#         for r in reader:
#             a.append([
#                 r[0], r[1],
#                 float(r[2]), int(r[3]),
#                 float(r[4]), float(r[5])
#             ])
#     return a


def main():
    a = nhap_thong_tin()
    xuat(a)

    # ghi_file(a)
    # print("\nĐã ghi dữ liệu ra file congnhan.csv")

    # a = doc_file()
    # print("\nDữ liệu đọc lại từ file:")
    # xuat(a)

    cn_max = timMax(a)
    print("\nCông nhân có lương cao nhất:")
    print(f"- {cn_max[1]} | Tổng lương: {cn_max[5]:,.0f} VNĐ")

    d = count(a)
    print(f"\nSố công nhân có lương từ 10 triệu trở lên: {d}")


if __name__ == "__main__":
    main()
