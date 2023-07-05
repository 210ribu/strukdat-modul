def remainderFunction(a , b):
    return a % b

def createHashTable(a = 11):
    return [[None] for i in range(a)]

def chainning(data, hashTable):
    for i in data:
        index = remainderFunction(i, len(hashTable))
        if hashTable[index] == [None]:
            hashTable[index] = [i]
        else:
            hashTable[index].append(i)

def searchHash(a, hashTable):
    findIndex = remainderFunction(a, len(hashTable))
    for i in range(len(hashTable[findIndex])):
        if a == hashTable[findIndex][i]:
            print(f'Data berada di slot ke- {findIndex}, dan indeks ke-{i}')
            return

    print(False)


a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
makeHashTable = createHashTable()
chainning(a, makeHashTable)
print(makeHashTable)
searchHash(66, makeHashTable)
searchHash(54, makeHashTable)
searchHash(20, makeHashTable)
searchHash(55, makeHashTable)
searchHash(100, makeHashTable)

