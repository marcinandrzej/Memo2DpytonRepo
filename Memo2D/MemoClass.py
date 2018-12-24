import pygame
import random

COLORS = ((255,0,0),(0,255,0),(0,0,255),(255,0,255),(0,255,255),(255,255,0),(128,64,32),(64,32,128),(255,255,255))
BLACK = (0,0,0)


class MemoClass:

    def __init__(self, window_w=500, window_h=500):

        self.grid = []
        for row in range(4):
            self.grid.append([])
            for column in range(4):
                self.grid[row].append(2*row + column//2)

        self.activeGrid = []
        for row in range(4):
            self.activeGrid.append([])
            for column in range(4):
                self.activeGrid[row].append(0)

        self.firstClick = True
        self.hit = False
        self.firstLocation = [0,0]
        self.secondLocation = [0,0]

        self.width = window_w // 4
        self.height = window_h // 4
        self.window_w = window_w
        self.window_h = window_h

        self.width_w = min((self.window_w // 100),5)
        self.width_h = min((self.window_h // 100),5)

        self.font = pygame.font.SysFont('Arial', 30, True, False)

        self.setGame()

    def drawScene(self, screen, win):

        screen.fill(BLACK)

        if not win:
            for row in range(4):
                for col in range(4):
                    if self.activeGrid[row][col] == 1:
                        color = COLORS[self.grid[row][col]]
                    else:
                        color = COLORS[8]
                    pygame.draw.rect(screen, color, [col * self.width, row * self.height, self.width, self.height])

            pygame.draw.line(screen, BLACK, [self.width, 0], [self.width, self.window_h], self.width_w)
            pygame.draw.line(screen, BLACK, [2 * self.width, 0], [2 * self.width, self.window_h], self.width_w)
            pygame.draw.line(screen, BLACK, [3 * self.width, 0], [3 * self.width, self.window_h], self.width_w)
            pygame.draw.line(screen, BLACK, [0, self.height], [self.window_w, self.height], self.width_h)
            pygame.draw.line(screen, BLACK, [0, 2 * self.height], [self.window_w, 2 * self.height], self.width_h)
            pygame.draw.line(screen, BLACK, [0, 3 * self.height], [self.window_w, 3 * self.height], self.width_h)
        else:
            text = self.font.render("CONGRATULATIONS", True, COLORS[5])
            screen.blit(text, [self.window_w // 3, self.window_h // 3])
            text = self.font.render("Press R to Restart", True, COLORS[5])
            screen.blit(text, [self.window_w // 3, self.window_h // 2])

        pygame.display.flip()

    def update(self, player_position):

        if player_position[0] > 0 and player_position[0] < (4 * self.width) and \
            player_position[1] > 0 and player_position[1] < (4 * self.height):
            row = min((player_position[1]) // self.height, 3)
            col = min((player_position[0]) // self.width, 3)
            if self.firstClick:
                if self.activeGrid[row][col] == 0:
                    if not self.hit:
                        self.activeGrid[self.firstLocation[0]][self.firstLocation[1]] = 0
                        self.activeGrid[self.secondLocation[0]][self.secondLocation[1]] = 0
                    self.hit = False
                    self.firstLocation = [row, col]
                    self.activeGrid[row][col] = 1
                    self.firstClick = False
            else:
                if self.activeGrid[row][col] == 0:
                    self.secondLocation = [row, col]
                    self.activeGrid[row][col] = 1
                    if (self.grid[self.firstLocation[0]][self.firstLocation[1]]
                            == self.grid[self.secondLocation[0]][self.secondLocation[1]]):
                        self.hit = True
                    self.firstClick = True

    def checkWin(self):
        if (self.activeGrid[0][0] == self.activeGrid[0][1] == self.activeGrid[0][2] == self.activeGrid[0][3] ==
                self.activeGrid[1][0] == self.activeGrid[1][1] == self.activeGrid[1][2] == self.activeGrid[1][3] ==
                self.activeGrid[2][0] == self.activeGrid[2][1] == self.activeGrid[2][2] == self.activeGrid[2][3] ==
                self.activeGrid[3][0] == self.activeGrid[3][1] == self.activeGrid[3][2] == self.activeGrid[3][3] == 1):
            return True
        else:
            return False

    def setGame(self):
        randi = random.randrange(30,40)
        for i in range(randi):
            randx1 = random.randrange(4)
            randy1 = random.randrange(4)
            randx2 = random.randrange(4)
            randy2 = random.randrange(4)
            temp = self.grid[randx1][randy1]
            self.grid[randx1][randy1] = self.grid[randx2][randy2]
            self.grid[randx2][randy2] = temp