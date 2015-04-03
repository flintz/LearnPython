#Rename all files 
import os
p = 'D:\Test'
files = os.listdir(p)
print(files)
i = 335
for f in files:
    n = 'bixes_% s.exr' % i
    i += 1
    oldName = os.path.join(p,f)
    newName = os.path.join(p,n)
    os.rename(oldName, newName)
    
