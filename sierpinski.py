import pygame
# hello! this is a change!

colors = [pygame.Color(0, 0, 0, 255),       # Black
          pygame.Color(255, 0, 0, 255),     # Red
          pygame.Color(0, 255, 0, 255),     # Green
          pygame.Color(0, 0, 255, 255),     # Blue
          pygame.Color(255, 255, 255, 255)] # White


BLACK = 0
RED = 1
GREEN = 2
BLUE = 3
WHITE = -1


def draw_triangle(p1, p2, p3, color, line_width, screen):
    pygame.draw.polygon(screen, colors[color], [p1, p2, p3], line_width)
    pygame.display.flip()


def find_midpoint(p1, p2):
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return [x, y]


def sierpinski(degree, p1, p2, p3, color, line_width, screen):
    if(degree != -1):
        degree -= 1
        draw_triangle(p1, p2, p3, color, line_width, screen)
        p1x = p1
        p2x = find_midpoint(p1,p2)
        p3x = find_midpoint(p1,p3)
        p1y = find_midpoint(p2,p1)
        p2y = p2
        p3y = find_midpoint(p2,p3)
        p1z = find_midpoint(p3,p1)
        p2z = find_midpoint(p3,p2)
        p3z = p3
        sierpinski(degree, p1x, p2x, p3x, color, line_width, screen)
        sierpinski(degree, p1y, p2y, p3y, color, line_width, screen)
        sierpinski(degree, p1z, p2z, p3z, color, line_width, screen)

def main():
    pygame.init()

    width = 640 
    height = 640 
    size = [width, height] 

    p1 = [5, height - 5]
    p2 = [(width - 10) / 2, 5]
    p3 = [width - 5, height - 5]
    initial_color = BLACK 
    initial_line_width = 1 

    degree = 5 
    
    pygame.display.set_caption("Sierpinski Triangle")
    
    screen = pygame.display.set_mode(size)
    
    screen.fill(WHITE)
    pygame.display.flip()
    
    sierpinski(degree, p1, p2, p3, initial_color, initial_line_width, screen)


    done = False
    count = 0
    while not done:
        count = count + 1
        if count % 1000000 == 0:
            print(".", end = "")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    print("\nNow Quitting")
    pygame.quit()

    

if __name__ == "__main__":
    main()
