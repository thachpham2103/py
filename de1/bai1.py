def nhap_thong_tin():
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    a = list()
    for i in range(n):
        print(f'\nNhập phần tử thứ {i+1}:')
        id = input("Nhập mã công nhân: ")
        hoTen = input("Nhập họ tên công nhân: ")
        luongNgay = float(input("Nhập lương ngày: "))
        soNgayCong = int(input("Nhập số ngày công: "))
        phuCap = float(input("Nhập phụ cấp: "))

        luong_co_ban = luongNgay * soNgayCong
        tong_luong = luong_co_ban + phuCap

        a.append([id, hoTen, luongNgay, soNgayCong, phuCap, tong_luong])
    return a


def xuat(a):
    print("\n------------------------------- THÔNG TIN CÔNG NHÂN -----------------------------------------")

    print("{:<10}|{:<25}|{:>12}|{:>12}|{:>12}|{:>15}".format(
        "ID", "Họ tên", "ngày", "Ngày công", "Phụ cấp", "Tổng lương"
    ))
    print("-" * 90)

    for cn in a:
        print("{:<10}|{:<25}|{:>12.2f}|{:>12}|{:>12.2f}|{:>15.2f}".format(
            cn[0], cn[1], cn[2], cn[3], cn[4], cn[5]
        ))


def timMax(a):
    congnhan_max = a[0]
    for cn in a:
        if cn[5] > congnhan_max[5]:
            congnhan_max = cn
    return congnhan_max


def count(a):
    dem = 0
    for cn in a:
        if cn[5] >= 10: 
            dem += 1
    return dem


def main():
    a = nhap_thong_tin()
    xuat(a)

    cn_max = timMax(a)
    print("\nCông nhân có lương cao nhất:")
    print(f"- {cn_max[1]} | Tổng lương: {cn_max[5]:,.0f} VNĐ")

    d = count(a)
    print(f"\nSố công nhân có lương từ 10 triệu trở lên: {d}")


if __name__ == "__main__":
    main()

