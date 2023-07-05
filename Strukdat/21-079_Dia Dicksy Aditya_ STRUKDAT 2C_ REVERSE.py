#Buat function untuk ’reverse word’ dengan menggunakan konsep stacks, misalkan kata ’stacks’
#menjadi ’skcats’

def reverse(a): 
    str = "" 
    for i in a: 
        str = i + str 
    return str 

a = "stacks" 
print ("String awal : ",end="") 
print (a) 

print ("String yang sudah dibalik : ",end="") 
print (reverse(a)) 