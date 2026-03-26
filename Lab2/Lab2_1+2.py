def python_is_shit(chislo:float)->int: #так как питон прекрасно представляет числа с плавающей точкой
    str_num = str(chislo)              #я подумал что решением будет округлять числа при каждом их изменении
    if '.' in str_num:
        return len(str_num.split('.')[1])
    else:
        return 0

def f(inp:float)->float:        #f(x) Полный график на десмосе
    if      inp<-8  :
        return 3*inp+27
    elif    inp<-5  :
        return (-7/3)*inp-47/3
    elif    inp<-2  :
        return (9-(inp+5)**2)**(1/2)-7
    elif    inp<5   :
        return -(49-(inp+2)**2)**(1/2)
    elif    inp<8   :
        return inp*2/3-10/3
    elif    inp<=9  :
        return 4*inp-30
    else            :
        return float('nan')



h=float(input('Введите значение шага h : '))
KocTblJIb=python_is_shit(h)

x=-9.0

# Украшение
print(f'\n|{"-" * (17 + KocTblJIb)}|')
print(f'| {"while":^{16 + KocTblJIb}}|')
print(f'|{"-" * (5 + KocTblJIb)}т{"-" * 11}|')
print(f'| {"x":^{3 + KocTblJIb}} | {"y":^{9}} |')
print(f'|{"-" * (5 + KocTblJIb)}|{"-" * 11}|')
# Украшение



#Задание 1
while round(x, KocTblJIb)<=9:
    y=f(round(x,KocTblJIb))
    print(f'|{round(x,KocTblJIb):{4+KocTblJIb}.{KocTblJIb}f} |{y:10.5f} |')
    x += h
print(f'|{"-" * (5 + KocTblJIb)}|{"-" * 11}|')
#Задание 1



# Украшение
print(f'\n|{"-" * (17 + KocTblJIb)}|')
print(f'| {"for":^{16 + KocTblJIb}}|')
print(f'|{"-" * (5 + KocTblJIb)}т{"-" * 11}|')
print(f'| {"x":^{3 + KocTblJIb}} | {"y":^{9}} |')
print(f'|{"-" * (5 + KocTblJIb)}|{"-" * 11}|')
# Украшение



#Задание 2
for steps in range(int(18/h)+1):
    x=round(-9+h*steps,KocTblJIb)
    y=f(x)
    print(f'|{round(x, KocTblJIb):{4 + KocTblJIb}.{KocTblJIb}f} |{y:10.5f} |')
print(f'|{"-" * (5 + KocTblJIb)}|{"-" * 11}|')
#Задание 2