def createDeque():
    return []
def addFront(deque, item):
    deque.insert(0, item)
    return deque
def addRear(deque, item):
    deque.append(item)
    return deque
def removeFront(deque):
    return deque.pop(0)
def removeRear(deque):
    return deque.pop()
def isEmpty(deque):
    return len(deque) == 0
def size(deque):
    return len(deque)


def palindromeCheck(kata):
    x = len(kata)//2
    y = createDeque()

    for i in kata:
        addRear(y, i)
    
    condition = False
    for j in range(x):
        if removeFront(y) == removeRear(y):
            condition = True
        else:
            condition = False
            break

    return condition

print(palindromeCheck('hannah'))
print(palindromeCheck('surabaya'))
print(palindromeCheck('abcdcba'))
print(palindromeCheck('katak'))
print(palindromeCheck('taat'))
print(palindromeCheck('dia'))
