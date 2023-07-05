def stack():
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
    return(s==[])
def size(s):
    return(len(s))
def dec2bin(num):
    st=stack()
    divNum=num
    while divNum>0:
        push(st,divNum%2)
        divNum=divNum//2
    temp=''
    while not(isEmpty(st)):
        temp=temp+str(pop(st))
    return temp
print(dec2bin(8))