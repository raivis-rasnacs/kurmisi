import pygame
import random

pygame.init()

pygame.display.set_caption("Kurmīši")
icon = pygame.image.load('assets/mole-icon.png')

screen = pygame.display.set_mode((600, 600))
pygame.display.set_icon(icon)

# **EVENTS***
MOLE_APPEARS = pygame.USEREVENT + 1
MOLE_DISAPPEARS = pygame.USEREVENT + 2
pygame.time.set_timer(MOLE_APPEARS, 3000)
pygame.time.set_timer(MOLE_DISAPPEARS, 6000)


pygame.mouse.set_cursor((8, 8),
                        (0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0))

gameOver = False

caves = [
    (50, 30),
    (230, 30),
    (410, 30),
    (50, 210),
    (230, 210),
    (410, 210),
    (50, 390),
    (230, 390),
    (410, 390)]

moles = []

newCave = pygame.image.load('assets/ala.png')
newMole = pygame.image.load('assets/kurmis.png')
hammerImg = pygame.image.load('assets/amurs-augsa.png')


def hit(x, y):
    for mole in moles:
        if mole[0] <= x <= mole[0] + 150 and mole[1] <= y <= mole[1] + 150:
            return mole
    else:
        return 0


while gameOver is False:
    screen.fill((20, 163, 24))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
            pygame.QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hammerImg = pygame.image.load('assets/amurs-leja.png')
            response = hit(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            if isinstance(response, tuple):
                idx = moles.index(response)
                caves.append(moles[idx])
                moles.pop(idx)
        elif event.type == pygame.MOUSEBUTTONUP:
            hammerImg = pygame.image.load('assets/amurs-augsa.png')
        elif event.type == MOLE_APPEARS:
            idx = random.randrange(0, len(caves))
            moles.append(caves[idx])
            caves.pop(idx)
        elif event.type == MOLE_DISAPPEARS:
            if len(moles) >= 1:
                idx = random.randrange(0, len(moles))
                caves.append(moles[idx])
                moles.pop(idx)

    for i in range(len(caves)):
        screen.blit(newCave, (caves[i][0], caves[i][1]))

    if len(moles) >= 1:
        for i in range(len(moles)):
            screen.blit(newMole, (moles[i][0], moles[i][1]))

    screen.blit(hammerImg, (
                pygame.mouse.get_pos()[0],
                pygame.mouse.get_pos()[1] - 100))

    pygame.display.update()
