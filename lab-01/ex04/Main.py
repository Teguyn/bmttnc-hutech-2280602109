from SinhVien import SinhVien
from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\n========== CHUONG TRINH QUAN LY SINH VIEN ==========")
    print("**  1. Them sinh vien.                              **")
    print("**  2. Xuat danh sach sinh vien.                    **")
    print("**  3. Tinh diem trung binh.                        **")
    print("**  4. Xep loai hoc luc sinh vien.                  **")
    print("**  5. Tim sinh vien gioi.                          **")
    print("**  6. Sap xep sinh vien theo diem trung binh.      **")
    print("**  7. Sap xep sinh vien theo ten.                  **")
    print("**  8. Hien thi sinh vien theo hoc luc.             **")
    print("**  0. Thoat.                                       **")
    print("=====================================================")

    key = int(input("Nhap tuy chon: "))
    if key == 1:
        print("\n1. Them sinh vien.")
        maSo = input("Nhap ma so: ")
        hoTen = input("Nhap ho ten: ")
        diemToan = float(input("Nhap diem toan: "))
        diemLy = float(input("Nhap diem ly: "))
        diemHoa = float(input("Nhap diem hoa: "))
        sv = SinhVien(maSo, hoTen, diemToan, diemLy, diemHoa)
        qlsv.themSinhVien(sv)
    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Xuat danh sach sinh vien.")
            print(f"{'Ma so':<10}{'Ho ten':<25}{'Toan':<10}{'Ly':<10}{'Hoa':<10}{'Diem TB':<10}{'Hoc luc':<15}")
            qlsv.xuatDanhSachSinhVien()
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Tinh diem trung binh.")
            qlsv.tinhDiemTrungBinh()
            print("Da tinh xong diem trung binh.")
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Xep loai hoc luc sinh vien.")
            qlsv.xepLoaiHocLuc()
            print("Da xep loai hoc luc sinh vien.")
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Tim sinh vien gioi.")
            listGioi = qlsv.getSinhVienGioi()
            qlsv.showSinhVien(listGioi)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo diem trung binh.")
            qlsv.sapXepTheoDiemTrungBinh()
            qlsv.xuatDanhSachSinhVien()
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Sap xep sinh vien theo ten.")
            qlsv.sapXepTheoTen()
            qlsv.xuatDanhSachSinhVien()
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 8:
        if qlsv.soLuongSinhVien() > 0:
            print("\n8. Hien thi sinh vien theo hoc luc.")
            hocLuc = input("Nhap hoc luc can tim (Gioi, Kha, Trung binh, Yeu): ")
            listResult = qlsv.getSinhVienTheoHocLuc(hocLuc)
            qlsv.showSinhVien(listResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 0:
        print("\nTam biet!")
        break
    else:
        print("\nKhong hop le!")
