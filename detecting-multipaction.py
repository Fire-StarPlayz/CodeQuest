for _ in range(int(input())):  # Number of test cases
    list1 = list(map(float, input().split()))  # Read first list of floats
    list2 = list(map(float, input().split()))  # Read second list of floats
    finlist = []
    
    for i in range(len(list1)):
        if 0.6 <= list1[i] <= 0.85 and 0.6 <= list2[i] <= 0.85:
            finlist.append(i)

    N = len(finlist)  # Count detected events

    if N == 0:
        print("No multipaction events detected.")
    elif N == 1:
        print(f"A multipaction event was detected at time index {finlist[0]}.")
    else:
        print(f"{N} multipaction events were detected at time indices: {' '.join(map(str, finlist))}.")
