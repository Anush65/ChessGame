#Welcome to our 2 player chess game!!!

#This game follows all rules of chess!!!!!!! (lol you thought)


#Part one: Set up variables, images and game loop
import pygame
pygame.init() 
num = 8 #Size of the board
width = 600
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
size = width // num
pygame.display.set_caption('2 Player Chess') #Title of the window
font = pygame.font.Font('freesansbold.ttf', 21)
big_font = pygame.font.Font('freesansbold.ttf', 47)
timer = pygame.time.Clock()
fps = 50 #To just determine how smooth your game goes
#game variables and images here
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations =  [(0,7), (1,7), (2, 7), (3,7), (4, 7), (5, 7), (6, 7), (7,7),
                    (0,6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)] #(column, row)
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations =  [(0,0), (1,0), (2, 0), (3,0), (4, 0), (5, 0), (6, 0), (7,0),
                    (0,1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
captured_pieces_white = [] #To keep track of what pieces are captured
captured_pieces_black = []

#0 - whites turn, no selection, 1 - whites turn, piece selection, 2 - blacks turn no selection, 3 - blacks turn piece selection
turn_step = 0
selection = 1000
valid_moves = [] #once a piece is selected, we have to display all valid moves

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
black_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
#check variables or flash counter
counter = 0
winner = ''
game_over = False

#draw main gameboard
def draw_board():
    #please decipher what logic
    for i in range(0, num - 1, 2):
        for j in range(0, num - 1, 2):
            rect = pygame.Rect(i*size, j*size, size, size)
            pygame.draw.rect(screen, '#edd6b0', rect)
    for i in range(1, num, 2):
        for j in range(1, num, 2):
            rect = pygame.Rect(i*size, j*size, size, size)
            pygame.draw.rect(screen, '#edd6b0', rect)
    pygame.draw.rect(screen, 'light gray', [0, 600, 800, size])
    pygame.draw.rect(screen, 'gold', [0, 600, 800, size], 5)
    pygame.draw.rect(screen, 'light gray', [600, 0, 200, 800])
    pygame.draw.rect(screen, 'gold', [600, 0, 200, 800], 5)

    status_text = ['White: select a piece to move!', "White: Select pieces' destination",
                   'Black: select a piece to move!', "Black: Select pieces' destination"]
    screen.blit(font.render(status_text[turn_step], True, 'red'), (120, 620))
    for i in range(9):
        pygame.draw.line(screen, 'black', (0,600//8 * i), (600, (600//8) * i), 2)
        pygame.draw.line(screen, 'black', ((600//8) * i,0), ((600//8) * i, 600), 2)
    screen.blit(font.render('You QUIT!?', True, 'orange'), (630, 610))

#draw pieces onto the board
def draw_pieces(): #btw draw_pieces needs to be after draw_board function since pieces are going to be on top of the board
    
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 600//8 + 8, white_locations[i][1] * 600//8 + 10))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 600//8 + 10, white_locations[i][1] * 600//8 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, '#f6eb72', [white_locations[i][0] * 600//8 + 1, white_locations[i][1] * 600//8 + 1,600//8, 600//8], 5)
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 600//8 + 8, black_locations[i][1] * 600//8 + 10))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 600//8 + 10, black_locations[i][1] * 600//8 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, '#f6eb72', [black_locations[i][0] * 600//8 + 1, black_locations[i][1] * 600//8 + 1,600//8, 600//8], 5)

def flip_pieces():
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
        options = check_options(blackpieces, blackloc, 'black')
        for piece in options:
            if whiteloc[whitepieces.index('king')] in piece: 
                return True
    if turn == 'black':
        options = check_options(whitepieces, whiteloc, 'white')
        for piece in options:
            if blackloc[blackpieces.index('king')] in piece: 
                return True
    return False


#function to check all valid options for the piece to move
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = [] #use moves_list to calculate and append to this list
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
    #going to return list of all possible moves (valid)
    return all_moves_list

#Check all valid moves for all pieces
#1.Pawn moves
def check_pawn(position, color):
    moves_list = []

    #white bottom
    if turn_step < 2:
        if color == 'white':
            #last condition to check if the piece on last square
            if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations \
                and position[1] > 0: 
                moves_list.append((position[0], position[1] - 1))
            # last condition to check if the pawn in initial position
            if (position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations \
                and position[1] == 6 and (position[0], position[1] - 1) not in black_locations and (position[0], position[1] - 1) not in white_locations: 
                moves_list.append((position[0], position[1] - 2))
            if (position[0] + 1, position[1] - 1) in black_locations:
                moves_list.append((position[0] + 1, position[1] - 1))
            if (position[0] - 1, position[1] - 1) in black_locations:
                moves_list.append((position[0] - 1, position[1] - 1))
        else:
            # last condition to check if the piece on last square
            if (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations \
                        and position[1] < 7 :  
                    moves_list.append((position[0], position[1] + 1))
            # last condition to check if the pawn in initial position
            if (position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations \
                        and position[1] == 1 and (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations:  # last condition to check if the pawn in initial position
                    moves_list.append((position[0], position[1] + 2))
            if (position[0] + 1, position[1] + 1) in white_locations:
                    moves_list.append((position[0] + 1, position[1] + 1))
            if (position[0] - 1, position[1] + 1) in white_locations:
                    moves_list.append((position[0] - 1, position[1] + 1))

    #black bottom
    else:
        if color == 'white':
            if (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations \
                and position[1] < 7: #last condition to check if the piece on last square
                moves_list.append((position[0], position[1] + 1))
            if (position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations \
                and position[1] == 1: #last condition to check if the pawn in initial position
                moves_list.append((position[0], position[1] + 2))
            if (position[0] + 1, position[1] + 1) in black_locations:
                moves_list.append((position[0] + 1, position[1] + 1))
            if (position[0] - 1, position[1] + 1) in black_locations:
                moves_list.append((position[0] - 1, position[1] + 1))
        else:
            if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations \
                        and position[1] > 0 :  # last condition to check if the piece on last square
                    moves_list.append((position[0], position[1] - 1))
            if (position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations \
                        and position[1] == 6:  # last condition to check if the pawn in initial position
                    moves_list.append((position[0], position[1] - 2))
            if (position[0] + 1, position[1] - 1) in white_locations:
                    moves_list.append((position[0] + 1, position[1] - 1))
            if (position[0] - 1, position[1] - 1) in white_locations:
                    moves_list.append((position[0] - 1, position[1] - 1))
    
        

    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4): #down up right left
        path = True #to check if path is valid (taken by the rook)
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) \
                not in friends_list and 0 <= position[0] + (chain*x) <= 7 and \
                0 <= position[1] + (chain*y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain*y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) \
                in enemies_list: #if enemy piece is there we can't go further
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    # 8 squares to check for knight
    # they can go 2 squares in one direction, then one to left or right
    #up - -1, down - 1, right - 2, left - 1
    targets = [(1,2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8): #for all 8 possible moves
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <=target[0] <= 7 and \
            0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list

def check_bishop(position, color): #similar to rook
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    # similar to rook but diagonal
    for i in range(4): #up-right, up-left, down-right, down-left
        path = True #to check if path is valid (taken by the bishop)
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        elif i == 3:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) \
                    not in friends_list and 0 <= position[0] + (chain * x) <= 7 and \
                    0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) \
                        in enemies_list:  # if enemy piece is there we can't go further
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    moves_list += second_list
    return moves_list

def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
        if white_moved[4] == False: 
            if white_moved[7] == False and (5, 7) not in white_locations:
                moves_list.append((6, 7))
            if white_moved[0] == False and (3, 7) not in white_locations and (2, 7) not in white_locations and (1, 7) not in white_locations:
                moves_list.append((2, 7))
    else:
        friends_list = black_locations
        enemies_list = white_locations
        if black_moved[4] ==  False:
            if black_moved[7] == False and (5, 7) not in black_locations and (4,7) not in black_locations and (6,7) not in black_locations:
                moves_list.append((5, 7))
            if black_moved[0] == False and (2, 7) not in black_locations and (1, 7) not in black_locations:
                moves_list.append((1, 7))
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_valid_moves():
    if turn_step < 2: #and turn_step == 1
        options_list = white_options
        #checking next move (doesn't work)
        '''tmp_black_pieces = black_pieces[::]
        tmp_white_pieces = white_pieces[::]
        tmp_white_locations = white_locations[::]
        tmp_black_locations = black_locations[::]
        #simulate every move
        for i in options_list[selection]:
            print(selection)
            tmp_white_locations[selection] = i
            if i in tmp_black_locations: #piece captured
                black_piece = tmp_black_locations.index(i)
                tmp_black_pieces.pop(black_piece)
                tmp_black_locations.pop(black_piece)
            if incheck(tmp_white_pieces, tmp_black_pieces, tmp_white_locations, tmp_black_locations, 'black'): 
                print("OH NO")
                options_list[selection].remove(i)'''
    else:
        options_list = black_options
        turn = 'white'
    
    valid_options = options_list[selection]
    return valid_options

def draw_valid(moves):
    for i in range(len(moves)):
        if moves[i] in white_locations or moves[i] in black_locations:
            color = 'red'
            pygame.draw.rect(screen, 'red', [moves[i][0] * 600//8 + 1, moves[i][1] * 600//8 + 1, 600//8, 600//8], 5)
        else: 
            if (moves[i][0] + moves[i][1]) % 2 == 0: 
                color = '#d5c09e' #light squares
            else: 
                color = '#a57958' #dark squares
            pygame.draw.circle(screen, color, (moves[i][0] * (600//8) + 40, moves[i][1] * (600//8) + 40),12)
            
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'red', (white_locations[king_index][0] * size + 1,
                                                            white_locations[king_index][1] * size + 1 , 600//8, 600//8), 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * size + 1,
                                                            black_locations[king_index][1] * size + 1 , 600//8, 600//8], 5)

#to show captured pieces on the side
#this is not working pls check the coordination
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (625, 5 + 50 * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (725, 5 + 50 * i))

def draw_game_over():
    pygame.draw.rect(screen, 'brown', [130,250,400,50])
    screen.blit(font.render(f' W {winner} who wins the game!', True, 'orange'), (130,250))
    screen.blit(font.render(f'Press ENTER for a new game', True, 'orange'), (140,280))

#main game loop
black_options = check_options(black_pieces,black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    screen.fill('#b88762') #whatever color you want the screen's background to be and the dark squared
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 1000:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves) #to draw valid moves on the screen for user
    #event handling
    for event in pygame.event.get(): #getting everything that is happening in the computer like click, etc
        if event.type == pygame.QUIT: #the little X in the top of the window
            run = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x_coord = event.pos[0] // (600//8) #event.pos tells the (x, y) coordinates
        y_coord = event.pos[1] // (600//8)
        click_coords = (x_coord, y_coord)
        if turn_step < 2:
            if click_coords == (8, 8) or click_coords == (9,8):
                winner = 'Black'
            if click_coords in white_locations:
                selection = white_locations.index(click_coords)
                if turn_step == 0:
                    turn_step = 1 #We're making turn_step = 1 to make the move
            if click_coords in valid_moves and selection != 1000:
                white_locations[selection] = click_coords


                #move the rook if castled
                castled = False
                if white_pieces[selection] == 'king' and white_moved[selection] == False:
                    if white_locations[4] == (6, 7):
                        castled = True
                        white_locations[7] = (5, 7)
                    elif white_locations[4] == (2, 7):
                        castled = True
                        white_locations[0] = (3, 7)


                white_moved[selection] = True
                turn_step = 2
                if click_coords in black_locations: #piece captured
                    black_piece = black_locations.index(click_coords)
                    captured_pieces_white.append(black_pieces[black_piece])
                    if black_pieces[black_piece] == 'king':
                        winner = 'White'
                    #Now we are removing the piece from the board as well as the list
                    black_pieces.pop(black_piece)
                    black_locations.pop(black_piece)
                    black_moved.pop(black_piece)
                #empty selection to avoid auto select
                selection = 1000
                click_coords = None
                flip_pieces()
                #Now we are going to check for black and white pieces' options for next move
                black_options = check_options(black_pieces,black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                #Now we are going to let black play
                valid_moves = [] #Because now valid moves are going to be different

        if turn_step >= 2:
            if click_coords == (8,8) or click_coords == (9,8):
                winner = 'White'
            if click_coords in black_locations:
                selection = black_locations.index(click_coords)
                if turn_step == 2:
                    turn_step = 3 #We're making turn_step = 1 to make the move
            if click_coords in valid_moves and selection != 1000:
            
                black_locations[selection] = click_coords
                #move the rook if castled
                castled = False
                if black_pieces[selection] == 'king' and black_moved[selection] == False:
                    if black_locations[4] == (5, 7):
                        castled = True
                        black_locations[0] = (4, 7)
                    if black_locations[4] == (1, 7):
                        castled = True
                        black_locations[7] = (2, 7)
                black_moved[selection] = True
                turn_step = 0
                if click_coords in white_locations: #piece captured
                    white_piece = white_locations.index(click_coords)
                    captured_pieces_black.append(white_pieces[white_piece])
                    if white_pieces[white_piece] == 'king':
                        winner = 'Black'
                    #Now we are removing the piece from the board as well as the list
                    white_pieces.pop(white_piece)
                    white_locations.pop(white_piece)
                    white_moved.pop(white_piece)
                #empty selection to avoid autoselect
                selection = 1000
                click_coords = None
                flip_pieces()
                #Now we are going to check for black and white pieces' options for next move
                black_options = check_options(black_pieces,black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')
                #Now we are going to let white play
                valid_moves = [] #Because now valid moves are going to be different
    if event.type == pygame.KEYDOWN and game_over:
        if event.key == pygame.K_RETURN:
            game_over = False
            winner = ''
            white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
            black_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]  # (column, row)
            black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
            white_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                               (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
            white_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
            black_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
            captured_pieces_white = []  # To keep track of what pieces are captured
            captured_pieces_black = []
            turn_step = 0
            selection = 1000
            valid_moves = []
            black_options = check_options(black_pieces, black_locations, 'black')
            white_options = check_options(white_pieces, white_locations, 'white')
    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.flip() #throws everything onto the screen

pygame.quit()
#So until this code we should be able to get the window + background color + ability to quit
