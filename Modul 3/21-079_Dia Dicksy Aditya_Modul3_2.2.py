class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, new_Next):
        self.next = new_Next

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                # mengembalikan Benar tetapi tidak dapat mengembalikan nilai yang salah
                found = True
            else:
                current = current.getNext()
        return found

    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
            
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    #untuk menghapus node tertentu
    #      
    def remove(self, item): #mendefinisikan fungsi remove dengan parameter item
        current = self.head
        previous = None
        found = False
        if self.search(item):
            while not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def insertPrevious(self, item, newItem):
        current = self.head
        previous = None
        ketemu = False
        if self.search(item):
            while not ketemu:
                if current.data == item:
                    ketemu = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.add(newItem)
            else:
                temp = Node(newItem)
                temp.setNext(current)
                previous.setNext(temp)

    def insertNext(self, item, newItem):
        current = self.head
        previous = None
        ketemu = False
        if self.search(item):
            while not ketemu:
                if current.data == item:
                    ketemu = True
                    previous = current
                    current = current.getNext()
                else:
                    current = current.getNext()
            temp = Node(newItem)
            if current == None:
                previous.setNext(temp)
            else:
                temp.setNext(current)
                previous.setNext(temp)


new = LinkedList()
new.add(8)
new.add(1)
new.add(4)
new.add(7)
new.add(3)

print("Data awal")
new.display()

new.insertNext(11, 4)
print("Data linkedlist yang baru menjadi :")
new.display()
print("============================")

anyar = LinkedList()
anyar.add(1)
anyar.add(5)
anyar.add(7)
anyar.add(2)

print("Data awal")
anyar.display()

anyar.insertNext(11, 7)
print("Data linkedlist yang baru menjadi :")
anyar.display()
print("============================")

mboh = LinkedList()
mboh.add(11)
mboh.add(33)
mboh.add(44)
mboh.add(66)
mboh.add(22)

print("Data awal")
mboh.display()

mboh.insertNext(99, 44)
print("Data linkedlist yang baru menjadi :")
mboh.display()