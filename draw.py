from tkinter import messagebox
import pygame
import tkinter as tk





# color
color = (135, 206, 235)
BLACK = (0, 0, 0)

# font types
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

drawing = False
last_pos = None

# var for width of pencil
w = 4


def init():
    global screen

    pygame.init()
    mainloop()


screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('DrawPy')

# tkinter for popup msg
root = tk.Tk()
root.wm_withdraw()  # to hide the main window
messagebox.showinfo('Welcome!', 'Press "c" to clear the screen, and "s" to save the image.')


def draw(event):
    global drawing, last_pos, w

    if event.type == pygame.MOUSEMOTION:
        if (drawing):
            mouse_position = pygame.mouse.get_pos()
            if last_pos is not None:
                pygame.draw.line(screen, color, last_pos, mouse_position, w)
            last_pos = mouse_position
    elif event.type == pygame.MOUSEBUTTONUP:
        mouse_position = (0, 0)
        drawing = False
        last_pos = None
    elif event.type == pygame.MOUSEBUTTONDOWN:
        drawing = True


def mainloop():
    global screen

    loop = 1
    while loop:
        # checks every user interaction in this list
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.image.save(screen, "drawing.png")
                    messagebox.showinfo('Image saved!','Press "c" to clear and do another!')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    screen.fill(BLACK)
            draw(event)
        pygame.display.flip()
    pygame.quit()


init()

