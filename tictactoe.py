# this program is tic tac toe game




# the show_board function display board 
def show_board(board):
	print(board[0], board[1], board[2])
	print(board[3], board[4], board[5])
	print(board[6], board[7], board[8])
	
# the ask_move function ask player to make its move
def ask_move(player, board):
	print('player ', player, ' its your turn!')
	room_num = int(input('enter your selected room number:'))
	board[room_num - 1] = player
	return board
	
	
# the evaluate_board function evaluate the board and update the game_status
def evaluate_board(board):
        return 'go'


# the switch_turn function change turn to other player
def switch_player(player):
        if player == 'x':
                next_player = 'o'
        else:
                next_player = 'x'
        return next_player

		
# the show_result function print the winner or tie
def show_result():
	if game_status == 'win':
		print('player ', player, ' won!')
	else:
		print('game finished tie!')
		
def main():
        game_status = 'go'
        player = 'x'
        board = ['1','2','3','4','5','6','7','8','9']
        while game_status == 'go' :
                player = switch_player(player)
                show_board(board)
                board = ask_move(player, board)
                game_status = evaluate_board(board)
        show_result(game_status)
	
	
			
main()		
