group1=[]
group2=[]
group3=[]

def cricket():
    a=int(input("enter the no of student who plays cricket"))
    for i in range (a):
      b=int(input("enter roll no of student who plays cricket"))
      group1.append(b)
    print("student who palys cricket",group1)

def football():
    c=int(input("no of students who plays football"))
    for i in range (c):
      d=int(input("enter roll no of student who plays football"))
      group2.append(d)
    print("student who palys football",group2)

def badminton():
    e=int(input("no of students who plays badminton"))
    for i in range (e):
      f=int(input("enter roll no of student who plays batminton"))
      group3.append(f)
    print("student who palys cricket",group3)

def condition1():
    for i in  group1:
        if i in  group2:
           print("students who plalys both cricket and football",i)

def condition2():
    #student who plays either cricket or football
    D=group1+group2
    for i in group1:
        if i in group2:
            D.remove(i)
    for j in group2:
        if j in group1:
             D.remove(j)
    print("student who plays either cricket or football",D)

def condition3():
    #student who neither plays cricket or football
    for i in group1:
        if i in group3:
            group3.remove(i)
    for j in group2:
        if j in group3:
            group3.remove(j)
    w=len(group3)
    print("student who neither plays cricket nor footabll",w)

def condition4():
    #std who plays cricket and badminton but not football
    f=[]
    for i in group1:
        if i in group3:
            f.append(i)
    for j in group2:
        if j in f:
            f.remove(j)
    w1=len(f)
    print("std who plays cricket and badminton but not football",w1)



cricket()
football()
badminton()
s=int(input('''enter your choice:
       PRESS 1: LIST OF STUDENTS WHO PLAY  BOTH CRICKET AND BADMINTON
       PRESS 2: LIST OF STUDENTS WHO PLAY EITHER CRICKET OR BADMINTON BUT NOT BOTH
       PRESS 3: NO. OF STUDENTS WHO PLAY NEITHER CRICKET NOR BADMINTON
       PRESS 4: NO. OF STUDENTS WHO PLAY CRICKET AND FOOTBALL BUT NOT BADMINTON'''))

if s==1:
 condition1()
if s==2:
 condition2()
if s==3: 
 condition3()
if s==4:
 condition4()
    

    


