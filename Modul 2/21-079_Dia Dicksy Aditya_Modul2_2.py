

def inputTask(numOfTask):
    task = []
    for i in range(numOfTask):
        nama = input(f'Nama Proses ke-{i} : ')
        waktu = int(input('Waktu proses : '))
        temp = [nama, waktu]
        enqueue(task, temp)
        
    return task

x = int(input("Jumlah proses yang akan dijadwalkan di CPU = "))
y = inputTask(x)
print(y)

def scheduling(limitTime, task): 
    taskQueue = task
    print(f'Antrian Proses beserta Waktunya = {task}')
    count = 0
    while not(isEmpty(taskQueue)): 
        temp = dequeue(taskQueue) 
        remainTime = temp[1] - limitTime 
        
        if remainTime > 0:
            enqueue(taskQueue, temp)
        else:
            remainTime = 0
        
        temp[1] = remainTime
        count += 1
        print(f"Iterasi ke-{count}")
        if temp[1] == 0:
            print(f"\tProses {temp[0]} telah selesai diproses")
        else:
            print(f"\tProses {temp[0]} sedang diproses, dan sisa waktu proses {temp[0]} = {temp[1]}")
        print(f"\tData proses yang tersisa : {taskQueue}")
    return task

cpu = int(input("waktu proses CPU = "))
tasknew = scheduling(cpu, y) 
