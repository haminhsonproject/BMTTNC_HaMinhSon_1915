from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if(self.soluongSinhVien() > 0):
            maxID = self.listSinhVien[0].MaSV
            for sv in self.listSinhVien:
                if(sv.MaSV > maxID):
                    maxID = sv.MaSV
            maxID += 1
        return maxID

    def soluongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        MaSV = self.generateID()
        HoTen = input("Nhap ho ten: ")
        GioiTinh = input("Nhap gioi tinh: ")
        ChuyenNganh = input("Nhap chuyen nganh: ")
        DiemTB = float(input("Nhap diem trung binh: "))
        sv = SinhVien(MaSV, HoTen, GioiTinh, ChuyenNganh, DiemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, MaSV):
        for sv in self.listSinhVien:
            if(sv.MaSV == MaSV):
                HoTen = input("Nhap ho ten: ")
                GioiTinh = input("Nhap gioi tinh: ")
                ChuyenNganh = input("Nhap chuyen nganh: ")
                DiemTB = float(input("Nhap diem trung binh: "))
                sv.HoTen = HoTen
                sv.GioiTinh = GioiTinh
                sv.ChuyenNganh = ChuyenNganh
                sv.DiemTB = DiemTB
                self.xepLoaiHocLuc(sv)
            else:
                print("Khong tim thay sinh vien co ma so: " + str(MaSV))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda sv: sv.MaSV, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv.HoTen, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda sv: sv.DiemTB, reverse=False)

    def findByID(self, MaSV):
        serchResult = []
        for sv in self.listSinhVien:
            if(sv.MaSV == MaSV):
                serchResult.append(sv)
        return serchResult
    
    def findByName(self, HoTen):
        listSV = []
        for sv in self.listSinhVien:
            if(sv.HoTen == HoTen):
                listSV.append(sv)
        return listSV
    
    def deleteById(self, MaSV):
        isDelete = False
        sv = self.findByID(MaSV)
        if(sv!=None):
            self.listSinhVien.remove(sv[0])
            isDelete = True
        return isDelete
    
    def xepLoaiHocLuc(self, sv):
        if(sv.DiemTB >= 8):
            sv.HocLuc = "Gioi"
        elif(sv.DiemTB >= 6.5):
            sv.HocLuc = "Kha"
        elif(sv.DiemTB >= 5):
            sv.HocLuc = "Trung Binh"
        else:
            sv.HocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                .format("MaSV", "HoTen", "GioiTinh", "ChuyenNganh", "DiemTB", "HocLuc"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                    .format(sv.MaSV, sv.HoTen, sv.GioiTinh, sv.ChuyenNganh, sv.DiemTB, sv.HocLuc))
                
                print("\n")

    def getListSinhVien(self):
        return self.listSinhVien    