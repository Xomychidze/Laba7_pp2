import pygame

pygame.init()

FPS = 60
SPEED = 10
WIDTH, HEIGHT = 1200, 800

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
COLOR_SCREEN =(0, 0, 0)
direction = [0, 0]
running = True

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.font = pygame.font.Font(None, 16)
        self.text = "Click Me"
        self.text_color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.x - self.radius < 0: 
            direction[0] = -direction[0]
        elif self.x + self.radius > WIDTH:
            direction[0] = -direction[0]
        if self.y - self.radius < 0:
            direction[1] = -direction[1]
        elif self.y + self.radius > HEIGHT:
            direction[1] = -direction[1]

ball = Ball(600, 400, 25, (0, 255, 0))

while running: 
    screen.fill(COLOR_SCREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction[1] = -1
            if event.key == pygame.K_s:
                direction[1] = 1
            if event.key == pygame.K_a:
                direction[0] = -1
            if event.key == pygame.K_d:
                direction[0] = 1
                
    ball.move(direction[0] * SPEED, direction[1] * SPEED)
    
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
            
pygame.quit()
