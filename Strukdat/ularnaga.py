def createQueue():
    a = []
    return (a)
def enqueue(a, data):
    a.insert(0, data)
    return(a)
def dequeue(a):
    data = a.pop()
    return(data)
def isEmpty(a):
    return (a == [])
def size(a):
    return (len(a))
def ularNaga(nama, hitungan):
    gameQueue = createQueue()

    for namaAnak in nama:
        enqueue(gameQueue, namaAnak)
    print('antrian awal = ', gameQueue)

    while not (isEmpty(gameQueue)):
        for i in range(hitungan):
            enqueue(gameQueue, dequeue(gameQueue))
            print('proses antrian = ', gameQueue)

        dequeue(gameQueue)
        print('antrian = ', gameQueue)


ularNaga(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 5)