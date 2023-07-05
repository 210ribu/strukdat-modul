# Program python untuk menentukan bilangan prima atau tidak
# Meminta input bilangan dari user
x = int(input("Masukkan bilangan: "))
# bilangan prima harus lebih besar dari 1
if x > 1:
    for i in range(2,x):
        if (x % i) == 0:
            print(x, "bukan bilangan prima")
            print(i, "kali", x//i, "=", x)
            break
    else:
        print(x,"adalah bilangan prima")
# bila bilangan kurang atau sama dengan satu
else:
    print(x, "bukan bilangan prima")