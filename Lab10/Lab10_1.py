def get_graf(filename):
    with open(filename) as f:
        lines = f.read().strip().splitlines()
    count = int(lines[0])
    routs = [list(map(int, line.split())) for line in lines[1:]]
    routs = [_ + [1] if len(_) == 2 else _ for _ in routs]
    return count, routs

def smezh_matrix(cnt,rts):
    output_shit=[[0]*cnt for _ in range(cnt)]
    for i in range(cnt):
        for j in range(cnt):
            for k in range(len(rts)):
                output_shit[i][j] = rts[k][2] if (rts[k][0] == i + 1 and rts[k][1] == j + 1) else output_shit[i][j]
    return output_shit


def fancy_output(mat):

    n = len(mat)
    data_width = max(len(str(mat[i][j])) for i in range(n) for j in range(n))
    data_width = max(data_width, len(str(n)))

    cell_width = data_width + 2
    left_width = max(len("from\\to"), len(str(n))) + 2

    top_line = "┌" + "─" * left_width + ("┬" + "─" * cell_width) * n + "┐"
    mid_line = "├" + "─" * left_width + ("┼" + "─" * cell_width) * n + "┤"
    bot_line = "└" + "─" * left_width + ("┴" + "─" * cell_width) * n + "┘"

    header = (f"│{'from\\to':^{left_width}}│" +"│".join(f"{i+1:^{cell_width}}" for i in range(n)) + "│")

    rows = []
    for i in range(n):
        row = (
            "│" +
            f"{i+1:^{left_width}}" +
            "│" +
            "│".join(f"{mat[i][j]:^{cell_width}}" for j in range(n)) +
            "│"
        )
        rows.append(row)

    print(top_line)
    print(header)
    print(mid_line)
    for i, r in enumerate(rows):
        print(r)
        if i < n - 1:
            print(mid_line)
    print(bot_line)

if __name__ == "__main__":
    print('Вывод матрицы смежности взвешенного графа')
    cnt,rts = get_graf("GraphVES.txt")
    fancy_output(smezh_matrix(cnt,rts))
    print('Вывод матрицы смежности просто графа')
    cnt,rts = get_graf("Graph.txt")
    fancy_output(smezh_matrix(cnt,rts))

    print(rts)