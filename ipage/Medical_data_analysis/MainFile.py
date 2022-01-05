print("Please enter your details:")
print("Yes means:1   and No means :0")
age=int(input("Enter your age:"))
wt=int(input("Enter yor weight:"))
s1=int(input("severe_cough(1/0)"))
s2=int(input("Chest_pain(1/0)"))
s3=int(input("Fever(1/0)"))
if(s1&~s2&~s3):
    xxx=s1  #xxx is med
elif(~s1&s2&~s3):
    xxx=s2
elif(~s1&~s2&s3):
    xxx=s3
else:
    print("You want to take tests:sputum test,chest x-ray,genexpert test and culture test ")
    xxx=0
print("====================================================================================")
print("Enter the test results:")

t1=int(input("sputem test:"))
t2=int(input("chest x-ray:"))               #test1=starting,test2=2nd month,test3=
t3=int(input("genes:"))
t4=int(input("Is cavitation formed?"))
cd=int(input("Is cd4+ counts less than 100?"))
hiv=int(input("HIV:"))
if(t1&~t2&~t3):
    st=t1  #xxx is med
elif(~t1&t2&~t3):
    st=t2
elif(~t1&~t2&t3):
    st=t3
else:
    st=0
print(st)
if(st):
    print("you need not be admitted")
    plan=1
else:
    print("you need to be admitted")
    plan=0

import pandas as pd

if(age<15&wt<40):
    mm="child"
    df=pd.read_csv('Regimen 1\childs.csv')
else:
    mm="adult"
    df=pd.read_csv('Regimen 1\dult.csv')
print("The following list of drugs you need to take for two weaks:")
print([df])
