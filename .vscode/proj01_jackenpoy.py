#Let's play Jack 'n Poy!
import random

#Player information
score = {'Player Score': 0, 'Comp Score': 0}
print("Hello, I am Pidong! Iligan City is still under MECQ right? I think you're a little bored right now!")
input('Answer: ')
print('Well, I guess you might wanna play with me?')
input('Answer: ')
print("Let's play an old game called 'JACK 'n POY'! Remember? childhood days?")
input('Answer: ')
print('Just press the hotkeys according to what has been said for ROCK, PAPER, and SCISSORS, understood?')
input('Answer: ')
name = input('Let us start by typing your name here: ')
num_win = int(input('How many points does a winner need?\nSelect a number:'))

#Game mechanics
def winner (p1, p2):
    if p1 == 'Q' and p2 == 'E': return 'YOU WON!'
    elif p1 == 'E' and p2 == 'W': return 'YOU WON!'
    elif p1 == 'W' and p2 == 'Q': return 'YOU WON!'
    elif p1 == p2: return "IT'S A TIE!"
    else: return 'PIDONG WON!'
    
#Betting choices
computer = {'Q': 'ROCK', 'W': 'PAPER', 'E': 'SCISSORS'}
c_keys = list(computer.keys())

#In-game program
while True:
    try:
        player_1 = input("Select 'Q' = ROCK, 'W' = PAPER, 'E' = SCISSORS, 'X' = EXIT: ")
        if player_1 == 'X':
            break
        for k in player_1:
            p_bet = computer[k]
        
        c_rand = random.choice(c_keys)
        for c in c_rand:
            c_bet = computer[c]

        x = winner(player_1, c_rand)
        
        if x == 'YOU WON!':
            score['Player Score'] = score['Player Score'] + 1
        elif x == 'PIDONG WON!':
            score['Comp Score'] = score['Comp Score'] + 1
        
        print('''
        ---------------------------------------
        Your bet:''', p_bet, '|', "Pidong's bet:", c_bet,'''\n
        \tINITIAL RESULT:''', x, '\n', '''
        ----------------SCOREBOARD--------------\n''','\t   First to reach', num_win, 'points will WIN!', '\n\n' '\t   ', name + "'s Score:", score.get('Player Score'), '|', "Pidong's Score:", score.get('Comp Score'))
        print('''
        ----------------------------------------
        ''')

        if score['Player Score'] == num_win:
            print('''
               CONGRATULATIONS,''', name + '!', 'YOU WON!!!\n')
            break
        elif score['Comp Score'] == num_win:
            print('''
               TRY HARDER''', name + '!', "I'll just pretend I enjoyed it!\n")
            break
        continue

    except:
        print('''
        Please bet properly, select from these choices:
        ['Q': ROCK, 'W': PAPER, 'E': SCISSORS]
        ''')
        continue

#I guess we're all set! Let's play!
#Let's win against the bot player I created named Pidong!
#Wish me luck!