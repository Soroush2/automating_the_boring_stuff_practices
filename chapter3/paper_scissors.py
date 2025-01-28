import random,sys
print('Rock, Paper, Scissors')
tie=0
win=0
lose=0
while True:
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit')
        player_input=input()
        if player_input=='r':
            print('Rock versus...')
            break
        elif player_input=='p':
            print('Paper versus...')
            break
        elif player_input=='s':
            print('Scissors versus...')
            break
        elif player_input=='q':
            sys.exit()
    computer_input=random.randint(1,3)
    if computer_input ==1:
        computer_input='r'
        print('Rock')
    elif computer_input ==2:
        computer_input='p'
        print('Paper')
    elif computer_input ==3:
        computer_input='s'
        print('Scissors')
    if computer_input == player_input:
        tie+=1
        print('It\'s a tie')
    elif (computer_input == 'r' and player_input=='s') or (computer_input =='s' and player_input=='p') or (computer_input=='p'and player_input=='r'):
        lose+=1
        print('You lost')
    elif (computer_input == 's' and player_input=='r') or (computer_input =='p' and player_input=='s') or (computer_input=='r'and player_input=='p'):
        win+=1
        print('you won')
    print('%s Won,%s tie,%s lost' % (win,lose,tie))
    
        


