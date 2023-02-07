import os

a=os.listdir('test_pic')

g=len(a)

for i in range(0, g):
   os.rename(f'./test_pic/{a[i]}',f'./images/{i}.jpg')