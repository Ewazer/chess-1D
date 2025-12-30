import re
import copy

coordinate = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h"
}

piece_note_style = {
    5: "♖",   
    3: "♘",  
    7: "♔", 
    -3: "♞", 
    -7: "♚",
    -5: "♜", 
    0: " "    
}

def board_print(board, style=True):
    if style:
        print([piece_note_style[e] for e in board])
    else:
        print(board)
    print(["a","b","c","d","e","f","g","h"])


def give_info_move(move):
    move_num = [coordinate[move[0]],coordinate[move[1]]]
    
    start_value = board[move_num[0]-1]
    end_value = board[move_num[1]-1]
 
    if abs(start_value) != 1 and ((start_value>0 and end_value>0) or (start_value<0 and end_value<0) or start_value==0):
        return None
        
    info_move = {
        "move":move,
        "move num":move_num,
        "start value":start_value,
        "end value":end_value,
        "switch": 0
    }
    return info_move

def valid_rook_move(info_move):
    for i in range(info_move["move num"][0]+1,info_move["move num"][1]):
        if board[i-1] != 0:
            return 'invalid'
    return 'valid'

def valid_king_move(info_move):
    if abs(info_move["move num"][0] - info_move["move num"][1]) != 1:
        return 'invalid'
    return 'valid'

def valid_knight_move(info_move):
    if abs(info_move["move num"][0] - info_move["move num"][1]) != 2:
        return 'invalid'
    return 'valid'

def list_rook_move(index):
    new_move = []
    if board[index] == 5:
        for i in range(index+1,8):
            if board[i] == 0:
                new_move.append([index,i])
            else:
                break
        if index+1 < 8:
            if board[index+1] < 0:
                new_move.append([index,index+1])
        for i in range(index-1,0,-1):
            if board[i] == 0:
                new_move.append([index,i])
            else:
                break
        if index-1 > 0:
            if board[index-1] < 0:
                new_move.append([index,index-1])
        return new_move
    else:
        for i in range(index+1,8):
            if board[i] == 0:
                new_move.append([index,i])
            else:
                break
        if index+1 < 8:
            if board[index+1] > 0:
                new_move.append([index,index+1])
        for i in range(index-1,0,-1):
            if board[i] == 0:
                new_move.append([index,i])
            else:
                break
        if index-1 > 0:
            if board[index-1] > 0:
                new_move.append([index,index-1])
        return new_move

def list_king_move(index):
    new_move = []
    if board[index] == 7:
        if index+1 < 8:
            if board[index+1] <= 0:
                new_move.append([index,index+1])
        if index-1 > 0:
            if board[index-1] <= 0:
                new_move.append([index,index-1])
        return new_move
    else:
        if index-1 > 0:
            if board[index-1] >= 0:
                new_move.append([index,index-1])
        if index+1 < 8:
            if board[index+1] >= 0:
                new_move.append([index,index+1])
        return new_move


def list_knight_move(index):
    new_move = []
    if board[index] == 3:
        if index+2 < 8:
            if board[index+2] <= 0:
                new_move.append([index,index+2])
        if index-2 > 0:
            if board[index-2] <= 0:
                new_move.append([index,index-2])   
        return new_move
    else:
        if index-2 > 0:
            if board[index-2] >= 0:
                new_move.append([index,index-2])
        if index+2 < 8:
            if board[index+2] >= 0:
                new_move.append([index,index+2])
        return new_move
        

def list_legal_move():
    move_legal = []
    for i in range(len(board)):
        if board[i] != 0:
            new_move = []
            if board[i] == 5:
                new_move = list_rook_move(i)
            elif board[i] == 3:
                new_move = list_knight_move(i)
            elif board[i] == 7:
                new_move = list_king_move(i)
            elif board[i] == -5:
                new_move = list_rook_move(i)
            elif board[i] == -3:
                new_move = list_knight_move(i)
            elif board[i] == -7:
                new_move = list_king_move(i)
            if new_move != []:
                for n in new_move:
                    new_board = copy.deepcopy(board)
                    new_board[n[0]] = 0
                    new_board[n[1]] = board[n[0]]
                    if is_check("black" if board[n[0]] < 0 else "white",new_board) != 'check':
                        move_legal.append(new_move)
    return move_legal

def black_list_legal_move():
    move_legal = []
    for i in range(len(board)):
        if board[i] != 0:
            new_move = []
            if board[i] == -5:
                new_move = list_rook_move(i)
            elif board[i] == -3:
                new_move = list_knight_move(i)
            elif board[i] == -7:
                new_move = list_king_move(i)
            if new_move != []:
                for n in new_move:
                    new_board = copy.deepcopy(board)
                    new_board[n[0]] = 0
                    new_board[n[1]] = board[n[0]]
                    if is_check("black" if board[n[0]] < 0 else "white",new_board) != 'check':
                        move_legal.append(new_move)
    return move_legal

def white_list_legal_move():
    move_legal = []
    for i in range(len(board)):
        if board[i] != 0:
            new_move = []
            if board[i] == 5:
                new_move = list_rook_move(i)
            elif board[i] == 3:
                new_move = list_knight_move(i)
            elif board[i] == 7:
                new_move = list_king_move(i)
            if new_move != []:
                for n in new_move:
                    new_board = copy.deepcopy(board)
                    new_board[n[0]] = 0
                    new_board[n[1]] = board[n[0]]
                    if is_check("black" if board[n[0]] < 0 else "white",new_board) != 'check':
                        move_legal.append(new_move)
    return move_legal
        

def find_piece(board,piece):
    for i in range(len(board)):
        if board[i] == piece:
            return i

def is_check(color,board):
    if color == "white":
        white_king_position = find_piece(board,7)

        if white_king_position + 2 < 8:
            if board[white_king_position + 2] == -3:
                return 'check'
            
        if white_king_position - 2 > 0:
            if board[white_king_position - 2] == -3:
                return 'check'
        
        for i in range(white_king_position+1,8):
            if board[i] == -5:
                return 'check'
            elif board[i] != 0:
                break
        for i in range(white_king_position-1,0,-1):
            if board[i] == -5:
                return 'check'
            elif board[i] != 0:
                break
    
    elif color == "black":
        black_king_position = find_piece(board,-7)

        if black_king_position + 2 < 8:
            if board[black_king_position + 2] == 3:
                return 'check'
            
        if black_king_position - 2 > 0:
            if board[black_king_position - 2] == 3:
                return 'check'
        
        for i in range(black_king_position+1,8):
            if board[i] == 5:
                return 'check'
            elif board[i] != 0:
                break
        for i in range(black_king_position-1,0,-1):
            if board[i] == 5:
                return 'check'
            elif board[i] != 0:
                break

    return None

def enough_material():
    for piece in board:
        if abs(piece) == 5:
            return True
    return False

def play_chess():
    global board
    board = [7, 3, 5, 0, 0,-5,-3,-7]
    done = False
    i = 0
    while not done:
        while True:
            if i == 0:
                print("⚪---white play---⚪")
            else:
                print("⚫---black play---⚫")
            board_print(board)
            while True:
                move = input("Enter move (ex: ah): ")
                if bool(re.match(r'^[a-h][a-h]$', move)):
                    info_move = give_info_move(move)
                    if info_move:
                        if i == 0 and info_move["start value"] > 0:
                            break
                        if i == 1 and info_move["start value"] < 0:
                            break
                    else:
                        print("🚫---invalide move---🚫")
                        print()
                else:
                    print("🚫---invalide move---🚫 => valide move example: ✅--- ah ---✅")
                    print()
            if abs(info_move['start value']) == 5:
                if valid_rook_move(info_move) != 'valid':
                    print("🚫---invalide move---🚫")
                    print()
                    break
            elif abs(info_move['start value']) == 7:
                if valid_king_move(info_move) != 'valid':
                    print("🚫---invalide move---🚫")
                    print()
                    pass 
            elif abs(info_move['start value']) == 3:
                if valid_knight_move(info_move) != 'valid':
                    print("🚫---invalide move---🚫")
                    print()
                    pass        
            else:
                print("🚫---invalide move---🚫")
                print()
                break
            
            if info_move['start value'] == 3:
                new_board = copy.deepcopy(board)
                new_board[info_move["move num"][0]-1] = 0 
                if is_check("white",new_board):
                    print(f"🚫---white is in check when the knight jumps 🙃---🚫")
                    print()
                    break

            if info_move['start value'] == -3:
                new_board = copy.deepcopy(board)
                new_board[info_move["move num"][0]-1] = 0 
                if is_check("black",new_board):
                    print(f"🚫---black is in check when the knight jumps 🙃---🚫")
                    print()
                    break

            if is_check("black",board):
                new_board = copy.deepcopy(board)
                new_board[info_move["move num"][0]-1] = info_move['switch'] 
                new_board[info_move["move num"][1]-1] = info_move["start value"]
                if is_check("black",new_board):
                    print(f"🚫---invalide move black is in check---🚫")
                    print()
                    break

            if is_check("white",board):
                new_board = copy.deepcopy(board)
                new_board[info_move["move num"][0]-1] = info_move['switch'] 
                new_board[info_move["move num"][1]-1] = info_move["start value"]
                if is_check("white",new_board):
                    print(f"🚫---invalide move white is in check---🚫")
                    print()
                    break
                
            board[info_move["move num"][0]-1] = info_move['switch']
            board[info_move["move num"][1]-1] = info_move["start value"]

            opponent_move = black_list_legal_move() if i == 0 else white_list_legal_move()

            if opponent_move == []:
                if is_check("white" if i == 1 else "black",board) == 'check':
                    print()
                    print("👍---🏁 Finish! Mat---👍")
                    print()
                    done = True
                    board_print(board)
                    break
                else:
                    print()
                    print("👎---🏁 Finish! pat---👎")
                    print()
                    done = True
                    board_print(board)
                    break
            if enough_material()==False:
                print()
                print("👎---🏁 Finish! enough material---👎")
                print()
                done = True
                board_print(board)
                break
            print()
            i = 1 if i == 0 else 0

        if done == True:
            break

play_chess()
