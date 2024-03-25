import pygame as pg
import pyautogui as pag
pg.init()
pg.display.set_caption("Tic Tac Toe by Logan Slowik")
pag.alert("Use the numpad to play.\nGrid mimics the numpad shape\nTop left square = Numpad 7, etc.")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = SCREEN_WIDTH
CELL_PADDING = 50
PIECE_SIZE = (SCREEN_WIDTH/3-2*CELL_PADDING,SCREEN_HEIGHT/3-2*CELL_PADDING)
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#load sprites
xSprite = pg.image.load('ttt_x.png')
xSprite = pg.transform.scale(xSprite,PIECE_SIZE)
xRect = xSprite.get_rect()
oSprite = pg.image.load('ttt_o.png')
oSprite = pg.transform.scale(oSprite,PIECE_SIZE)
oRect = oSprite.get_rect()

pieceList = []
currentPlayer = 2 # 1 = o and 2 = x
matR, matC = (3,3)
matrix = [[0 for i in range(matC)] for j in range(matR)] #matrix storing the contents of the board in the order 7 8 9 4 5 6 1 2 3

moveCount = 0
gameOver = False
conclusion = ""
positions = {
    1 : (CELL_PADDING, 2*SCREEN_HEIGHT/3+CELL_PADDING),
    2 : (SCREEN_WIDTH/3+CELL_PADDING, 2*SCREEN_HEIGHT/3+CELL_PADDING),
    3 : (2*SCREEN_WIDTH/3+CELL_PADDING, 2*SCREEN_HEIGHT/3+CELL_PADDING),
    4 : (CELL_PADDING, SCREEN_HEIGHT/3+CELL_PADDING),
    5 : (SCREEN_WIDTH/3+CELL_PADDING, SCREEN_HEIGHT/3+CELL_PADDING),
    6 : (2*SCREEN_WIDTH/3+CELL_PADDING, SCREEN_HEIGHT/3+CELL_PADDING),
    7 : (CELL_PADDING, CELL_PADDING),
    8 : (SCREEN_WIDTH/3+CELL_PADDING, CELL_PADDING),
    9 : (2*SCREEN_WIDTH/3+CELL_PADDING, CELL_PADDING)
    }

def ToggleTurn():
    global currentPlayer
    if currentPlayer == 1:
        currentPlayer = 2
    elif currentPlayer == 2:
        currentPlayer = 1

def DrawBoard(sw,sh):
    lineThickness = 10
    borderThickness = 25
    lineL = pg.Rect((sw/3-lineThickness/2,borderThickness,lineThickness,sh-2*borderThickness))
    lineR = pg.Rect((2*sw/3-lineThickness/2,borderThickness,lineThickness,sh-2*borderThickness))
    lineU = pg.Rect((borderThickness,sh/3-lineThickness/2,sw-2*borderThickness,lineThickness))
    lineD = pg.Rect((borderThickness,2*sh/3-lineThickness/2,sw-2*borderThickness,lineThickness))
    pg.draw.rect(screen, (255,255,255), lineL)
    pg.draw.rect(screen, (255,255,255), lineR)
    pg.draw.rect(screen, (255,255,255), lineU)
    pg.draw.rect(screen, (255,255,255), lineD)
def PlacePiece(piece,slot, matX, matY):
    if not (1,slot) in pieceList and not (2,slot) in pieceList:
        global moveCount
        global matrix
        matrix[matX][matY] = piece
        pieceList.append((piece,slot))
        moveCount=moveCount+1
        ToggleTurn()
        CheckForEndGame()
    else:
        print("GAME NOTE: A piece has already been placed there!")
def CheckForEndGame():
    '''
    Uses the set() function to verify there are not several different pieces in a valid winning position. Further verifies that
    the positions are not all 0s.  This line could be removed if the board was initialized to something like
    [(4 5 6), (5 6 4), (6 4 5)] because then the win condition would never all be the same number.  However, initializing the board to all
    0s is more intuitive and easier to follow
    '''
    global gameOver
    global conclusion
    if gameOver:
        return
    if moveCount == 9:
        gameOver=True
        conclusion = "Draw.  No players win."
    if len(set((matrix[0][0],matrix[0][1],matrix[0][2]))) == 1:
        if matrix[0][0] > 0:
            gameOver = True
            if matrix[0][0] == 1:
                conclusion = "O wins!"
            elif matrix[0][0] == 2:
                conclusion = "X wins!"
    if len(set((matrix[1][0],matrix[1][1],matrix[1][2]))) == 1:
        if matrix[1][0] > 0:
            gameOver = True
            if matrix[1][0] == 1:
                conclusion = "O wins!"
            elif matrix[1][0] == 2:
                conclusion = "X wins!"
    if len(set((matrix[2][0],matrix[2][1],matrix[2][2]))) == 1:
        if matrix[2][0] > 0:
            gameOver = True
            if matrix[2][0] == 1:
                conclusion = "O wins!"
            elif matrix[2][0] == 2:
                conclusion = "X wins!"
    if len(set((matrix[0][0],matrix[1][0],matrix[2][0]))) == 1:
        if matrix[0][0] > 0:
            gameOver = True
            if matrix[0][0] == 1:
                conclusion = "O wins!"
            elif matrix[0][0] == 2:
                conclusion = "X wins!"
    if len(set((matrix[0][1],matrix[1][1],matrix[2][1]))) == 1:
        if matrix[0][1] > 0:
            gameOver = True
            if matrix[0][1] == 1:
                conclusion = "O wins!"
            elif matrix[0][1] == 2:
                conclusion = "X wins!"
    if len(set((matrix[0][2],matrix[1][2],matrix[2][2]))) == 1:
        if matrix[0][2] > 0:
            gameOver = True
            if matrix[0][2] == 1:
                conclusion = "O wins!"
            elif matrix[0][2] == 2:
                conclusion = "X wins!"
    if len(set((matrix[0][0],matrix[1][1],matrix[2][2]))) == 1:
        if matrix[0][0] > 0:
            gameOver = True
            if matrix[0][0] == 1:
                conclusion = "O wins!"
            elif matrix[0][0] == 2:
                conclusion = "X wins!"
    if len(set((matrix[0][2],matrix[1][1],matrix[2][0]))) == 1:
        if matrix[0][2] > 0:
            gameOver = True
            if matrix[0][2] == 1:
                conclusion = "O wins!"
            elif matrix[0][2] == 2:
                conclusion = "X wins!"
    if not conclusion == "":
        UpdateBoard()
        print(conclusion)
        pag.alert(conclusion)


def PrintMatrix():
    #used for debugging purposes
    global matrix, matC, matR
    for i in range(matC):
        print(str(matrix[i][0]) + " " + str(matrix[i][1]) + " " + str(matrix[i][2]))
    print("\n")
def UpdateBoard():
    screen.fill((0,0,0))
    DrawBoard(SCREEN_WIDTH, SCREEN_HEIGHT)
    for piece in pieceList:
        if (piece[0] == 2):
            screen.blit(xSprite,positions[piece[1]])
        elif (piece[0] == 1):
            screen.blit(oSprite,positions[piece[1]])
RUN = True
while RUN:
    UpdateBoard()
    #event handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                RUN = False
            elif event.key == pg.K_KP1:
                PlacePiece(currentPlayer,1,2,0)
            elif event.key == pg.K_KP2:
                PlacePiece(currentPlayer,2,2,1)
            elif event.key == pg.K_KP3:
                PlacePiece(currentPlayer,3,2,2)
            elif event.key == pg.K_KP4:
                PlacePiece(currentPlayer,4,1,0)
            elif event.key == pg.K_KP5:
                PlacePiece(currentPlayer,5,1,1)
            elif event.key == pg.K_KP6:
                PlacePiece(currentPlayer,6,1,2)
            elif event.key == pg.K_KP7:
                PlacePiece(currentPlayer,7,0,0)
            elif event.key == pg.K_KP8:
                PlacePiece(currentPlayer,8,0,1)
            elif event.key == pg.K_KP9:
                PlacePiece(currentPlayer,9,0,2)
            elif event.key == pg.K_p:
                PrintMatrix()
    pg.display.update()
