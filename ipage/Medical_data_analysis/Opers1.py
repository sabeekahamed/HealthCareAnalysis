import pandas as pd
s=[9,10,11,12,13,14,15,16,17,18,19,20,21,22]
df1=pd.read_csv("ForExample\Combined_csv.csv",encoding = 'ISO-8859-1')
ss=[df1[df1.index==0].Manufacturer.to_string(index=False),]
print(ss)
sp =pd.DataFrame({'Manufacturer':["",],'counts':[0,]})
i=0
for sn in df1.Manufacturer:
    t=0
    for sk in df1.Manufacturer:
        if(sn==sk):
            t=t+1
    #sp.append({'Manufacturer':[sn],'counts':[t]},ignore_index=True)
    sp.append(pd.DataFrame({'Manufacturer':[sn],'counts':[t]}),ignore_index=True,verify_integrity=False)
    #sp.counts
    i=i+1
print(sp)


        
    
