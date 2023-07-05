#!/usr/bin/env python
# coding: utf-8

# Nama      : Krisdova Rio Alvonsa
# NIM       : 210411100165
# Prodi     : Teknik Informatika / 2C

# Latihan Queue ( CPU Task )

# In[24]:


#Program CPU Task
def InputTask (jumlahtask):
    task = {}
    for i in range (jumlahtask):
        CPU = input ("Masukkan Nama CPU : ")
        waktu = int(input("Lama waktu yang dibutuhkan : "))
        task[CPU] = [waktu,0]
    return task


# In[25]:


Tugas = InputTask (3)


# In[26]:


print(Tugas)


# In[27]:


def createQueue():
    q=[]
    return (q)
def enqueue(q,data):
    q.insert(0,data)
    return(q)
def dequeue(q):
    data=q.pop()
    return(data)
def isEmpty(q):
    return (q==[])
def size(q):
    return (len(q))


# In[37]:


def penjadwalan (bataswaktu, task):
    q = createQueue ()
    for CPU in task.keys():
        enqueue (q, CPU)
    print (q)


# In[38]:


penjadwalan (3, Tugas)


# In[41]:


def penjadwalan (bataswaktu, task):
    q = createQueue ()
    for CPU in task.keys():
        enqueue (q, CPU)
    total = 0
    while not(isEmpty(q)):
        tampung = dequeue(q)
        sisawaktu = task[tampung][0] - bataswaktu
        
        if sisawaktu > 0:
            enqueue(q, tampung)
            proses = bataswaktu
        else:
            proses = task[tampung][0]
            sisawaktu = 0
        total = total + proses
        task[tampung][0] = sisawaktu
        task[tampung][1] = total
        
        print(q)
    return task


# In[42]:


baru = penjadwalan(3, Tugas)


# In[43]:


Tugas = InputTask(3)


# In[44]:


baru = penjadwalan(3, Tugas)
print(baru)


# In[ ]:




