import sys, pygame
import pygame.math
BLACK = (0,0,0)
WHITE = (255,255,255)
MOVESPEED = 4
BALLSPEED = 4
SIZE = WIDTH, HEIGHT = 1000, 800

def main():
    pygame.init()

    paddle1 = pygame.Rect(30, 30, 20, 100)
    paddle2 = pygame.Rect(940, 30, 20, 100)
    
    ball = pygame.Rect(500, 400, 15, 15)
    ballDirection = pygame.Vector2(BALLSPEED)

    screen = pygame.display.set_mode(SIZE)


    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()


        paddle1 = movePaddle(paddle1, pygame.K_w, pygame.K_s)
        paddle2 = movePaddle(paddle2, pygame.K_UP, pygame.K_DOWN)

        ball = ball.move(ballDirection)

        if (ball.top < 0):
            ball.top = 0
            ballDirection[1] = ballDirection[1] * -1
        if (ball.bottom > HEIGHT):
            ball.bottom = HEIGHT
            ballDirection[1] = ballDirection[1] * -1

        if (ball.left < 0):
            ball.left = 0
            ballDirection[0] = ballDirection[0] * -1
        if (ball.right > WIDTH):
            ball.right = WIDTH
            ballDirection[0] = ballDirection[0] * -1

        if (ball.colliderect(paddle1) or ball.colliderect(paddle2)):
            ballDirection[0] = ballDirection[0] * -1

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.rect(screen, WHITE, ball)
        pygame.display.flip()
        pygame.time.delay(10)

def movePaddle(paddle, upkey, downkey):
    keys = pygame.key.get_pressed()
    if (keys[upkey]):
        paddle = paddle.move((0, MOVESPEED * -1))
    if (keys[downkey]):
        paddle = paddle.move((0, MOVESPEED))

    if (paddle.top < 0):
        paddle.top = 0
    if (paddle.bottom > HEIGHT):
        paddle.bottom = HEIGHT

    return paddle

if (__name__ == "__main__"):
    main()
