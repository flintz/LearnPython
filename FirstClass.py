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
