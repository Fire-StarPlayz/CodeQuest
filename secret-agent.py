for i in range(int(input())):
    greeting, response = input().split('|')
    g_letters = set(c.lower() for c in greeting if c.isalpha())
    r_letters = set(c.lower() for c in response if c.isalpha())
    if r_letters.issubset(g_letters):
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")