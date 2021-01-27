import random, sys

def play():

    userChances = 2
    compChances = 2
    rounds = 0

    while True:

        print('User = %s Hands, Comp = %s Hands' % (userChances, compChances))
        compMove = random.choice(['c', 'k', 'p']).lower()

        while True:
            print('Enter your move: (c) chi, (k) ku, (p) pang or (q) quit')
            userMove = input('Your move: ').lower()
            #storage += 1
            rounds += 1

            if userMove == 'q':
                sys.exit()
            elif userMove == 'c' or userMove == 'k' or userMove == 'p':
                break
            else:
                print('Type either c, k, p or q')
                break


        while rounds == 1:
            rounds += 1
            if (userMove == 'c' and compMove == 'k') or (userMove == 'c' and compMove == 'p')  or (userMove == 'k' and compMove == 'c') or (userMove == 'k' and compMove == 'p') or (userMove == 'p' and compMove == 'c') or (userMove == 'p' and compMove == 'k'): #and storage == 1:
                #storage += 1
                print(f'USER\'S TURN \n{userMove} versus {compMove}')
                print('Nobody wins!')
                break

            elif userMove == compMove: #and storage == 1:
                compChances -= 1
                #storage += 1
                print(f'USER\'S TURN \nUser : {userMove} VS {compMove} : Comp \nYou win! Comp loses a hand.')

                if compChances == 0:
                    print('You\'ve won this match!')
                    sys.exit()

        while rounds == 3:
            rounds -= 3
            if (userMove == 'c' and compMove == 'k') or (userMove == 'c' and compMove == 'p')  or (userMove == 'k' and compMove == 'c') or (userMove == 'k' and compMove == 'p') or (userMove == 'p' and compMove == 'c') or (userMove == 'p' and compMove == 'k'): #and storage != 1:
                #storage -= 3
                print(f'COMP\'S TURN \n{userMove} versus {compMove}')
                print('Nobody wins!')
                break

            elif compMove == userMove: #and storage != 1:
                userChances -= 1
                #storage -= 3
                print(f'COMP\'S TURN \nUser : {userMove} VS {compMove} : Comp \nYou lose! You lose a hand.')

                if userChances == 0:
                    print('Computer wins. You suck at this game!')
                    sys.exit()


play()