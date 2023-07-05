def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str 
    return str 

s = "stacks" 
print ("String awal : ",end="") 
print (s) 

print ("String yang sudah dibalik : ",end="") 
print (reverse(s)) 
