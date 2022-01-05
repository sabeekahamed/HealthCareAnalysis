def intiate2(t1,t2,t3,t4,cd,hiv):
    if(t1&~t2&~t3):
        st=t1  #xxx is med
    elif(~t1&t2&~t3):
        st=t2
    elif(~t1&~t2&t3):
        st=t3
    else:
        st=0
    if(st):
        print("you need not be admitted")
        plan=1
    else:
        print("you need to be admitted")
        plan=0
