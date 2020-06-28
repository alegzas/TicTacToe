import pygame

pygame.init()

grid = [[0,0,0], [0,0,0], [0,0,0]]


width = 600
heigth = 600

gameDisplay = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('Tic-Tac-Toe')
clock = pygame.time.Clock()
gameDisplay.fill([220,220,220])
pygame.display.update()


crashed = False

currentPlayer = 1;

while not crashed:
#loop


    mouseX, mouseY = pygame.mouse.get_pos()


    for event in pygame.event.get():
    #loop
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                gameDisplay.fill([220,220,220])
                grid = [[0,0,0], [0,0,0], [0,0,0]]
                currentPlayer = 1
        if event.type == pygame.MOUSEBUTTONUP:
            if grid[0][0] == 0 and mouseX > 0 and mouseX < width/3  and mouseY > 0 and mouseY < heigth/3:
                grid[0][0] = currentPlayer
                currentPlayer *= -1
            elif grid[0][1] == 0 and mouseX > width/3 and mouseX < width/1.5 and mouseY > 0 and mouseY < heigth/3:
                grid[0][1] = currentPlayer
                currentPlayer *= -1
            elif grid[0][2] == 0 and mouseX > width/1.5 and mouseX < width and mouseY > 0 and mouseY < heigth/3:
                grid[0][2] = currentPlayer
                currentPlayer *= -1
            elif grid[1][0] == 0 and mouseX > 0 and mouseX < width/3 and mouseY > heigth/3 and mouseY < heigth/1.5:
                grid[1][0] = currentPlayer
                currentPlayer *= -1
            elif grid[1][1] == 0 and mouseX > width/3 and mouseX < width/1.5 and mouseY > heigth/3 and mouseY < heigth/1.5:
                grid[1][1] = currentPlayer
                currentPlayer *= -1
            elif grid[1][2] == 0 and mouseX > width/1.5 and mouseX < width and mouseY > heigth/3 and mouseY < heigth/1.5:
                grid[1][2] = currentPlayer
                currentPlayer *= -1
            elif grid[2][0] == 0 and mouseX > 0 and mouseX < width/3 and mouseY > heigth/1.5 and mouseY < heigth:
                grid[2][0] = currentPlayer
                currentPlayer *= -1
            elif grid[2][1] == 0 and mouseX > width/3 and mouseX < width/1.5 and mouseY > heigth/1.5 and mouseY < heigth:
                grid[2][1] = currentPlayer
                currentPlayer *= -1
            elif grid [2][2] == 0 and mouseX > width/1.5 and mouseX < width and mouseY > heigth/1.5 and mouseY < heigth:
                grid[2][2] = currentPlayer
                currentPlayer *= -1
        #print(event)
    #endloop
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == -1:
                pygame.draw.circle(gameDisplay, (255, 0, 0), (100 + (200*j) , 100 + (200 * i)), 80, 10)
            elif grid[i][j] == 1:
                pygame.draw.line(gameDisplay, (0, 0, 255), (200*j, 200*i), (200*(j+1), 200*(i+1)), 10)
                pygame.draw.line(gameDisplay, (0, 0, 255), (200*(j+1), 200*i), (200*j, 200*(i+1)), 10)

    pygame.draw.line(gameDisplay, (0, 0, 0), (width/3, 0), (width/3, heigth), 10)
    pygame.draw.line(gameDisplay, (0, 0, 0), (width/1.5, 0), (width/1.5, heigth), 10)
    pygame.draw.line(gameDisplay, (0, 0, 0), (0, heigth/3), (width, heigth/3), 10)
    pygame.draw.line(gameDisplay, (0, 0, 0), (0, heigth/1.5), (width, heigth/1.5), 10)
    pygame.display.update()
    clock.tick(60)
#endloop


#pygame.draw.circle(gameDisplay, (0, 0, 0), (100, 100), 80, 5)
