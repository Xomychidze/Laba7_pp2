import pygame

pygame.init()
pygame.mixer.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
direction = (0, 0)
last_direction = (0, 0)
playlist = ["Music/922639359.mp3", "Music/2.mp3", "Music/3.mp3", "Music/4.mp3", "Music/5.mp3"]
current_track = 0
pygame.mixer.music.load(playlist[0])
pygame.mixer.music.play(-1)

image = pygame.image.load("Music/download.jpg")
image_rect = image.get_rect(center=(600, 400))

paused = False
running = True
SPEED = 5

class Button:
    def __init__(self, x, y, width, height, color, text, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def resolve_collision(button1, button2):
    if button1.rect.colliderect(button2.rect):
        if direction[0] > 0:  
            button1.rect.right = button2.rect.left
        elif direction[0] < 0:  
            button1.rect.left = button2.rect.right
        if direction[1] > 0: 
            button1.rect.bottom = button2.rect.top
        elif direction[1] < 0:  
            button1.rect.top = button2.rect.bottom

def wrap_around(button):
    """Перемещает кнопку на противоположный край, если она вышла за экран"""
    if button.rect.x > screen.get_width():
        button.rect.x = -button.rect.width
    elif button.rect.x + button.rect.width < 0:
        button.rect.x = screen.get_width()

    if button.rect.y > screen.get_height():
        button.rect.y = -button.rect.height
    elif button.rect.y + button.rect.height < 0:
        button.rect.y = screen.get_height()

button = Button(600, 300, 150, 60, (255, 0, 0), "Pause", (255, 255, 255))
next_button = Button(700, 400, 150, 60, (255, 0, 0), "Next", (255, 255, 255))
prev_button = Button(500, 400, 150, 60, (255, 0, 0), "Prev", (255, 255, 255))

def play_track(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_track(current_track)

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_track(current_track)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if paused:
                    pygame.mixer.music.unpause()
                    button.text = "Pause"
                    direction = last_direction
                else:
                    pygame.mixer.music.pause()
                    button.text = "Play"
                    last_direction = direction
                    direction = (0, 0)
                paused = not paused

            if event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()

            if event.key == pygame.K_w:
                direction = (0, -1)
            elif event.key == pygame.K_s:
                direction = (0, 1)
            elif event.key == pygame.K_a:
                direction = (-1, 0)
            elif event.key == pygame.K_d:
                direction = (1, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                if paused:
                    pygame.mixer.music.unpause()
                    button.text = "Pause"
                else:
                    pygame.mixer.music.pause()
                    button.text = "Play"
                paused = not paused

            if next_button.is_clicked(event.pos):
                next_track()

            if prev_button.is_clicked(event.pos):
                prev_track()
                
                
    image_rect.x += direction[0] * SPEED 
    image_rect.y += direction[1] * SPEED 
    
    if image_rect.x > screen.get_width():
        image_rect.x = -image_rect.width     
    elif image_rect.x + image_rect.width < 0:
        image_rect.x = screen.get_width()

    if image_rect.y > screen.get_height():
        image_rect.y = -image_rect.height
    elif image_rect.y + image_rect.height < 0:
        image_rect.y = screen.get_height()
    
    for btn in [button, next_button, prev_button]:
        btn.rect.x += direction[0] * SPEED
        btn.rect.y += direction[1] * SPEED
        wrap_around(btn)

    resolve_collision(button, next_button)
    resolve_collision(button, prev_button)
    resolve_collision(next_button, prev_button)

    
    screen.fill((0, 200, 0))
    screen.blit(image, image_rect)
    button.draw(screen)
    prev_button.draw(screen)
    next_button.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
