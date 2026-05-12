def taotupletolist(lst):
    return tuple(lst)

nhapchuoi = input("Nhap chuoi ")
numbers = list(map(int, nhapchuoi.split(',')))

mytuple = taotupletolist(numbers)
print("list: ", numbers)
print("tuple to list: ", mytuple)