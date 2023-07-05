def sequentialSearch(data, item):
    indexFind = []
    x = 0
    y = 0
    while x < len(data):
        if data[x] == item:
            indexFind.append(x)
            x += 1
        else:
            x += 1
        y += 1
    if len(indexFind) == 0:
        return ["Data tidak ada", y]

    return [indexFind, y]

a = [1, 5, 9, 8, 1, 5, 10, 26, 5, 12]
[hasil, jumlahIterasi] = sequentialSearch(a, 0)
print(f'Posisi data= {hasil}' )
print(f'Jumlah Iterasi= {jumlahIterasi}')