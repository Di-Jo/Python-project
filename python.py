def details():
    print("\t\t\tLOVELY PROFESSIONAL UNIVERSITY\t\t")
    username=input("Enter student name:\t")
    num=input("Enter rollno: \t")
    ri=int(input("Semester: "))
    print("STUDENT NAME: ",username)
    print("STUDENT ROLLNO:",num)
    print("Semester:",ri) 


def tgpa():
    dict1={}
    print("Total number of subjects in semester one:")
    s=int(input("Enter the number of subject:"))
    for i in range(s):
        print("Enter the subject and mark obtaind by student:")
        str1=input("SUBJECT:")
        mrk=int(input("MARK:"))
        dict1.update({str1:mrk})
    l1=list(dict1.values())
    l2=list(dict1.keys())
    tg=0
    for i in l1:
        if(i<=100 and i>=90):
            tg=tg+9
        elif(i<90 and i>=80):
            tg=tg+8
        elif(i<80 and i>=70):
            tg=tg+7
        elif(i<70 and i>=60):
            tg=tg+6
        elif(i<60 and i>=50):
            tg=tg+5
        elif(i<=49):
            tg=4
    tgp=tg/s
    print("________")
    print("SUBJECT                          MARK_SCORED")
    for (i,j) in zip(l1,l2):
        print(j,"\n","                                     ",i,"\n")
    print("TGPA OF THE STUDENT IS = ",tgp)       
    print("________")
    
    dict2={}
    print("Total number of subjects in semester two:")
    x=int(input("Enter the number of subject:"))
    for i in range(x):
        print("Enter the subject and mark obtaind by student:")
        str2=input("SUBJECT:")
        mrk2=int(input("MARK:"))
        dict2.update({str2:mrk2})
    l11=list(dict2.values())
    l22=list(dict2.keys())
    tg=0
    for i in l11:
        if(i<=100 and i>=90):
            tg=tg+9
        elif(i<90 and i>=80):
            tg=tg+8
        elif(i<80 and i>=70):
            tg=tg+7
        elif(i<70 and i>=60):
            tg=tg+6
        elif(i<60 and i>=50):
            tg=tg+5
        elif(i<=49):
            tg=4
    tgp2=tg/s
    print("_______")
    print("SUBJECT                          MARK_SCORED")
    for (i,j) in zip(l11,l22):
        print(j,"\n","                                     ",i,"\n")
    print("TGPA OF THE STUDENT IS = ",tgp2)
    print("_______")

    cgpa=(tgp+tgp2)/2
    
    print("_______")
    print("TOTEL CGPA OBTAIND BY THE STUDENT = ",cgpa)
    print("_______")
      


    
            
                
def display():
    details()     
    tgpa()
    
        
            
    
#main
display()
