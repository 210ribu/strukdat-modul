def ganjilGenapSort(data):
    print(f'Data= {data}')
    for x in range(len(data)):
        if x % 2 == 0:
            for j in range(0, len(data), 2):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        else:
            for j in range(1, len(data)-1, 2):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        print(f'Genap-Ganjil Sorting \n{data}')

    return data

def modifiedSelection(data):
    for x in range(len(data)//2):
        maxIndex = x
        minIndex = x
        iter = x+1

        print(f'Iterasi ke- {x+1}')
        for j in range(x, len(data)):
            if data[minIndex] > data[j]:
                minIndex = j 
        
        data[x], data[minIndex] = data[minIndex], data[x]
        print(f'urut data minimal \t: {data}')

        for y in range(len(data)-iter, x, -1):
            if data[maxIndex] < data[y]:
                maxIndex = y
        
        data[len(data)-iter], data[maxIndex] = data[maxIndex], data[len(data)-iter]
        print(f'urut data maksimal \t: {data}')
        
    return data

a = [13, 12, 10, 8, 7, 5, 11, 2]
b = [10, 2, 5, 8, 1, 20, 7, 12, 4]
print(ganjilGenapSort(a))
print(f'Data Urut= {modifiedSelection(b)}')