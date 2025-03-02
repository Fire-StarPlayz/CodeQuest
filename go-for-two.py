dict = {-15:2, -14:1, -13:2, -12:1, -11:2, -10:2, -9:1, -8:2, -7:1, -6:1, -5:2, -4:2, -3:1, -2:2, 
        -1:1, 0:1, 1:2, 2:1, 3:1, 4:1, 5:2, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:2,}
for i in range(int(input())):
    team, opp = list(map(int, input().split()))
    if -15 <= team-opp <= 12:
        print(dict.get(team-opp))
    else:
        print(1)