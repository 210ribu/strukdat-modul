def check(strmat):
    parantheses={')':'(','}':'{',']':'['}
    buka=kurung.values()
    tutup=kurung.keys()
    temp=stack()
    matched=True
    for i in strmat:
        if i in buka:
            push(temp,i)
        if i in tutup:
            if isEmpty(temp):
                return 'kelebihan dari kurung tutup'
        else:
            temp1=pop(temp)
            if temp1==kurung[i]:
                matched=matched and True
            else:
                matched=matched and False
    if not(isEmpty(temp)):
    return 'kelebihan kurung buka'
    if matched==True:
    return 'OK'
    else:
        return 'tidak cocok kurungnya'


    