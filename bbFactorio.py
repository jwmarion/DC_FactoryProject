import pygame

class Board(object):
    def __init__(self):
        self.color = (0,0,0)
        self.x = 800
        self.y = 600

    def DrawBoard(self,screen):
        pygame.draw.rect(screen, self.color, ((0,0),(798,598)), 4)
        pygame.draw.line(screen, self.color, (600,0), (600,600), 2)
        pygame.draw.line(screen, self.color, (600,100),(800, 100), 2)
        pygame.draw.line(screen, self.color, (600,200),(800, 200), 2)
        pygame.draw.line(screen, self.color, (600,300),(800, 300), 2)
        pygame.draw.line(screen, self.color, (600,400),(800, 400), 2)
        pygame.draw.line(screen, self.color, (600,500),(800, 500), 2)

        #play/pause/ff
        pygame.draw.line(screen, self.color, (666,500),(666, 600), 2)
        pygame.draw.line(screen, self.color, (732,500),(732, 600), 2)


class gamePiece(object):
    def __init__(self):
        self.type = "blank"
        self.x = 0
        self.y = 0

    def render():
        screen.blit(self.img, (self.x, self.y))

class Machine(gamePiece):
    def __init__(self):
        self.type = "blank"
        self.x = 0
        self.y = 0


class Mover(gamePiece):
    def __init__(self, x, y):
        self.type = "blank"
        self.x = x
        self.y = y

class Belt(gamePiece):
    def __init__(self):
        self.type = "blank"
        self.x = 0
        self.y = 0

class Source(gamePiece):
    def __init__(self):
        self.type = "blank"
        self.x = 0
        self.y = 0

class OutPut(gamePiece):
    def __init__(self):
        self.type = "blank"
        self.x = 0
        self.y = 0

class Button(object):
    def __init__(self):
        self.x = 0
        self.y = 0

def roundClick(self, x, y):
    if x % 30 != 0:
         x = x - (x%20)
    if y % 30 != 0:
         y = y - (y%20)
    item = [x,y]
    return item

def checkClick(self, x, y):
        item = grid[x][y]
        if (x <= 800 and x >= 600 and y <=200 and y >= 100):  #machine button
            placeMachine = True
        if (x <= 800 and x >= 600 and y <=300 and y >= 201):  #mover button
            placeMover = True

        if placeMover == True or placeMachine == True:
            if placeMover == True:
                item = roundClick(x,y)
                x = item[0]
                y = item[1]
                if checkEmpty('mover',x,y) == True:
                    objectList.append(Mover(x,y))
                else:
                    pass
                #mover.placeMover
            else:
                #placeMachine
                item = roundClick(x,y)
                x = item[0]
                y = item[1]
                if checkEmpty('machine',x,y) == True:
                    objectList.append(Machine(x,y))
                else:
                    pass



        else:
            if (item != None):
                # if item == 1:   #button
                #     if button.type == 'machine':
                #     if button.type == 'mover':
                # if item == 2:   #machine
                # if item == 3:   #mover
                # if item == 4:   #belt
                # if item == 5:   #source
                # if item == 6:   #output
                # if item == 7:   #play
                # if item == 8:   #ff
                pass


def checkEmpty(self,type,x,y):
    if type == 'mover': #check 1x2
        if grid[x][y] == None and grid[x][y+1] == None:
            return True
    if type == 'machine' or type == 'source' or type == 'output': #check 2x2
            if grid[x][y] == None and grid[x + 1][y] == None and grid[x][y+1] == None and grid[x + 1][y+1] == None:
                return True



def main():
    #
    width = 800
    height = 600
    white_color = (255, 255, 255)
    black_color = (0,0,0)
    #setup
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    board = Board()
    grid = [[None] * 20] * 20

    #text setup
    font = pygame.font.Font(None, 25)
    playText = font.render("PLAY", True, (0,0,0))
    pauseText = font.render("Pause", True, (0,0,0))
    ffText = font.render("FF", True, (0,0,0))
    titleText = font.render("PyFactory", True, (0,0,0))
    machineBtext = font.render("Machine", True, (0,0,0))
    moverBtext = font.render("Movers", True, (0,0,0))

    objectList =[]




    # Game initialization


    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                checkClick(x,y)


            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background

        screen.fill(white_color)
        board.DrawBoard(screen)
        screen.blit(pauseText, (607,550 ))
        screen.blit(playText, (680,550 ))
        screen.blit(ffText, (750,550 ))
        screen.blit(titleText, (607,10))
        screen.blit(machineBtext,(605,105))
        screen.blit(moverBtext,(605,205))
        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
