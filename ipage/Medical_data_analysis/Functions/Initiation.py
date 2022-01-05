def intiate(s1,s2,s3):
    if(s1&~s2&~s3):
        return "recommend Fever Medications"
    elif(~s1&s2&~s3):
        return "recommend cough Medications"
    elif(~s1&~s2&s3):
        return "recommend chest pain Medications"
    else:
        print("You want to take tests:sputum test,chest x-ray,genexpert test and culture test ")
        xxx=0
        

