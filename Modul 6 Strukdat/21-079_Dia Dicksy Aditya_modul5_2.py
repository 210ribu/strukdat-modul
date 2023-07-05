def ordSequenSearch(data, element):
    x = 0
    y = False
    posIndex = []
    while x < len(data) and not(y):
        if data[x] == element:
            posIndex.append(x)
            x += 1
        else:
            if data[x] > element:
                y = True
                x += 1
            else:
                x += 1
    
    if len(posIndex) == 0:
        return ['Data tidak ada', x]

    return [posIndex, x]

a = [1, 1, 5, 5, 5, 8, 9, 10, 12, 26]
[hasil, iterasi] = ordSequenSearch(a, 0)
print(f'Posisi data= {hasil}')
print(f'Jumlah Iterasi= {iterasi}')

