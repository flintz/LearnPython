class phone(object):
    def __init__(self):
        self.number = 10
    def call(self):
        print('call', self.number)
p = phone()
p1 = phone()
p1.call()
