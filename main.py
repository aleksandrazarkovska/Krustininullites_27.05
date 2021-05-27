def display_board(board): 
    blankBoard= """
    ___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
""" 
    for i in range(1,10): 
        if (board[i] == 'O' or board[i] == 'X'): 
            blankBoard = blankBoard.replace(str(i), board[i]) 
        else: 
            blankBoard = blankBoard.replace(str(i), ' ') 
    print(blankBoard) 
def player_input():
    player1 = input("Lūdzu, atlasiet 'X' vai 'O' ") 
    while True: 
        if player1.upper() == 'X': 
            player2='O' 
            print("Jūs izvēlējāties " + player1 + ". 2. spēlētājs būs " + player2) 
            return player1.upper(),player2 
        elif player1.upper() == 'O':
            player2='X' 
            print("Jūs izvēlējāties " + player1 + ". 2. spēlētājs būs " + player2) 
            return player1.upper(),player2 
        else: 
            player1 = input("Lūdzu, atlasiet 'X' vai 'O' ") 

def place_marker(board, marker, position): 
    board[position] = marker 
    return board 

def space_check(board, position): 
    return board[position] == '#' 

def full_board_check(board): 
    return len([x for x in board if x == '#']) == 1 

def win_check(board, mark): 
    if board[1] == board[2] == board[3] == mark: 
        return True 
    if board[4] == board[5] == board[6] == mark: 
        return True 
    if board[7] == board[8] == board[9] == mark: 
        return True 
    if board[1] == board[4] == board[7] == mark: 
        return True 
    if board[2] == board[5] == board[8] == mark: 
        return True 
    if board[3] == board[6] == board[9] == mark: 
        return True 
    if board[1] == board[5] == board[9] == mark: 
        return True 
    if board[3] == board[5] == board[7] == mark: 
        return True 
        return False 

 
def player_choice(board): 
    choice = input("Lūdzu, atlasiet tukšu vietu no 1 līdz 9:") 
    while not space_check(board, int(choice)): 
        choice = input("Šī vieta nav brīva. Lūdzu, izvēlieties no 1 līdz 9:") 
        return choice 

def replay(): 
    playAgain = input("Vai vēlaties spēlēt vēlreiz (jā / nē)? ") 
    if playAgain.lower() == 'jā': 
        return True 
    if playAgain.lower() == 'nē': 
        return False 
    if __name__ == "__main__": 
        print('Laipni lūdzam spelē "Krustiņi-nullītes"!') 
i = 1 
players=player_input() 
board = ['#'] * 10 
while True: 
    game_on=full_board_check(board) 
    while not game_on: 
        position = player_choice(board) 
        if i % 2 == 0: 
            marker = players[1] 
        else: 
            marker = players[0] 
        place_marker(board, marker, int(position)) 
        display_board(board) 
        i += 1 
        if win_check(board, marker): 
            print("Tu uzvarēji!") 
            break
        game_on=full_board_check(board) 
    if not replay(): 
        break
    else: 
        i = 1 
        players=player_input() 
        board = ['#'] * 10 