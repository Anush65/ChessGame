#Welcome to our 2 player chess game!!!

#This game follows all rules of chess!!!!!!! (lol you thought)


#Part one: Set up variables, images and game loop
import pygame

usernames = ['', '']

pygame.init() 
num = 8 #Size of the board

#game variables and images here
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_pieces2 = ['leftrook', 'leftknight', 'leftbishop', 'queen', 'king', 'rightbishop', 'rightknight', 'rightrook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations =  [(0,7), (1,7), (2, 7), (3,7), (4, 7), (5, 7), (6, 7), (7,7),
                    (0,6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)] #(column, row)
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_pieces2 = ['rightrook', 'rightknight', 'rightbishop', 'queen', 'king', 'leftbishop', 'leftknight', 'leftrook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations =  [(0,0), (1,0), (2, 0), (3,0), (4, 0), (5, 0), (6, 0), (7,0),
                    (0,1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
captured_pieces_white = [] #To keep track of what pieces are captured
captured_pieces_black = []

#0 - whites turn, no selection, 1 - whites turn, piece selection, 2 - blacks turn no selection, 3 - blacks turn piece selection
turn_step = 0
selection = 1000
valid_moves = [] #once a piece is selected, we have to display all valid moves

#dimensions of maximized window
max_size = (pygame.display.Info().current_w, pygame.display.Info().current_h - 63) #63 is the height of the sidebar @ minimum 

def titlescreen():

    global usernames

    screen = pygame.display.set_mode((960, 540))
    base_font = pygame.font.Font('freesansbold.ttf', 25)
    selection = None

    def draw_background():
        tmp_background = pygame.image.load('downloads\\images\\Titlescreen2.png')
        background = pygame.transform.scale(tmp_background, (960, 540))
        screen.blit(background, (0, 0))
    
    input_rect_white = pygame.Rect(966//2, 700//2, 190, 30)
    input_rect_black = pygame.Rect(966//2, 770//2, 190, 30)
    boxcolor = ['black', 'black']

    playbutton = pygame.Rect(424, 450, 100, 60)

    pygame.display.set_caption("2 Player Chess")
    run = True
    while run:
        for event in pygame.event.get(): #getting everything that is happening in the computer like click, etc
            if event.type == pygame.QUIT: #the little X in the top of the window
                run = False

            #Quit button
            if event.type == pygame.MOUSEBUTTONUP:
                if playbutton.collidepoint(event.pos):
                    run = False

            #selecting box
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_white.collidepoint(event.pos):
                    selection = 0
                elif input_rect_black.collidepoint(event.pos):
                    selection = 1
                else: selection = None

            #coloring selected box
            if selection == 0:
                boxcolor[0] = 'yellow'
            else: boxcolor[0] = 'black'
            if selection == 1:
                boxcolor[1] = 'yellow'
            else: boxcolor[1] = 'black'

            #entering text
            if event.type == pygame.KEYDOWN:
                if selection != None:
                    if event.key == pygame.K_BACKSPACE:
                        usernames[selection] = usernames[selection][:-1]
                    else: 
                        if text[selection].get_width() < 150:
                            usernames[selection] += event.unicode

        screen.fill("black")
        draw_background()

        #input boxes
        pygame.draw.rect(screen, boxcolor[0], input_rect_white, 2)
        pygame.draw.rect(screen, boxcolor[1], input_rect_black, 2)

        #rendering inputted text
        text = [base_font.render(usernames[0], True, 'black'), base_font.render(usernames[1], True, 'black')]
        screen.blit(text[0], (input_rect_white.x + 4, input_rect_white.y + 4))
        screen.blit(text[1], (input_rect_black.x + 4, input_rect_black.y + 4))

        #rendering playbutton
        pygame.draw.rect(screen, 'green', playbutton)
        pygame.draw.rect(screen, 'black', playbutton, 3)
        #rendering 'play'
        screen.blit(base_font.render('Play', True, 'black'), (playbutton.x + 23, playbutton.y + 20))

        input_rect_white.w = max(text[0].get_width() + 12, 100)
        input_rect_black.w = max(text[1].get_width() + 12, 100)

        pygame.display.flip()

    #accidentally interchanged indices oops (this fixes that)
    usernames[0], usernames[1] = usernames[1], usernames[0]
    
    #default usernames
    if usernames[0] == '': usernames[0] = 'Black'
    if usernames[1] == '': usernames[1] = 'White'

    pygame.quit()

titlescreen()

#initialize screen
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
size = width // num
transposx = 450
transposy = 100
pygame.display.set_caption('2 Player Chess') #Title of the window
font = pygame.font.Font('freesansbold.ttf', 21)
big_font = pygame.font.Font('freesansbold.ttf', 47)
timer = pygame.time.Clock()
fps = 50 #To just determine how smooth your game goes

#load in game pieces' images (queen, king, rook, knight, pawn, bishop) (each piece 2 times)
black_queen = pygame.image.load('downloads/images/bQ.png')
black_queen_small = pygame.transform.scale(black_queen, (60, 60))
#black_queen = pygame.image.scale(black_queen, (70,70)) dont think its needed rn
black_king = pygame.image.load('downloads/images/bK.png')
black_king_small = pygame.transform.scale(black_king, (60, 60))
black_rook = pygame.image.load('downloads/images/bR.png')
black_rook_small = pygame.transform.scale(black_rook, (60, 60))
black_bishop = pygame.image.load('downloads/images/bB.png')
black_bishop_small = pygame.transform.scale(black_bishop, (60, 60))
black_knight = pygame.image.load('downloads/images/bN.png')
black_knight_small = pygame.transform.scale(black_knight, (60, 60))
black_pawn = pygame.image.load('downloads/images/bp.png')
black_pawn_small = pygame.transform.scale(black_pawn, (60, 60))
white_queen = pygame.image.load('downloads/images/wQ.png')
white_queen_small = pygame.transform.scale(white_queen, (60, 60))
white_king = pygame.image.load('downloads/images/wK.png')
white_king_small = pygame.transform.scale(white_king, (60, 60))
white_rook = pygame.image.load('downloads/images/wR.png')
white_rook_small = pygame.transform.scale(white_rook, (60, 60))
white_bishop = pygame.image.load('downloads/images/wB.png')
white_bishop_small = pygame.transform.scale(white_bishop, (60, 60))
white_knight = pygame.image.load('downloads/images/wN.png')
white_knight_small = pygame.transform.scale(white_knight, (60, 60))
white_pawn = pygame.image.load('downloads/images/wp.png')
white_pawn_small = pygame.transform.scale(white_pawn, (60, 60))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop'] #this order is important because index needs to be aligned with the previous 2 lists
white_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
white_castled = False
white_enp = None, None
black_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
black_castled = False
black_enp = None, None

old = new = None

#check variables or flash counter
counter = 0
winner = ''
game_over = False


#draw main gameboard
def draw_board():
    #please decipher what logic
    for i in range(0, num - 1, 2):
        for j in range(0, num - 1, 2):
            rect = pygame.Rect(i*size + transposx, j*size + transposy, size, size)
            pygame.draw.rect(screen, '#edd6b0', rect)
        for j in range(1, num, 2):
            rect = pygame.Rect(i*size + transposx, j*size + transposy, size, size)
            pygame.draw.rect(screen, '#b88762', rect)
    for i in range(1, num, 2):
        for j in range(1, num, 2):
            rect = pygame.Rect(i*size + transposx, j*size + transposy, size, size)
            pygame.draw.rect(screen, '#edd6b0', rect)
        for j in range(0, num, 2):
            rect = pygame.Rect(i*size + transposx, j*size + transposy, size, size)
            pygame.draw.rect(screen, '#b88762', rect)
    
    pygame.draw.rect(screen, 'dark gray', [0 + transposx, 600 + transposy, 600, size])
    pygame.draw.rect(screen, 'dark gray', [600 + transposx, 0 + transposy, 200, 9 * size])
    pygame.draw.rect(screen, 'black', [0 + transposx, 600 + transposy, 8 * size + 2, size], 2)
    pygame.draw.rect(screen, 'black', [600 + transposx, 0 + transposy, 200, 9 * size], 2)
    pygame.draw.rect(screen, 'black', [8 * size + transposx, 8 * size + transposy, 200, size], 2)

    status_text = ['White: Select a piece to move!', "White: Select destination",
                   'Black: Select a piece to move!', "Black: Select destination"]
    screen.blit(font.render(status_text[turn_step], True, 'black'), (120 + transposx, 620 + transposy))

    if maximized:
        if turn_step < 2:
            black = 0
            white = 1
        else: 
            white = 0
            black = 1
        screen.blit(font.render(usernames[black], True, 'yellow'), (size * (-2) + transposx, 30 + transposy))
        screen.blit(font.render(usernames[white], True, 'yellow'), (size * (-2) + transposx, size * 7 + 30 + transposy))

    for i in range(9):
        pygame.draw.line(screen, 'black', (0 + transposx, 600//8 * i + transposy), (600 + transposx, (600//8) * i + transposy), 2)
        pygame.draw.line(screen, 'black', ((600//8) * i + transposx, 0 + transposy), ((600//8) * i + transposx, 600 + transposy), 2)
    screen.blit(font.render('Resign', True, 'black'), (660 + transposx, 620 + transposy))

#draw pieces onto the board
def draw_pieces(white_pieces, black_pieces, white_locations, black_locations): #btw draw_pieces needs to be after draw_board function since pieces are going to be on top of the board
    
    for i in range(len(white_pieces)):
        if (white_locations[i][0] + white_locations[i][1]) % 2 == 0:
            color = '#f6eb72'
        else:
            color = '#e0c44c'
        index = piece_list.index(white_pieces[i])
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, color, [white_locations[i][0] * 600//8 + 1 +2 + transposx, white_locations[i][1] * 600//8 + 1 +2 + transposy, 600//8 - 4, 600//8 - 4])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 600//8 + 8 + transposx, white_locations[i][1] * 600//8 + 10 + transposy))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 600//8 + 10 + transposx, white_locations[i][1] * 600//8 + 10 + transposy))
    for i in range(len(black_pieces)):
        if (black_locations[i][0] + black_locations[i][1]) % 2 == 0:
            color = '#f6eb72'
        else:
            color = '#e0c44c'
        index = piece_list.index(black_pieces[i])
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, color, [black_locations[i][0] * 600//8 + 1 +2 + transposx, black_locations[i][1] * 600//8 + 1 +2 + transposy, 600//8 - 4, 600//8 - 4])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 600//8 + 8 + transposx, black_locations[i][1] * 600//8 + 10 + transposy))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 600//8 + 10 + transposx, black_locations[i][1] * 600//8 + 10 + transposy))

def flip_pieces(white_locations, black_locations):
    #flip white
    for i in range(len(white_locations)):
        x = white_locations[i][0]; y = white_locations[i][1]
        white_locations[i] = (7 - x, 7 - y)
    #flip black
    for i in range(len(black_locations)):
        x = black_locations[i][0]; y = black_locations[i][1]
        black_locations[i] = (7 - x, 7 - y)

def incheck(whitepieces, blackpieces, whiteloc, blackloc, turn):
    if turn == 'white':
        if 'king' in whitepieces:
            king_index = whitepieces.index('king')
            king_location = whiteloc[king_index]
            # When checking if white king is in check, get all of black's moves
            black_options_for_incheck = check_options(blackpieces, blackloc, 'black') 
            for i in range(len(black_options_for_incheck)):
                if king_location in black_options_for_incheck[i]:
                    return True
    elif turn == 'black':
        if 'king' in blackpieces:
            king_index = blackpieces.index('king')
            king_location = blackloc[king_index]
            # When checking if black king is in check, get all of white's moves
            white_options_for_incheck = check_options(whitepieces, whiteloc, 'white')
            for i in range(len(white_options_for_incheck)):
                if king_location in white_options_for_incheck[i]:
                    return True
    return False

def is_checkmate(color):
    # Determine current player's and opponent's pieces/locations based on color
    current_player_pieces_init, current_player_locations_init, opponent_pieces_init, opponent_locations_init = [], [], [], []
    if color == 'white':
        current_player_pieces_init = white_pieces[:]
        current_player_locations_init = white_locations[:]
        opponent_pieces_init = black_pieces[:]
        opponent_locations_init = black_locations[:]
        current_player_all_options = check_options(current_player_pieces_init, current_player_locations_init, 'white')
    else: # color == 'black'
        current_player_pieces_init = black_pieces[:]
        current_player_locations_init = black_locations[:]
        opponent_pieces_init = white_pieces[:]
        opponent_locations_init = white_locations[:]
        current_player_all_options = check_options(current_player_pieces_init, current_player_locations_init, 'black')

    # 1. Check if the current player's king is in check using the *initial state for this check*.
    initial_check_status = False
    if color == 'white':
        initial_check_status = incheck(current_player_pieces_init, opponent_pieces_init, current_player_locations_init, opponent_locations_init, 'white')
    else: # color == 'black'
        initial_check_status = incheck(opponent_pieces_init, current_player_pieces_init, opponent_locations_init, current_player_locations_init, 'black')
    
    if not initial_check_status:
        return False # Not in check, so not checkmate

    # 2. If in check, iterate through all possible moves.
    for piece_index in range(len(current_player_all_options)):
        if piece_index >= len(current_player_pieces_init): 
            continue
        
        piece_moves = current_player_all_options[piece_index]
        for move in piece_moves:
            temp_curr_pieces = current_player_pieces_init[:]
            temp_curr_locations = current_player_locations_init[:]
            temp_opp_pieces = opponent_pieces_init[:]
            temp_opp_locations = opponent_locations_init[:]

            original_piece_location = temp_curr_locations[piece_index] 
            temp_curr_locations[piece_index] = move

            if move in temp_opp_locations:
                try:
                    captured_piece_idx = temp_opp_locations.index(move)
                    temp_opp_pieces.pop(captured_piece_idx)
                    temp_opp_locations.pop(captured_piece_idx)
                except ValueError:
                    pass 

            king_still_in_check = False
            if color == 'white':
                king_still_in_check = incheck(temp_curr_pieces, temp_opp_pieces, temp_curr_locations, temp_opp_locations, 'white')
            else: # color == 'black'
                king_still_in_check = incheck(temp_opp_pieces, temp_curr_pieces, temp_opp_locations, temp_curr_locations, 'black')
            
            if not king_still_in_check:
                return False 
    return True 

def is_stalemate(color):
    current_player_pieces_init, current_player_locations_init, opponent_pieces_init, opponent_locations_init = [], [], [], []
    if color == 'white':
        current_player_pieces_init = white_pieces[:]
        current_player_locations_init = white_locations[:]
        opponent_pieces_init = black_pieces[:]
        opponent_locations_init = black_locations[:]
        if incheck(current_player_pieces_init, opponent_pieces_init, current_player_locations_init, opponent_locations_init, 'white'):
            return False # In check, so not stalemate
        current_player_all_options = check_options(current_player_pieces_init, current_player_locations_init, 'white')
    else:  # color == 'black'
        current_player_pieces_init = black_pieces[:]
        current_player_locations_init = black_locations[:]
        opponent_pieces_init = white_pieces[:]
        opponent_locations_init = white_locations[:]
        if incheck(opponent_pieces_init, current_player_pieces_init, opponent_locations_init, current_player_locations_init, 'black'):
            return False # In check, so not stalemate
        current_player_all_options = check_options(current_player_pieces_init, current_player_locations_init, 'black')

    for piece_index in range(len(current_player_all_options)):
        if piece_index >= len(current_player_pieces_init): 
            continue
        
        piece_moves = current_player_all_options[piece_index]
        for move in piece_moves:
            temp_curr_pieces = current_player_pieces_init[:]
            temp_curr_locations = current_player_locations_init[:]
            temp_opp_pieces = opponent_pieces_init[:]
            temp_opp_locations = opponent_locations_init[:]
            
            temp_curr_locations[piece_index] = move

            if move in temp_opp_locations:
                try:
                    captured_piece_idx = temp_opp_locations.index(move)
                    temp_opp_pieces.pop(captured_piece_idx)
                    temp_opp_locations.pop(captured_piece_idx)
                except ValueError:
                    pass
            
            leaves_king_in_check = False
            if color == 'white':
                leaves_king_in_check = incheck(temp_curr_pieces, temp_opp_pieces, temp_curr_locations, temp_opp_locations, 'white')
            else: # color == 'black'
                leaves_king_in_check = incheck(temp_opp_pieces, temp_curr_pieces, temp_opp_locations, temp_curr_locations, 'black')
            
            if not leaves_king_in_check:
                return False # Found a legal move
                
    return True # No legal moves found, and not in check

def check_enpassant(old, new):
    if turn_step < 2:
        index = white_locations.index(old)
        enpassant = (7-new[0], 7- (new[1] + 1)) 
        piece = white_pieces[index]
    else:
        index = black_locations.index(old)
        enpassant = ( 7-new[0],  7- (new[1] + 1))
        piece = black_pieces[index]
    if piece == 'pawn' and abs(old[1] - new[1]) > 1:
        pass
    else: enpassant = (None, None)
    return enpassant

def check_options(pieces, locations, turn): 
    moves_list = []
    all_moves_list = [] 
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn) 
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_pawn(position, color): 
    moves_list = []
    if color == 'white':
        friends_list = white_locations 
        enemies_list = black_locations 
        en_passant_own = white_enp 
        
        if (position[0], position[1] - 1) not in friends_list and \
           (position[0], position[1] - 1) not in enemies_list and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if position[1] == 6 and \
           (position[0], position[1] - 2) not in friends_list and \
           (position[0], position[1] - 2) not in enemies_list and \
           (position[0], position[1] - 1) not in friends_list and \
           (position[0], position[1] - 1) not in enemies_list: 
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in enemies_list:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in enemies_list:
            moves_list.append((position[0] - 1, position[1] - 1))
        if en_passant_own != (None, None) and position[1] == 3: 
            if en_passant_own == (position[0] + 1, position[1] - 1) or \
               en_passant_own == (position[0] - 1, position[1] - 1):
                 moves_list.append(en_passant_own)

    else:  # color == 'black'
        friends_list = black_locations 
        enemies_list = white_locations 
        en_passant_own = black_enp 
        
        if (position[0], position[1] - 1) not in friends_list and \
           (position[0], position[1] - 1) not in enemies_list and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if position[1] == 6 and \
           (position[0], position[1] - 2) not in friends_list and \
           (position[0], position[1] - 2) not in enemies_list and \
           (position[0], position[1] - 1) not in friends_list and \
           (position[0], position[1] - 1) not in enemies_list:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in enemies_list:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in enemies_list:
            moves_list.append((position[0] - 1, position[1] - 1))
        if en_passant_own != (None, None) and position[1] == 3: 
            if en_passant_own == (position[0] + 1, position[1] - 1) or \
               en_passant_own == (position[0] - 1, position[1] - 1):
                moves_list.append(en_passant_own)
    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == 'white': 
        enemies_list = black_locations
        friends_list = white_locations
    else: 
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4): 
        path = True 
        chain = 1
        if i == 0: x, y = 0, 1
        elif i == 1: x, y = 0, -1
        elif i == 2: x, y = 1, 0
        else: x, y = -1, 0
        while path:
            target_col, target_row = position[0] + (chain * x), position[1] + (chain * y)
            if 0 <= target_col <= 7 and 0 <= target_row <= 7:
                if (target_col, target_row) not in friends_list:
                    moves_list.append((target_col, target_row))
                    if (target_col, target_row) in enemies_list: 
                        path = False
                    chain += 1
                else: path = False
            else: path = False
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white': friends_list = white_locations
    else: friends_list = black_locations
    targets = [(1,2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for t in targets: 
        target_col, target_row = position[0] + t[0], position[1] + t[1]
        if 0 <= target_col <= 7 and 0 <= target_row <= 7:
            if (target_col, target_row) not in friends_list:
                moves_list.append((target_col, target_row))
    return moves_list

def check_bishop(position, color): 
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4): 
        path = True 
        chain = 1
        if i == 0: x,y = 1, -1
        elif i == 1: x,y = -1, -1
        elif i == 2: x,y = 1, 1
        else: x,y = -1, 1
        while path:
            target_col, target_row = position[0] + (chain*x), position[1] + (chain*y)
            if 0 <= target_col <= 7 and 0 <= target_row <= 7:
                if (target_col, target_row) not in friends_list:
                    moves_list.append((target_col, target_row))
                    if (target_col, target_row) in enemies_list:  
                        path = False
                    chain += 1
                else: path = False
            else: path = False
    return moves_list

def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    moves_list += second_list
    return moves_list

def check_king(position, color): 
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else: 
        friends_list = black_locations

    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for t in targets:
        target_col, target_row = position[0] + t[0], position[1] + t[1]
        if 0 <= target_col <= 7 and 0 <= target_row <= 7:
            if (target_col, target_row) not in friends_list:
                moves_list.append((target_col, target_row))
    return moves_list

def check_valid_moves():
    tmp_white_pieces_init = white_pieces[:]
    tmp_black_pieces_init = black_pieces[:]
    tmp_white_locations_init = white_locations[:]
    tmp_black_locations_init = black_locations[:]
    
    valid_options = [] 

    if turn_step < 2: 
        all_player_options = white_options 
        current_player_pieces_orig = tmp_white_pieces_init
        current_player_locations_orig = tmp_white_locations_init
        opponent_pieces_orig = tmp_black_pieces_init
        opponent_locations_orig = tmp_black_locations_init
        current_turn_string = 'white'
    else: 
        all_player_options = black_options
        current_player_pieces_orig = tmp_black_pieces_init
        current_player_locations_orig = tmp_black_locations_init
        opponent_pieces_orig = tmp_white_pieces_init
        opponent_locations_orig = tmp_white_locations_init
        current_turn_string = 'black'

    if selection >= len(all_player_options) or selection < 0 or \
       not all_player_options[selection] or selection >= len(current_player_pieces_orig): 
        return [] 

    for move in all_player_options[selection]:
        temp_current_player_pieces = current_player_pieces_orig[:]
        temp_current_player_locations = current_player_locations_orig[:]
        temp_opponent_pieces = opponent_pieces_orig[:]
        temp_opponent_locations = opponent_locations_orig[:]

        if selection >= len(temp_current_player_locations): 
            continue

        temp_current_player_locations[selection] = move 

        if move in temp_opponent_locations: 
            try:
                opponent_piece_index = temp_opponent_locations.index(move)
                temp_opponent_pieces.pop(opponent_piece_index)
                temp_opponent_locations.pop(opponent_piece_index)
            except ValueError: 
                pass 
        
        if current_turn_string == 'white':
            is_in_check = incheck(temp_current_player_pieces, temp_opponent_pieces, temp_current_player_locations, temp_opponent_locations, current_turn_string)
        else: 
            is_in_check = incheck(temp_opponent_pieces, temp_current_player_pieces, temp_opponent_locations, temp_current_player_locations, current_turn_string)
        
        if not is_in_check:
            valid_options.append(move)
            
    return valid_options

def draw_valid(moves):
    for i in range(len(moves)):
        if (moves[i][0] + moves[i][1]) % 2 == 0: 
            color = '#d5c09e' 
            capture = '#f07c64'
        else: 
            color = '#a57958' 
            capture = '#e86c54'
        if moves[i] in white_locations or moves[i] in black_locations:
            pygame.draw.rect(screen, capture, [moves[i][0] * 600//8 + 1 + transposx, moves[i][1] * 600//8 + 1 + transposy, 600//8, 600//8], 5)
        else: 
            pygame.draw.circle(screen, color, (moves[i][0] * (600//8) + 40 + transposx, moves[i][1] * (600//8) + 40 + transposy), 12)
            
def draw_check():

        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            if (white_locations[king_index][0] + white_locations[king_index][1]) % 2 == 0:
                color = '#f07c64'
            else: 
                color = '#e86c54'
            king_location = white_locations[king_index]
            if black_options and any(king_location in opt_list for opt_list in black_options if opt_list):
                if counter < 15:
                    pygame.draw.rect(screen, color, (white_locations[king_index][0] * size + 1 +2 + transposx,
                                                        white_locations[king_index][1] * size + 1 +2 + transposy, 600//8 - 4, 600//8 - 4))

        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            if (black_locations[king_index][0] + black_locations[king_index][1]) % 2 == 0:
                color = '#f07c64'
            else: 
                color = '#e86c54'
            king_location = black_locations[king_index]
            if white_options and any(king_location in opt_list for opt_list in white_options if opt_list):
                if counter < 15:
                    pygame.draw.rect(screen, color, [black_locations[king_index][0] * size + 1 +2 + transposx,
                                                        black_locations[king_index][1] * size + 1 +2 + transposy, 600//8 - 4, 600//8 - 4])

def draw_prev(old, new):
    for pos in old, new:
        pos = 7-pos[0], 7-pos[1]
        if (pos[0] + pos[1]) % 2 == 0: 
            color = '#f6eb72' 
        else: 
            color = '#e0c44c' 
        pygame.draw.rect(screen, color, [pos[0] * size + 1 +2 + transposx, pos[1] * size + 1 +2 + transposy, 600//8 - 4, 600//8 - 4])

def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (625 + transposx, 5 + 50 * i + transposy))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (725 + transposx, 5 + 50 * i + transposy))

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200 + transposx - 70, 220 + transposy, 340, 100]) 
    if winner == 'DRAW':
        screen.blit(big_font.render(f'Stalemate!', True, 'blue'), (200 + transposx - 50, 230 + transposy))
        screen.blit(font.render(f'Game is a Draw.', True, 'yellow'), (200 + transposx - 30, 275 + transposy))
    else:
        if winner == 'White': winner_name = usernames[1]
        else: winner_name = usernames[0]
        screen.blit(big_font.render(f'Checkmate!', True, 'red'), (200 + transposx - 40, 230 + transposy))
        screen.blit(font.render(f'{winner_name} wins!', True, 'yellow'), (200 + transposx, 275 + transposy)) 
    screen.blit(font.render(f'Press ENTER for new game', True, 'yellow'), (160 + transposx, 300 + transposy))

#main game loop
black_options = check_options(black_pieces,black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    
    window_size = pygame.display.get_window_size()
    maximized = False
    if window_size == max_size: 
        transposx, transposy = 450, 100
        maximized = True
    else:
        transposx, transposy = 0, 0
        maximized = False
    screen.fill('black') 
    draw_board()
    if old != None and new != None:
        draw_prev(old, new)
    draw_check()
    draw_pieces(white_pieces, black_pieces, white_locations, black_locations)
    draw_captured()

    
    if selection != 1000:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves) 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = (event.pos[0] - transposx) // (600//8) 
            y_coord = (event.pos[1] - transposy) // (600//8)
            click_coords = (x_coord, y_coord)
            if turn_step < 2: # White's turn logic
                if click_coords == (8, 8) or click_coords == (9,8): 
                    winner = 'Black'
                    game_over = True 
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1 
                if click_coords in valid_moves and selection != 1000:
                    black_enp = check_enpassant(white_locations[selection], click_coords) 
                    old, new = white_locations[selection], click_coords
                    white_locations[selection] = click_coords
                    
                    if click_coords == white_enp: 
                        black_piece_idx = black_locations.index((click_coords[0], click_coords[1] + 1))
                        captured_pieces_white.append(black_pieces[black_piece_idx])
                        black_pieces.pop(black_piece_idx)
                        black_pieces2.pop(black_piece_idx) 
                        black_locations.pop(black_piece_idx)
                        if black_piece_idx < len(black_moved): black_moved.pop(black_piece_idx)

                    if white_pieces[selection] == 'king' and not white_moved[selection]: 
                        king_idx_for_castle_check = white_pieces.index('king') 
                        if white_locations[king_idx_for_castle_check] == (6, 7): 
                            white_castled = True
                            rook_idx = white_locations.index((7, 7))
                            white_locations[rook_idx] = (5, 7)
                        elif white_locations[king_idx_for_castle_check] == (2, 7): 
                            white_castled = True
                            rook_idx = white_locations.index((0, 7))
                            white_locations[rook_idx] = (3, 7)
                    white_moved[selection] = True
                    
                    if click_coords in black_locations: 
                        black_piece_idx = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece_idx])
                        # Removed: if black_pieces[black_piece_idx] == 'king': winner = 'White'; game_over = True
                        black_pieces.pop(black_piece_idx)
                        black_pieces2.pop(black_piece_idx)
                        black_locations.pop(black_piece_idx)
                        if black_piece_idx < len(black_moved): black_moved.pop(black_piece_idx)
                    
                    if not game_over: 
                        turn_step = 2 
                        selection = 1000
                        valid_moves = []
                        click_coords = None
                        flip_pieces(white_locations, black_locations)
                        black_options = check_options(black_pieces,black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        if is_stalemate('black'):
                            winner = 'DRAW'
                            game_over = True
                        elif not game_over and is_checkmate('black'): 
                             winner = 'White'
                             game_over = True

            elif turn_step >= 2: # Black's turn logic
                if click_coords == (8,8) or click_coords == (9,8): 
                    winner = 'White'
                    game_over = True 
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3 
                if click_coords in valid_moves and selection != 1000:
                    white_enp = check_enpassant(black_locations[selection], click_coords)
                    old, new = black_locations[selection], click_coords
                    black_locations[selection] = click_coords

                    if click_coords == white_enp: 
                        white_piece_idx = white_locations.index((click_coords[0], click_coords[1] + 1))
                        captured_pieces_black.append(white_pieces[white_piece_idx]) 
                        white_pieces.pop(white_piece_idx)
                        white_pieces2.pop(white_piece_idx)
                        white_locations.pop(white_piece_idx)
                        if white_piece_idx < len(white_moved): white_moved.pop(white_piece_idx)
                    
                    king_idx_for_black_castle = black_pieces.index('king') 
                    if black_pieces[selection] == 'king' and not black_moved[king_idx_for_black_castle]: 
                        if black_locations[king_idx_for_black_castle] == (5, 0): 
                            black_castled = True
                            rook_idx = black_locations.index((7, 0))
                            black_locations[rook_idx] = (4, 0)
                        elif black_locations[king_idx_for_black_castle] == (1, 0): 
                            black_castled = True
                            rook_idx = black_locations.index((0, 0))
                            black_locations[rook_idx] = (2, 0)
                    black_moved[selection] = True

                    if click_coords in white_locations: 
                        white_piece_idx = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece_idx])
                        # Removed: if white_pieces[white_piece_idx] == 'king': winner = 'Black'; game_over = True
                        white_pieces.pop(white_piece_idx)
                        white_pieces2.pop(white_piece_idx)
                        white_locations.pop(white_piece_idx)
                        if white_piece_idx < len(white_moved): white_moved.pop(white_piece_idx)
                    
                    if not game_over: 
                        turn_step = 0 
                        selection = 1000
                        valid_moves = []
                        click_coords = None
                        flip_pieces(white_locations, black_locations)
                        black_options = check_options(black_pieces,black_locations, 'black')
                        white_options = check_options(white_pieces, white_locations, 'white')
                        if is_stalemate('white'):
                            winner = 'DRAW'
                            game_over = True
                        elif not game_over and is_checkmate('white'): 
                            winner = 'Black'
                            game_over = True

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_pieces2 = ['leftrook', 'leftknight', 'leftbishop', 'queen', 'king', 'rightbishop', 'rightknight', 'rightrook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)] 
                black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_pieces2 = ['rightrook', 'rightknight', 'rightbishop', 'queen', 'king', 'leftbishop', 'leftknight', 'leftrook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                white_moved = [False, False, False, False, False, False, False, False, 
                   False, False, False, False, False, False, False, False]
                black_moved = [False, False, False, False, False, False, False, False, 
                   False, False, False, False, False, False, False, False]
                captured_pieces_white = [] 
                captured_pieces_black = []
                turn_step = 0
                selection = 1000
                valid_moves = []
                
                # Board state reset, then flip to black's perspective for black_options, then flip back for white's turn
                # This is to match the game start where white_options are for white's first move.
                if turn_step == 0 : #If it's white's turn (after reset)
                    black_options = check_options(black_pieces, black_locations, 'black') # Black options from black's perspective
                    white_options = check_options(white_pieces, white_locations, 'white') # White options from white's perspective
                else: # Should not happen if reset properly sets turn_step to 0
                    flip_pieces(white_locations, black_locations) 
                    white_options = check_options(white_pieces, white_locations, 'white')
                    flip_pieces(white_locations, black_locations) 
                    black_options = check_options(black_pieces, black_locations, 'black')


    if winner != '' and not game_over: 
        game_over = True 
    
    if game_over: 
        draw_game_over()

    pygame.display.flip() 

pygame.quit()
