import pygame
pygame.init()

#Setting the screen dimensions
screen = pygame.display.set_mode((600,600))
screen.fill('Cyan')

pygame.display.update()

class rect:
    def __init__(self, dim, color):
        self.rect_surf = screen
        self.rect_dim = dim
        self.rect_color = color
    
    def draw(self):
        self.draw_rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dim)

rect1 = rect((50,20,100,100),'Red')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect1.draw()
    pygame.display.update()


pygame.quit()