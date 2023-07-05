def createQueue():
    q=[]
    return(q)
def enqueue(q,data):
    q.insert(0,data)
    return(data)
def dequeue(q):
    data=q.pop()
    return(data)
def isEmpty(q):
    return (q==[])
def size(q):
    return (len(q))


def ularNaga(nama,hitungan):

    gameQueue=createQueue()
    for data in nama:
        enqueue(gameQueue,data)
    print("Antrian awal = ",gameQueue)
    while not(isEmpty(gameQueue)):
        for i in range (hitungan):
            enqueue(gameQueue,dequeue(gameQueue))
            print('Proses Antrian = ',gameQueue)
        dequeue(gameQueue)
        print('Antrian = ',gameQueue)
anak=['A','B','C','D','E','F','G']
ularNaga(anak,5)