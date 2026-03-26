from logging import exception

from Lab10_2 import GraphVisual as WelcomeToHell
from Lab10_1 import get_graf

def floyd_path(cnt, rts, start, end, directed=True):
    INF = 10**9
    # Матрицы: индексы от 1 до cnt включительно
    dist = [[INF] * (cnt + 1) for _ in range(cnt + 1)]
    next_node = [[None] * (cnt + 1) for _ in range(cnt + 1)]

    # Диагональ: нулевое расстояние до себя
    for i in range(1, cnt + 1):
        dist[i][i] = 0
        next_node[i][i] = i

    # Заполняем рёбра
    for u, v, w in rts:
        if w < dist[u][v]:
            dist[u][v] = w
            next_node[u][v] = v
        if not directed:  # для неориентированного графа — симметрично
            if w < dist[v][u]:
                dist[v][u] = w
                next_node[v][u] = u

    # Флойд–Уоршелл
    for k in range(1, cnt + 1):
        for i in range(1, cnt + 1):
            for j in range(1, cnt + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Восстановление пути
    if next_node[start][end] is None:
        return None

    path = []
    curr = start
    while curr != end:
        path.append(curr)
        curr = next_node[curr][end]
        if curr is None:
            return None
    path.append(end)

    return "-".join(map(str, path))

Grapfs = ["Graph.txt", "GraphVes.txt", "103Graph.txt"]
bool_list = [False, True]
def pool():

    print("Какой граф интересует:")
    for i in range(len(Grapfs)):
        name = Grapfs[i]
        cnt, rts = get_graf(name)
        for bb in bool_list:
            print(i * 2 + bb, f"|{name}| {"" if bb else "не"}направленный")
            WelcomeToHell(cnt, rts, is_naprav=bb, vzves=True, gr_label=f"{i * 2 + bb}|{name}|")

    return input(">")

def show(numero):
    name = Grapfs[numero//2]
    cnt, rts = get_graf(name)
    print(rts)
    WelcomeToHell(cnt, rts, is_naprav=bool_list[numero%2], vzves=True, gr_label=f"{numero}|{name}|")

if __name__ == '__main__':
    print("Вас приветствует консоль! (это ненормально чувак, поспал бы ты)")
    menu =("Список команд :\n*help* - вызов этого меню"
           "\n*pool* - повторный вызов списка графов(выбор другого)"
           "\n*exit* - выход"
           "\n*show* - показ выбранного графа"
           "\n*sp a b* поиск кратчайшего путик,"
           ",где а - точка из какой выходим и b - точка в которую идём")
    numnowgraph=0
    nowgraph=None
    inp=None
    print(menu)
    while True:

        inp=input(">")
        strips = inp.split(" ")
        try:
            match (strips[0]):
                case "help":
                    print(menu)
                case "pool":
                    if len(strips)==1:
                        numnowgraph= int(pool())
                    else:
                        numnowgraph = int( strips[1] )
                    nowgraph = get_graf(Grapfs[numnowgraph//2])
                    print(nowgraph)
                case "show":
                    show(numnowgraph)
                case "exit":
                    break
                case "sp":
                    print(floyd_path(nowgraph[0],nowgraph[1],int(strips[1]),int(strips[2]),bool_list[numnowgraph%2]))
                case _:
                    print(menu)

        except exception(exception):
            print("nothing to say...")
