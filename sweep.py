import random
import pygame

class Board:
    def __init__(self, size):
        self.size=size
        self.gameplay = self.setup(self.size)
        self.conquered = {}
    
    """
    Place the bombs randomly on the board
    Assign the numbers according to the bomb placements
    """
    def setup(self,size): # board setup working as intended
        board = [[0 for i in range(size)] for i in range(size)] # set up board with all 0s in each square
        bombs = size**2 // 5 # the number of bombs is 1/5 of the total number of squares
        bomb_list = []
        for m in range(bombs):
            tmp = random.randint(0,size**2-1)
            while tmp in bomb_list: # continuously generate a new number if the location already has a bomb
                tmp = random.randint(0,size**2-1)
            bomb_list.append(tmp) # add bombs to all locations

        for bomb in bomb_list:
            r = bomb//size
            c = bomb%size
            board[r][c] = '*'
            for wide in range(-1,2):
                for high in range(-1,2):
                    try:
                        if board[r+high][c+wide] != '*':
                            board[r+high][c+wide] += 1
                    
                    except IndexError:
                        continue
        return board


    """
    We want to reveal the square that was dug
    Assign a number to each square which says the number of nearby bombs
    keep digging if that number is 0 (recursive)
    """
    def dig(self,row,col):
        print("manually dug at", row, ',', col)
        self.conquered[(row,col)] = self.gameplay[row][col]
        if (self.gameplay[row][col] == '*'):
            self.lose()
        elif (self.gameplay[row][col] == 0):
            self.recurse(row,col)
        return

    def recurse(self,row,col):
        print("called for", row, ',', col)
        for ud in range(-1,2):
            for lr in range (-1,2):
                try:
                    if (row+ud,col+lr) not in self.conquered:
                        self.dig(row+ud,col+lr)
                except IndexError:
                    continue    
        return

        

    def lose(self):
        print("lost!")

WIDTH, HEIGHT = 720,720
def main():
    game = Board(10)
    for i in range(game.size):
        for j in range(game.size):
            print(str(game.gameplay[i][j]), end= ' ')
        print('\n')
    RWIDTH, RHEIGHT = WIDTH//2, HEIGHT//2
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    """
    Use modulus from the coordinates in order to match the position in the 2-D array
    - there is a five unit gap between each box
    - 10x10 grid
    """
    while running:
        board = pygame.Rect(WIDTH/4,HEIGHT/4,RWIDTH,RHEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if board.collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        x_pos,y_pos = pygame.mouse.get_pos()
                        row = (x_pos - (WIDTH//4)) // (RWIDTH//10)
                        col = ((y_pos - (HEIGHT//4)) // (RHEIGHT//10)) % 10
                        game.dig(row,col)
        screen.fill("purple")

        pygame.draw.rect(screen, (0,0,0), board)
        for x in range(0,RWIDTH,RWIDTH//10): # coordinates
            for y in range(0,RHEIGHT,RHEIGHT//10):
                box = pygame.Rect(WIDTH/4 + x + 5, HEIGHT/4 + y + 5, RWIDTH/10 - 5, RHEIGHT/10 - 5)
                if (x*10//RWIDTH,y*10//RHEIGHT) in game.conquered:
                    signal = (0,0,0)
                    if game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 1:
                        signal = (194,233,238)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 0:
                        signal = (239,187,187)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 2:
                        signal = (162,228,164)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 3:
                        signal = (220,70,70)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 4:
                        signal = (120,120,240)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 5:
                        signal = (208,240,120)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 6:
                        signal = (246,188,144)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 7:
                        signal = (255,0,255)
                    elif game.conquered[(x*10//RWIDTH,y*10//RHEIGHT)] == 8:
                        signal = (153,0,51)
                    
                else:
                    signal = (255,255,255)
                if box.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen,(222,176,252), box)
                else:
                    pygame.draw.rect(screen, signal, box)



        """
        put the appropriate numbers onto the display based on the set of cleared squares in the board object
        """

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()