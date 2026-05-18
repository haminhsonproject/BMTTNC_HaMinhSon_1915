from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1):
    print("1. Nhap sinh vien")
    print("2. Cap nhat thong tin sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien theo ho ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")


    choose = int(input("Nhap lua chon: "))
    if(choose == 1):
        qlsv.nhapSinhVien()
        print("Nhap sinh vien thanh cong")
    elif(choose == 2):
        if(qlsv.soluongSinhVien() > 0):
            MaSV = int(input("Nhap ma so sinh vien can cap nhat: "))
            qlsv.updateSinhVien(MaSV)
        else:
            print("Khong co sinh vien de cap nhat")
    elif(choose == 3):
        if(qlsv.soluongSinhVien() > 0):
            MaSV = int(input("Nhap ma so sinh vien can xoa: "))
            if(qlsv.deleteById(MaSV)):
                print("Xoa sinh vien thanh cong")
            else:
                print("Khong tim thay sinh vien de xoa")
        else:
            print("Khong co sinh vien de xoa")
    elif(choose == 4):
        if(qlsv.soluongSinhVien() > 0):
            HoTen = input("Nhap ho ten sinh vien can tim kiem: ")
            searchResult = qlsv.findByName(HoTen)
            for sv in searchResult:
                print(sv.MaSV, sv.HoTen, sv.GioiTinh, sv.ChuyenNganh, sv.DiemTB, sv.HocLuc)
        else:
            print("Khong co sinh vien de tim kiem")
    elif(choose == 5):
        if(qlsv.soluongSinhVien() > 0):
            qlsv.sortByDiemTB()
            for sv in qlsv.listSinhVien:
                print(sv.MaSV, sv.HoTen, sv.GioiTinh, sv.ChuyenNganh, sv.DiemTB, sv.HocLuc)
        else:
            print("Khong co sinh vien de sap xep")
    elif(choose == 6):
        if(qlsv.soluongSinhVien() > 0):
            qlsv.sortByChuyenNganh()
            for sv in qlsv.listSinhVien:
                print(sv.MaSV, sv.HoTen, sv.GioiTinh, sv.ChuyenNganh, sv.DiemTB, sv.HocLuc)
        else:
            print("Khong co sinh vien de sap xep")
    elif(choose == 7):
        qlsv.showSinhVien(qlsv.getListSinhVien())