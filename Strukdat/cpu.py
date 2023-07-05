def inputTask(numOfTask):
    task = {}
    for i in range(numOfTask):
        nama = input('Masukkan nama Task : ')
        waktu = int(input('Masukkan waktu Task : '))
        task[nama] = [waktu, 0]
        
    return task
Task = inputTask(3)
print(Task)

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

def scheduling(limitTime, task):
    taskQueue = createQueue()
    for nama in task.keys():
        enqueue(taskQueue, nama)
    print(taskQueue)
scheduling(3, Task)

def scheduling(limitTime, task): 
    taskQueue = createQueue() 
    for nama in task.keys(): 
        enqueue(taskQueue, nama) 
    
    total = 0
    while not(isEmpty(taskQueue)): 
        temp = dequeue(taskQueue) 
        remainTime = task[temp][0] - limitTime 
        
        if remainTime > 0:
            enqueue(taskQueue, temp)
            procTime = limitTime
        else:
            procTime = task[temp][0]
            remainTime = 0
        
        total += procTime
        task[temp][0] = remainTime
        task[temp][1] = total
        
        print(taskQueue)  
    return task
newtask = scheduling(3, Task) 
print(newtask)
