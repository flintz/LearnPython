def find():
  str_1="This is test string"
  index_position=str_1.find("test")
  print(index_position)# return(number) or -1
  return()
    
def index_try_except(): # Get position word in string, try: & except: 
  str_1="This is test string"
  try:
    index_position=str_1.index("test")
    print(index_position) # Return(number) or Error
  except ValueError:
    print("The substring was not found")
  return()
    
def url_string():
  url_string='www.google.com'
  if url_string.endswith('.com')
    print('.com is that')
  else:
    print('.com is not that')
