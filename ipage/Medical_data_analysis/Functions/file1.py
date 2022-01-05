import pandas as pd
def file1(age,wt):
    ss=""
    param=""
    medi=""
    if(age<15 and wt<40):
        mm="child"
        df=pd.read_csv('Regimen 1\childs.csv',encoding = 'ISO-8859-1')
        param="Dose"
        for s in df["Anti-TB Drugs"]:
            ss=ss+s+" : "+df[df["Anti-TB Drugs"]==s].Dose.to_string(index=False)+" mg"+"+"
    else:
        mm="adult"
        df=pd.read_csv('Regimen 1\dult.csv',encoding = 'ISO-8859-1')
        if(wt<40):
            for s in df["Anti-TB Drugs"]:
                ss=ss+s+": "+df[df["Anti-TB Drugs"]==s].less.to_string(index=False)+" mg"+"+"
        elif(wt<55):
            for s in df["Anti-TB Drugs"]:
                ss=ss+s+": "+df[df["Anti-TB Drugs"]==s].inter.to_string(index=False)+" mg"+"+"
        else:
            for s in df["Anti-TB Drugs"]:
                ss=ss+s+": "+df[df["Anti-TB Drugs"]==s].grtr.to_string(index=False)+" mg"+"+"

    ss=ss[:-1]
file1(12,67)    
print(ss)



