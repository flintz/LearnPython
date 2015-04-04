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

