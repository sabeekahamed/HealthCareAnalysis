import os
path='ForExample'
k=0
contents=os.listdir(os.path.join(path))
for i in contents:
    if i.endswith('.csv'):
        k=k+1

print("total:"+str(k))
