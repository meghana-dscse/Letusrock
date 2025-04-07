import pygame
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((600,300))
pygame.display.set_caption('Piano Vaayinchu MAMA')
sounds={
    pygame.K_a : pygame.mixer.Sound("piano-mp3_C4.wav"),
    pygame.K_s : pygame.mixer.Sound("piano-mp3_D4.wav"),
    pygame.K_d  : pygame.mixer.Sound("piano-mp3_E4.wav"),
    pygame.K_f  : pygame.mixer.Sound("piano-mp3_F4.wav"),
    pygame.K_g : pygame.mixer.Sound("piano-mp3_G4.wav"),
    pygame.K_h: pygame.mixer.Sound("piano-mp3_A4.wav"),
    pygame.K_j  : pygame.mixer.Sound("piano-mp3_B4.wav"),
    pygame.K_k : pygame.mixer.Sound("piano-mp3_C5.wav")
}
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Arial", 60, bold=True)
title_text = font.render("Piano Master", True, WHITE)

run=True
while run:
    screen.fill(BLACK)
    screen.blit(title_text,(150, 120) )

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key in sounds:
                sounds[event.key].play()

pygame.quit()