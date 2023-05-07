import pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 50)
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Scout Run')
bg_image = pygame.image.load('dbcr.png')
bg_image = pygame.transform.scale(bg_image,(800,600))
bg_x = 0
dino_img = pygame.image.load('run11.png').convert_alpha()
dino_img = pygame.transform.scale(dino_img, (200, 200))
cactus_img = pygame.image.load('spy1.png').convert_alpha()
cactus_img = pygame.transform.scale(cactus_img, (150, 150))
pygame.mixer.init()
pygame.mixer.music.load('valve.mp3')
pygame.mixer.music.play()
clock = pygame.time.Clock()
dino_x = 50
dino_y = 380
dino_y_change = 0
cactus_x = 800
cactus_y = 450
cactus_speed = 5
score = 0
score_needed_to_win = 5
def show_game_won():
    font = pygame.font.SysFont('Arial', 50)
    text = font.render('You win!', True, (0, 255, 0))
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(text, text_rect)
def show_game_over():
    font = pygame.font.SysFont('Arial', 50)
    text = font.render('You lose!', True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(text, text_rect)
font = pygame.font.SysFont('Arial', 36)
score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
run = True
finish = False
while run:
    bg_x -= 5
    if bg_x < -bg_image.get_width():
        bg_x = 0
    screen.blit(bg_image, (bg_x, 0))
    screen.blit(bg_image, (bg_x + bg_image.get_width(), 0))
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))
    screen.blit(score_text, (10, 10))
    if finish != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino_y_change = -30
        dino_y += dino_y_change
        if dino_y < 250:
            dino_y = 250
        if dino_y > 400:
            dino_y = 400
        dino_y_change += 1
        cactus_x -= cactus_speed
        if cactus_x < -100:
            cactus_x = 800
            score += 1
            score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
        if cactus_x <= dino_x + 50 <= cactus_x + 100 and cactus_y <= dino_y + 100 <= cactus_y + 50:
            finish = True
            show_game_over()
            run = False
            pygame.time.delay(3000)
        if score >= score_needed_to_win:
            finish = True
            show_game_won()
            run = False
            pygame.time.delay(3000)
        pygame.display.update()
    clock.tick(60)