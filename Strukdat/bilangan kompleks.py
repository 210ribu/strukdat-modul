class BilanganKompleks:
    def __init__(self,a,b):
        self.real=a
        self.im=b
    def display(self):
        print (self.real,'+',self.im,'i')
    def __str__(self):
        return str(self.real) + " - " + str(self.im) + " i "
    def subKompleks(self,obj):
        a=self.real-obj.real
        b=self.im-obj.im
        return BilanganKompleks(a,b)
    def __sub__(self,obj):
        a=self.real-obj.real
        b=self.im-obj.im
        return BilanganKompleks(a,b)
data1=BilanganKompleks(10,6)
data2=BilanganKompleks(15,10)
jumlah=data1-data2
print(data1)
print(data2)
print(jumlah)