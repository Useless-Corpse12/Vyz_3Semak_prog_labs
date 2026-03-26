import random

print('Дана действительная матрица размером M × N. Сформируйте одномерный '
      'массив из средних арифметических значений каждого столбца матрицы. ')
N=int(input('Введите N : '))
M=int(input('Введите M : '))
print()
A=[0]*M
for i in range(N):
      for j in range(M):
            RndF=random.randint(0,1000)/100-5
            print(f'{RndF:6.2f}',end=' ')
            A[j]+=RndF
      print()
print()
A=[x / N for x in A]
for j in range(M):
      print(f'{A[j]:6.2f}',end=' ')
print()