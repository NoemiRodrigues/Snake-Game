import pygame
import time
import random

#iniciando jogo
pygame.init()

#personalizando o quadrinho em que iremos jogar
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Definindo cores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

#Definindo um relógio para o jogo
relogio = pygame.time.Clock()

#Definindo velocidade e tamanho da cobrinha
block_size = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Função para termos a pontuação e ela aparecer na tela
def our_score(score):
    value = score_font.render("Sua pontuação: " + str(score), True, black)
    screen.blit(value, [0, 0])

#Função de desenho da cobrinha
def our_snake(block_size, snake_List):
    for x in snake_List:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

#Função para mostrar mensagem no jogo, aqui estamos definindo como irá aparecer
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [1, height / 3])

#Loop do jogo
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #Usando valores aleatórios para plotar a comida da cobrinha no jogo
    foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message (" Você perdeu! Pressione Q- Para sair ou C-Para jogar novamente", red)
            our_score(Length_of_snake - 1)
            pygame.display.update()

            #Lidar com eventos dentro do jogo, está definido como Q e C e não em português devido a própria biblioteca pygame
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)
        our_score(Length_of_snake - 1)

        pygame.display.update()

        #Condição para caso a cobrinha coma a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            Length_of_snake += 1
            #toda vez que ela comer, ela irá ganhar tamanho

        relogio.tick(snake_speed)

    pygame.quit()
    quit()

#Loop de jogo
gameLoop()
