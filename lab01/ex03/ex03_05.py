def demsolanxuathien(lst):
    countdict = {}
    for item in lst:
        if item in countdict:
            countdict[item] += 1
        else:
            countdict[item] = 1
    return countdict

inputstring = input("Nhap chuoi ")
wordlist = inputstring.split()

solanxuathien = demsolanxuathien(wordlist)
print("so lan xuat hien ", solanxuathien)