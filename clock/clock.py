import pygame 
import datetime

pygame.init()

SPEED = 5
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))
running = True

CLOCK = pygame.image.load("clock/clock.jpg")
HOUR = pygame.image.load("clock/hour.png")
MIN = pygame.image.load("clock/min.png")

HOUR = pygame.transform.scale(HOUR, (200, 200))
MIN = pygame.transform.scale(MIN, (230, 240))

clock_rect = CLOCK.get_rect(center=(600, 400))
hour_rect = HOUR.get_rect(center=(530, 340))
min_rect = MIN.get_rect(center=(700, 320))

def Angle_img(surf, image, image_rect, angle, pos):
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255))
    now = datetime.datetime.now()
    hour_angle = -((now.minute % 60) * 6 + now.second * 0.1)  
    min_angle = -(now.second * 6) 
    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.blit(CLOCK, clock_rect)
    Angle_img(screen,HOUR,hour_rect, hour_angle, pos)       
    Angle_img(screen,MIN, min_rect, min_angle, pos) 
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
