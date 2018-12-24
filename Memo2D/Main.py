import pygame

from MemoClass import MemoClass

WINDOW_H = 600
WINDOW_W = 800


def main():

    done = False
    win = False

    pygame.init()

    size = [WINDOW_W, WINDOW_H]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("MEMO2D")

    clock = pygame.time.Clock()

    game = MemoClass(WINDOW_W, WINDOW_H)

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_r:
                    game = MemoClass(WINDOW_W, WINDOW_H)
            elif event.type == pygame.MOUSEBUTTONDOWN and not win:
                button = pygame.mouse.get_pressed()
                if(button[0]):
                    player_position = pygame.mouse.get_pos()
                    game.update(player_position)

        win = game.checkWin()

        game.drawScene(screen, win)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()