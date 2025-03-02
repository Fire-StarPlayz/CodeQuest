def Hamming(word1: str, word2: str) -> int:
    if len(word1) != len(word2):
        return 10000000000000000
    return sum(c1 != c2 for c1, c2 in zip(word1, word2))

for i in range(int(input())):
    D, W = (input().split(' '))
    Diction = []
    Words = []
    ham = []
    for i in range(int(D)):
        Diction.append(input())
    for i in range(int(W)):
        Words.append(input())
    for j in range(int(W)):
        for i in range(int(D)):
            ham.append(Hamming(Words[j], Diction[i]))
        min_value = min(ham)
        min_index = ham.index(min_value)
        print(Diction[min_index])
        ham = []