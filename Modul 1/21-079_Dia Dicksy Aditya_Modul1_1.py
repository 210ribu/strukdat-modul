def stack ():
    s=[]
    return (s)
def push(s,data):
    s.append(data)
def pop(s):
    data=s.pop()
    return(data)
def peek(s):
    return(s[len(s)-1])
def isEmpty(s):
    return (s==[])
def size(s):
    return(len(s))


#tumpukan = [1,2,3,4,5,6,7]
st=stack()
stop=False
while not(stop):
    print("Menghitung Tumpukan Batu Bata sebanyak 7 buah")
    print("1.Menambah Tumpukkan Batu Bata")
    print("2.Menghilangkan Tumpukan Batu Bata")
    print("3.Menampilkan Data Batu Bata")
    print("4.Mengecek Apakah Tumpukan Batu Bata Tersebut Sudah Kosong")
    print("5.Mengecek Apakah Tumpukan Batu Batu Bata Tersebut Sudah Penuh")
    print("6.Menghapus Tumpukan Batu Bata")
    opsi=str(input(("Masukkan menu yang anda ingin pilih :")))
   
    
    if opsi=="1":
        new =int(input("Masukkan Bata Ke-: "))
        for i in range (new):
            push(st, new)
            print("Bata ", st, " Sudah ditambahkan")
    elif opsi=="2":
         new= pop(st)
         print("Menghapus Bata Dengan Nilai",new)
         print(st)
    elif opsi=="3":
        for i in st:
            print("Menampilkan Urutan Bata: ", i)   
    elif opsi=="4":
        if isEmpty(st):
            print("Belum Terisi Bata")
        else:
            print("Masih Terisi Bata")
    elif opsi=="5":
        if size(st)==7:
            print("Sudah Penuh")
        else:
            print("Belum Penuh")
    elif opsi=="6":
        for i in range(size(st)):
            pop(st)
        print("Semua Bata Telah Terhapus")
    else:
        break