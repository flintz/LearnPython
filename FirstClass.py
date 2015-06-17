class FirstClass():
  def __init__(self, data):
    self.data = "Hello!"
                
  def __str__(self):
    return unicode(self.data)
            
  def setdata(self,data):
    self.data = data
                
  def show(self):
    print self.data
