N = int(input())
matrix = [input().replace(" ", "") for _ in range(N)]

white = 0
blue = 0

def count_color(x, y, n):
    global white, blue
    color = matrix[x][y]
    same = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != color:
                same = False
                break
        if not same:
            break
    if same:
        if color == '0':
            white += 1
        else:
            blue += 1
    else:
        m = n // 2
        count_color(x, y, m)
        count_color(x, y + m, m)
        count_color(x + m, y, m)
        count_color(x + m, y + m, m)

count_color(0, 0, N)
print(white)
print(blue)
