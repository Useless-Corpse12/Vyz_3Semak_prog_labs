from Lab10_2 import GraphVisual as FancyView
from Lab10_1 import get_graf
#На часах 2:31, пояснение для будущего меня
#
#Магистерская программа по информатике состоит из n семестровых курсов. Граф G отображает следующие зависимости: вершины
#графа соответствуют курсам, из v идет ориентированное ребро в w,
#если w можно изучать только после v. Постройте алгоритм, который по
#G определит минимальное количество семестров, необходимое для
#изучения всей программы (в одном семестре может быть сколько
#угодно курсов).
#
#я беру ориент граф состоящий из деревьев и нахожу самый длинный маршрут



cnt,rts = get_graf("103Graph.txt")
rts = [edge[:2] for edge in rts]

print(rts)

FancyView(cnt,rts,is_naprav=True,gr_label="Selling a garage. Call me : 893817339")

rts.sort()
rts = [[chr(a+48),chr(b+48)] for a,b in rts]
print(rts)

ribbit_pairs = []

for a_char, b_char in rts:
    #Если мы тут впервые - делаем метку
    if len(ribbit_pairs) == 0:
        ribbit_pairs.append(a_char + b_char)
        continue
    is_new = True
    #сверяемся что нынешниый путь не продолжение предидущего
    for frogy in range(len(ribbit_pairs)):
        if ribbit_pairs[frogy][-1] == a_char:
            ribbit_pairs[frogy] += b_char
            is_new = False
            break

    # Проверка в середине строки, если наш путь - продолжение части предидущего, ветвим ещё раз
    if is_new:
        for frogy in range(len(ribbit_pairs)):
            if a_char in ribbit_pairs[frogy]:
                idx = ribbit_pairs[frogy].find(a_char)
                if ribbit_pairs[frogy][idx + 1] != b_char:
                    ribbit_pairs.append(ribbit_pairs[frogy][:idx + 1] + b_char)
                    is_new = False
                    break

    #если всё ещё думаем что новоее - добавляем
    if is_new:
        ribbit_pairs.append(a_char + b_char)

print(ribbit_pairs)
print(f"{len(max(ribbit_pairs, key=len))} - минимальное количество курсов для изучения всей программы")
