def truycapphantu(tupledata):
    firstelement = tupledata[0]
    lastelement = tupledata[1]
    return firstelement, lastelement

inputtuple = eval(input("Nhap tuple "))
first, last = truycapphantu(inputtuple)

print("phan tu dau tien", first)
print("phan tu cuoi cung", last)