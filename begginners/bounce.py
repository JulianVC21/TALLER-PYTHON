import sys, pygame

pygame.init()

size = width, height = 640, 480
dx = 0.5
dy = 0.5
x= 163
y = 120
black = (0,0,0)
white = (255,255,255)
ball_size = 8
MAX_BALL_SIZE = 120
MIN_BALL_SIZE = 8
isOnIncrement = True

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx
        #check max/min ball size
        if ball_size >= MAX_BALL_SIZE:
            isOnIncrement = False
        elif ball_size <= MIN_BALL_SIZE:
            isOnIncrement = True
        #check increment
        if isOnIncrement:
            ball_size += 1
        else:
            ball_size -= 1

    if y < 0 or y > height:
        dy = -dy
        #check max/min ball size
        if ball_size >= MAX_BALL_SIZE:
            isOnIncrement = False
        elif ball_size <= MIN_BALL_SIZE:
            isOnIncrement = True
        #check increment
        if isOnIncrement:
            ball_size += 1
        else:
            ball_size -= 1

    screen.fill(black)

    pygame.draw.circle(screen, white, (x,y), ball_size)

    pygame.display.flip()