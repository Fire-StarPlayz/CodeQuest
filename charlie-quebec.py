diction =   {'A': 'Alpha',
            'N': 'November',
            'B': 'Bravo',
            'O': 'Oscar',
            'C': 'Charlie',
            'P': 'Papa',
            'D': 'Delta',
            'Q': 'Quebec',
            'E': 'Echo',
            'R': 'Romeo',
            'F': 'Foxtrot',
            'S': 'Sierra',
            'G': 'Golf',
            'T': 'Tango',
            'H': 'Hotel',
            'U': 'Uniform',
            'I': 'India',
            'V': 'Victor',
            'J': 'Juliet',	
            'W': 'Whiskey',
            'K': 'Kilo',
            'X': 'Xray',
            'L': 'Lima',
            'Y': 'Yankee',
            'M': 'Mike', 
            'Z': "Zulu" }
for i in range(int(input())):
    for j in range(int(input())):
        words = input().upper().split()  
        converted_words = ["-".join(diction[letter] for letter in word) for word in words] 
        print(" ".join(converted_words)) 