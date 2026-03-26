import random

N=random.randint(3,12)
M=random.randint(3,12)

print('M =',M)
print('N =',N)
A=[[random.randint(10, 99) for j in range(M)] for i in range(N)]

print()

MaxElem=A[0][0]
posy=0
posx=0

for i in range(M):
    for j in range(N):
        if A[j][i]>MaxElem :
            MaxElem=A[j][i]
            posy,posx=i,j


for i in range(M):
    for j in range(N):
        if posy==i and posx==j:
            print(f"\033[1m\033[31m{A[j][i]}\033[0m\033[0m",end=" ")
        elif posy==i:
            print(f"\033[34m{A[j][i]}\033[0m",end=" ")
        elif posx==j:
            print(f"\033[33m{A[j][i]}\033[0m",end=" ")
        else :
            print(A[j][i],end=" ")
    print()

print()

print(f'Максимальный элемент - \033[31m{MaxElem}\033[0m, его строка - \033[34m{posy+1}\033[0m, его столбец - \033[33m{posx+1}\033[0m')

A[0],A[posx]=A[posx],A[0]
for i in range(N):
    A[i][0],A[i][posy]=A[i][posy],A[i][0]
posx,posy=0,0

print()

for i in range(M):
    for j in range(N):
        if i == 0 and j == 0:
            print(f"\033[1m\033[31m{A[j][i]}\033[0m\033[0m", end=" ")
        elif i == 0:
            print(f"\033[34m{A[j][i]}\033[0m", end=" ")
        elif j == 0:
            print(f"\033[33m{A[j][i]}\033[0m", end=" ")
        else:
            print(A[j][i], end=" ")
    print()

print()

print(f'Теперь у максимального элемента - \033[31m{MaxElem}\033[0m, строка - \033[34m{posy+1}\033[0m, столбец - \033[33m{posx+1}\033[0m')