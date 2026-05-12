def tinhtongsochan(lst):
    tong= 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

nhapchuoi = input("Nhap chuoi ")
numbers = list(map(int, nhapchuoi.split(',')))

tongchan = tinhtongsochan(numbers)
print("tong chan la: ", tongchan)