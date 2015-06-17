class phone(object):
    def __init__(self, par1):   #Инициализация класса и передача параметра par1 при создании обьекта
        self.number = 10
        self.val1 = par1*2
    def printID(self):
        print(id(self))
    def printNumber(self):
        print('Number', self.number)
    def callPar1(self):
        print('Parameter', self.val1)

p = phone(1)
p1 = phone(1)
p.__class__
p1.__class__

class FirstClass():
  def __init__(self, data):
    self.data = "Hello!"
                
  def __str__(self):
    return unicode(self.data)
            
  def setdata(self,data):
    self.data = data
                
  def show(self):
    print self.data


class phone(object):
    def __init__(self):
        self.number = 10
    def call(self):
        print('call', self.number)
p = phone()
p1 = phone()
p1.call()
