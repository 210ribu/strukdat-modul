
iter  = 0
banding = 0
geser = 0
def partitionD(array, start, end):
    global iter,banding,geser
    pivot = array[start]
    left = start + 1
    right = end
    while True:
        while left <= right and array[left] >= pivot:
            left = left + 1
            banding +=1
        while left <= right and array[right] <= pivot:
            right = right - 1
            banding +=1
        if right<left:
            break
        else:
            array[left], array[right] = array[right], array[left]
            geser +=1
    array[start], array[right] = array[right], array[start]
    geser +=1
    iter +=1
    print(f'Iterasi ke - {iter}\n{array} Pivot -> {pivot}')
    return right

def partitionA(array, start, end):
    global iter,banding,geser
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
            banding +=1
        while low <= high and array[low] <= pivot:
            low = low + 1
            banding +=1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            geser +=1
        else:
            break
    array[start], array[high] = array[high], array[start]
    geser +=1
    iter +=1
    print(f'Iterasi ke - {iter}\n{array} Pivot -> {pivot}')
    return high

def quick_sortA(array, start, end):
    if start < end:
        p = partitionA(array, start, end)
        quick_sortA(array, start, p-1)
        quick_sortA(array, p+1, end)
    return banding,geser
def quick_sortD(array, start, end):
    if start < end:
        p = partitionD(array, start, end)
        quick_sortD(array, start, p-1)
        quick_sortD(array, p+1, end)
    return banding,geser

# main
arr = [56,26,93,17,31,44]
n = len(arr)
[banding,geser]=quick_sortA(arr,0,n-1)
print(f"\nHasil Akhir = {arr}")
print(f"Total Perbandingan : {banding}")
print(f"Total Pergeseran : {geser}")

iterasi,banding,geser = 0,0,0
def merge_sortA(a_list):
    global iterasi,banding,geser
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sortA(left_half)
        merge_sortA(right_half)
        i,j,k = 0,0,0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
                geser +=1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
            banding +=1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    if len(a_list) >1:
        iterasi +=1
        print(f"iterasi ke - {iterasi}")
        print("Merging ", a_list)
    return geser,banding

def merge_sortD(a_list):
    global iterasi,banding,geser
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sortD(left_half)
        merge_sortD(right_half)
        i,j,k = 0,0,0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                a_list[k] = left_half[i]
                i += 1
                geser +=1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1
            banding +=1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
    if len(a_list) >1:
        iterasi +=1
        print(f"iterasi ke - {iterasi}")
        print("Merging ", a_list)
    return geser,banding


array = [56,26,93,17,31,44]
while True:
    inpt = int(input("Pilih Metode Pengurutan:\n1.Merge Sort\n2.Quick Sort\nPilih: "))
    if inpt==1:
        inpt2 =int(input("Pengurutan Secara:\n1. Ascending\n2. Descending\nPilih: "))
        if inpt2 == 1:
            [total_geser,total_banding] = merge_sortA(array)
            print(f'\nBanyaknya Perbandingan - {total_banding}')
            print(f'Banyaknya Pergeseran - {total_geser}')
        elif inpt2 ==2:
            [total_geser,total_banding] = merge_sortD(array)
            print(f'\nBanyaknya Perbandingan - {total_banding}')
            print(f'Banyaknya Pergeseran - {total_geser}')
        else:
            print("Maaf Inputan Tidak Valid!")
    elif inpt ==2:
        inpt2 =int(input("Pengurutan Secara:\n1. Ascending\n2. Descending\nPilih: "))
        if inpt2 ==1:
            n = len(array)
            [banding,geser]=quick_sortA(array,0,n-1)
            print(f"\nHasil Akhir = {array}")
            print(f"Total Perbandingan : {banding}")
            print(f"Total Pergeseran : {geser}")
        elif inpt2 == 2:
            n = len(array)
            [banding,geser]=quick_sortD(array,0,n-1)
            print(f"\nHasil Akhir = {array}")
            print(f"Total Perbandingan : {banding}")
            print(f"Total Pergeseran : {geser}")
        else:
            print("Maaf Inputan Tidak Valid!")
    else:
        print("Maaf Inputan Tidak Valid!")

    akhir = int(input("\nPilih\n1.Lagi\n2.Keluar\nPilih: "))
    if akhir ==1:
        pass
    else:
        break