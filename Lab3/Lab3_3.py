import random

P1=1
P2=1
A=[round(random.randint(0,100)/10-5,1) for _ in range(random.randint(5,15))]
print(A)
for i in range(len(A)):
    if   A[i]>0 :
        P1*=A[i]
    elif A[i]<0 :
        P2*=A[i]

print('P1 = ', P1, ' P2 = ', P2)

if P2<0 : P2*=-1

if P2>P1 :
    print('|P2| > |P1|')
else:
    print('|P1| > |P2|')