import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("крута гра")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
HOVER_COLOR = (150, 150, 150)
TEXT_COLOR = (255, 100, 0)  


font = pygame.font.SysFont(None, 48)
scroll_font = pygame.font.SysFont(None, 36)


image = pygame.image.load("krutoi svin.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))


music_started = False


scroll_text = "Якщо вам сподабався мій проект, то дайте мені 8 тисяч, я куплю сухарікі"
scroll_surface = scroll_font.render(scroll_text, True, TEXT_COLOR)
scroll_x = WIDTH  


scroll_speed = 2  


def draw_button(text, x, y, w, h, mouse_pos):
    rect = pygame.Rect(x, y, w, h)
    if rect.collidepoint(mouse_pos):
        color = HOVER_COLOR
    else:
        color = GRAY
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, WHITE, rect, 2)

    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect


in_menu = True
running = True
clock = pygame.time.Clock()

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and in_menu:
            if play_button.collidepoint(event.pos):
                in_menu = False
                pygame.mixer.music.load("mysika.mp3")
                pygame.mixer.music.play(-1)
                music_started = True
            elif quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    if in_menu:
        screen.fill(BLACK)
        play_button = draw_button("Играть", 220, 150, 200, 60, mouse_pos)
        quit_button = draw_button("Выйти", 220, 250, 200, 60, mouse_pos)
    else:
        screen.blit(image, (0, 0))

       
        screen.blit(scroll_surface, (scroll_x, HEIGHT - 50))
        scroll_x -= scroll_speed
        if scroll_x < -scroll_surface.get_width():
            scroll_x = WIDTH  

    pygame.display.flip()
    clock.tick(60)  