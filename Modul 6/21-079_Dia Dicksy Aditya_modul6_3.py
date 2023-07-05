def binarySearch(data, item):
    pertama = 0
    terakhir = len(data)-1
    # found = Salah
    listFound = []
    iter = 0
    
    while pertama <= terakhir:
        midpoint = (pertama + terakhir) // 2
        if data[midpoint] == item:
            # found = Benar
            listFound.append(midpoint)
            if item < data[midpoint+1]:
                terakhir = midpoint - 1
            else:
                pertama = midpoint + 1
        else:
            if item < data[midpoint]:
                terakhir = midpoint -1
            else:
                pertama = midpoint + 1
        iter += 1

    if len(listFound) == 0:
        return ["Data tidak ada", iter]

    return [listFound, iter]


a = [1, 1, 5, 5, 5, 8, 9, 10, 12, 26]
[hasil, iterasi]=binarySearch(a, 10)
# print(binSearch(a, 1))
print(f'Posisi data= {hasil}')
print(f'Jumlah Iterasi= {iterasi}')


