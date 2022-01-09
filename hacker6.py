"""Problem Statement – Kochouseph Chittilappilly went to Dhruv Zplanet , a gaming space, with his friends and played
a game called “Guess the Word”. Rules of games are –

Computer displays some strings on the screen and the player should pick one string / word if this word matches with
the random word that the computer picks then the player is declared as Winner. Kochouseph Chittilappilly’s friends
played the game and no one won the game. This is Kochouseph Chittilappilly’s turn to play and he decided to must win
the game. What he observed from his friend’s game is that the computer is picking up the string whose length is odd
and also that should be maximum. Due to system failure computers sometimes cannot generate odd length words. In such
cases you will lose the game anyways and it displays “better luck next time”. He needs your help. Check below cases
for better understand Sample input : 5 → number of strings Hello Good morning Welcome you Sample output : morning

Explanation:

Hello → 5
Good → 4
Morning → 7
Welcome → 7
You → 3
First word that is picked by computer is morning

Sample input 2 :
3
Go to hell

Sample output 2:
Better luck next time

Explanation:
Here no word with odd length so computer confuses and gives better luck next time

"""

string1 = "Hello Good morning Welcome you"

split_list = string1.split(" ")


def odd_check(s):
    if s % 2 != 0:
        return True
    else:
        return False


temp_list = []

for index, value in enumerate(split_list):
    if odd_check(len(value)):
        temp_list.append(value)

dict1 = {1: 1}

for i in temp_list:
    dict1[i] = len(i)

a = 0
b = 0
for key, value in dict1.items():
    if value > a:
        a = value
        b = key

if b == 1:
    print("Better Luck Next time!")
else:
    print(f'{b}')
