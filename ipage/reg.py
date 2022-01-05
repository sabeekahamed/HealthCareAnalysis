import json
import os
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#------------------------- Doctor registration -------------------------------------------

def docid(dn):
    l = len(os.listdir("ipage\doctor_details"))
    filename = 'D-100'
    if l != 0:
        f = str( 100 + l)
        ff = 'D-'
        filename = ff + f
    data = {'id':filename, 'name': dn,'status':'NA'}
    with open('ipage\doctor_details\{}.json'.format(filename), 'w') as f:
        json.dump(data, f)
    return filename

#------------------------ Patient registration -------------------------------------------

def registration(fn,ln,dob,g):
    l = len(os.listdir("ipage\patient_details"))
    filename = 'P-100'
    if l != 0:
        f = str(100 + l)
        ff = 'P-'
        filename = ff + f
    data = {'id':filename, 'fname': fn, 'lname':ln, 'Dob':dob, 'Gender':g,'status':'NA'}
    with open('ipage\patient_details\{}.json'.format(filename), 'w') as f:
        json.dump(data, f)
    return filename

#------------------------- (json)ing questions -------------------------------------------

def basiq(a,pid,d,w,c,f,cp,brp,wz,ns,sl,wl,t,n,sr,h,o): #stores the queries
        with open('ipage\questions\{}.json'.format(pid),'r')as s:
            ss = json.load(s)
        data = {'weight':w,'cough':c,'fever':f,'chest_pain':cp,'breathing':brp,'wheezing':wz,'night_sweats':ns,'sleep':sl,'weight_loss':wl,'throat':t,'nose':n,'skin':sr,'habits':h,'others':o}
        ss.update(data)
        with open('ipage\questions\{}.json'.format(pid),'w')as f1:
            json.dump(ss,f1)
        r = ran(h,f,c,cp,w,wl)
        return r
#------------------------- Patient login check -------------------------------------------

def plogin(patid):
    try:
        r = open('ipage\patient_details\{}.json'.format(patid),'r')
        rr = json.load(r)
        return rr
    except FileNotFoundError:
        return None

#------------------------- Doctor login Check --------------------------------------------

def dlogin(did):
    try:
        r = open('ipage\doctor_details\{}.json'.format(did),'r')
        rr = json.load(r)
        rrr = rr['name']
        return rrr
    except FileNotFoundError:
        return None

#------------------------ Random forest algorithm ----------------------------------------

def ran(h,f,c,cp,w,wl):
    w = int(w)
    if w <60:
        if w <40:
            w = 1
        else:
            w = 2
    else:
        w = 3
    df = pd.read_csv('ipage\Medical_data_analysis\First.csv')
    labels = np.array(df['tb'])     #last_column
    df = df.drop('tb',axis=1)
    df = df.drop('id',axis=1)
    df_list = list(df.columns)
    tf = np.array(df)

    train_df, test_df, train_labels, test_labels = train_test_split(tf, labels, test_size = 0.25, random_state = 42)

    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

    rf.fit(train_df, train_labels);
    predictions = rf.predict([[int(h[0]),int(f),int(c),int(cp),int(w),int(wl)]])
    truefalse = str(int(predictions[0]))
    return truefalse

#-----------------------------------------------------------------------------------------

def dtt(patid):
    r = open('ipage\patient_details\{}.json'.format(patid),'r')
    rr = json.load(r)
    for i in rr:
            a = rr['id']
            b = rr['fname'] + rr['lname']
            c = rr['Dob']
            d = rr['Gender']
            e = rr['status']
    dta = ' id :  '+a+'\n Name : '+b+'\n Date of birth : '+c+'\n Gender : '+d+'\n Status : '+e
    file = open(r'ipage\static\ipage\\temp\{}.txt'.format(patid),'w')
    file.write(dta)

#-----------------------------------------------------------------------------------------

def chek(pid,d,a):
    try:
        open('ipage\patient_details\{}.json'.format(pid),'r')
        try:
            open('ipage\questions\{}.json'.format(pid),'r')
            return True
        except FileNotFoundError:
            data = {'id':pid,'disease':d,'Doctor refered':a}
            with open('ipage\questions\{}.json'.format(pid),'w')as f:
                json.dump(data,f)
            return False
    except FileNotFoundError:
        return '... The Requested person does not have Health Care account ...'
#-----------------------------------------------------------------------------------------

def ran1(sp,xr,gt,ct,hiv,cd4):

    w = 39
    if w <60:
        if w <40:
            w = 1
        else:
            w = 2
    else:
        w = 3
    pf = pd.read_csv('ipage\Medical_data_analysis\Result.csv')
    pf = pf[pf.cured==1]
    kf = pf
    labels = np.array(pf['regimen'])
    pf = pf.drop('regimen',axis=1)
    pf = pf.drop('id',axis=1)
    pf = pf.drop('cured',axis=1)
    pf_list = list(pf.columns)
    ttf = np.array(pf)
    from sklearn.model_selection import train_test_split
    train_df, test_df, train_labels, test_labels = train_test_split(ttf, labels, test_size = 0.25, random_state = 42)
    predict = tree.DecisionTreeClassifier()
    predict.fit(train_df,train_labels)
    pred = predict.predict([[int(sp),int(xr),int(gt),int(ct),int(hiv),int(cd4)]])
    print(pred)
    age=23
    st='ipage\Medical_data_analysis\Regimen'+str(int(pred))
    print(st)
    wt=43
    if(age<15&wt<40):
        mm="child"
    else:
        mm="dult"
    dest=st+'\\'+mm+'.csv'
    print(dest)
    df=pd.read_csv(dest,encoding = 'ISO-8859-1')
    print("The following list of drugs you need to take for two weeks:")
    print(df)
    if age<40:
        tmp='less'
    elif age<60:
        tmp='inter'
    else:
        tmp='grtr'
    tmp
    df=df[['Anti-TB Drugs',tmp]]
    po=''
    k=df[tmp]
    l=0
    for i in df['Anti-TB Drugs']:
        po=po+str(i)+':'+str(k[l])+'mg+'
        l=l+1
    po=po[0:-1]
    print(po)
    pf = pd.read_csv("ipage\Medical_data_analysis\Mainpage\LastUpdate.csv",encoding = 'ISO-8859-1',skip_blank_lines=True)
    lt = pf[pf['Generic / Quantity'] == po]


    ae = lt['S/N']-1
    if len(ae)==0:
        return "medicine name: Coxter 4FD costs :5.7 rs"
    wt = "ipage\Medical_data_analysis\\total\\SN"+str((int(ae)))+".csv"
    pm = pd.read_csv(wt, encoding='ISO-8859-1',skip_blank_lines=True)
    wtw = "ipage\Medical_data_analysis\\total\\SNS" + str((int(ae)))+".csv"
    pm1 = pd.read_csv(wtw, encoding='ISO-8859-1', skip_blank_lines=True)
    pm1 = pm1[pm1['cured'] == 1]
    pm1 = pm1.drop('SN', axis=1)
    pm1 = pm1.drop('cured', axis=1)
    labels = np.array(pm1['med'])
    pm1 = pm1.drop('med', axis=1)


    pm1_list = list(pm1.columns)
    ttf = np.array(pm1)
    from sklearn.model_selection import train_test_split
    train_df, test_df, train_labels, test_labels = train_test_split( ttf, labels, test_size=0.25, random_state=42)
    predict = tree.DecisionTreeClassifier()
    predict.fit(train_df, train_labels)
    pred = predict.predict([[1, 1, 0, 1, 1, 1]])
    pred
    pm
    sp=pm[pm['S/N']==int(pred)]
    med = str(sp['Name'])
    pr = str(sp['Price(In Rs.)'])
    wwm=" medicine name:"+med+" costs "+pr+'rs'
    print(wwm)
    return wwm

#-----------------------------------------------------------------------------------------
