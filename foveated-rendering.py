rows = []
for i in range(int(input())):
    y, x = list(map(int, input().split()))
    for i in range(20):
        for j in range(20):
            if j == x and i == y:
                rows.append("100")
            elif x-1 <= j <= x+1 and y-1 <= i <= y+1:
                rows.append("50")
            elif x-2 <= j <= x+2 and y-2 <= i <= y+2:
                rows.append("25")
            else:
                rows.append("10")
        print(" ".join(rows))
        rows = []