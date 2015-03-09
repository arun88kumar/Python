def check_result(game):
    
    #this will contain all possible combinations of winning collections
    possibilities = list()
    
    #adding all rows in the game
    possibilities.extend([row for row in game])
    
    #adding all columns in the game
    possibilities.extend([list(x) for x in zip(*game)])
    
    #adding the diagonal 
    possibilities.append([r[i] for i,r in enumerate(game)])
    
    #adding the opposite diagonal
    possibilities.append([r[-i-1] for i,r in enumerate(game)])
    
    #checking if all possiblities for a winner
    for possible in  possibilities:
        if len(set(possible)) == 1:
            return possible[0]
    
def check_play(game):
    for row in game:
        for box in row:
            if box == "_":
                return True

    return False
    
def play_box(game,box,play):
    
    box_mapping = { 1:(0,0), 2:(0,1), 3:(0,2),
                    4:(1,0), 5:(1,1), 6:(1,2),
                    7:(2,0), 8:(2,1), 9:(2,2),
                    }
    
    if box in box_mapping.keys():
        x,y = box_mapping[box]
        if game[x][y] == "_":
            game[x][y] = play
            return game
    else:
        return None
       

def display(game):
    print('-------------')
    for row in game:
        s = ""
        for box in row:
            s = s + '| ' + box + ' '
        print(s + '| ')
        print('-------------')

    
def game_play():
    start = """    
    ________Tic Tac Toe_______
    Instructions
    We have nine boxes to fill in, on every play the player needs to enter the box number as below
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
    
    The first play will be assigned with 'X' and second play will be 'O'
    
    !!!!! Lets play !!!!
    """
    print(start)
    
    Player1_name = str(input("Enter First Player's Name : "))
    Player2_name = str(input("Enter Second Player's Name : "))
    
    print("__VS__".join([Player1_name,Player2_name]))
    
    game = [['_' for i in range(3)]for j in range(3)]
    x_play = True
    
    while(True):
        if not check_play(game):
            print('The game ended in a Tie');
            display(game)
            break
        
        display(game)
        if x_play:
            print(Player1_name + "'s turn")
        else:
            print(Player2_name + "'s turn")
            
        while(True):
            box = int(input('Enter box to play : '))
            update_game = play_box(game,box,'X' if x_play else 'O')
            if update_game == None:
                print ("Invalid box selected, Please re-play")
            else:
                game = update_game
                x_play = not x_play
                break
            
        
        result = check_result(game)
        if result == 'X':
            print("Game Over")
            print(Player1_name + ' has won the game')
            display(game)
            break
        elif result == 'O':
            print("Game Over")
            print(Player2_name + ' has won the game')
            display(game)
            break
        

if __name__ == '__main__':
    game_play()
    while(True):
        restart = input('do you wanna start a new game, Enter Y/N: ')
        if restart == "Y" or restart == "y":
            game_play()
        else:
            break
            
    
    
    
    
    

    
    