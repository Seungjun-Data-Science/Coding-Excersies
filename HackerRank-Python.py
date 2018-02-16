Minion Game
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.

# input: A single line of input containing the string  (All uppercase)
# output: name of the winner and their score separated by a space. If draw, print DRAW

S = input().strip()
S_length = len(S)
player1, player2 = 0,0

for i in range(S_length):
    if S[i] in "AEIOU":
        player1 += S_length - i
    else:
        player2 += S_length - i        
        
if player1 > player2:
    print("Kevin", player1)
elif player1 < player2:
    print("Stuart", player2)
else:
    print("Draw")

# Words formed using the first letter B(index 0) = length - index  = 6
# Words formed using the second letter A (index 1) = length - index = 5
# Words formed using the third letter N (index 2) = 4
# Words formed using the fourth letter A = 3
# Words formed using the fifth letter N = 2
# Words formed using the last letter A = 1

####################################################################################################################################
Merge the Tools
Split n(length of string) into n/k subsegments and print out each subsegment string without duplicates

def merge_the_tools(string, k):
    s = string.strip()
    i = 0
    while i < len(s):
        a = s[i:i+k]
        result = ""
        for x in a:
            if x not in result:
                result += x
        print(result)
        i += k

merge_the_tools('AABCAAADA', 3)
####################################################################################################################################
