def daonguoclist(lst):
    return lst[::-1]

nhapchuoi = input("Nhap danh sach cac so ")
numbers = list(map(int, nhapchuoi.split(',')))

listdaonguoc = daonguoclist(numbers)
print("list sau khi dao nguoc: ", listdaonguoc)