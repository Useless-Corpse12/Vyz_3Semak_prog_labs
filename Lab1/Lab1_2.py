t=0
print('  t  |  z  ')
while (t<3):
    print(f'{t:4.1f} | {t**2 :4.2f}')
    t+=0.5
while (t<=7):
    print(f'{t:4.1f} | {t+1:4.2f}')
    t += 0.5
while (t<=10):
    print(f'{t:4.1f} | {t ** (1/2):4.2f}')
    t += 0.5