import random
a=[]
i=random.randint(1,26)+96
a.append(chr(i))
i=random.randint(1,26)+64
a.append(chr(i))
i=random.randint(16,26)+32
a.append(chr(i))
i=random.randint(1,15)+32
a.append(chr(i))
for i in range(0,2):   
 n=random.randint(1,5)
 if n==1: 
    i=random.randint(1,27)+96
 if n==2:
    i=random.randint(1,27)+64
 if n==3:
    i=random.randint(16,26)+32
 if n==4:
    i=random.randint(1,27)+32
 a.append(chr(i))   
random.shuffle(a)
st=str()
    
