import tkinter
from tkinter import font
import pygame
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Tik Tac Toe")
window.geometry("300x250")
window.resizable(width=False, height=False)
window.configure(bg='#a9b4f5')

myFont = font.Font(size=20)


def run_game():
    window.withdraw()
    black = (0, 0, 0)
    white = (255, 255, 255)
    size = 100
    margin = 5

    pygame.init()
    dis = pygame.display.set_mode((320, 320))
    pygame.display.update()
    pygame.display.set_caption("Tick Tack Toe")
    dis.fill(white)
    game_over = False

    position = []
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player1 = True
    draw = False
    quit_game = False

    def main_map():
        pygame.draw.line(dis, black, [2.5, 5], [2.5, 315], 5)
        pygame.draw.line(dis, black, [107.5, 5], [107.5, 315], 5)
        pygame.draw.line(dis, black, [212.5, 5], [212.5, 315], 5)
        pygame.draw.line(dis, black, [317.5, 5], [317.5, 315], 5)

        pygame.draw.line(dis, black, [0, 2.5], [320, 2.5], 5)
        pygame.draw.line(dis, black, [0, 107.5], [320, 107.5], 5)
        pygame.draw.line(dis, black, [0, 212.5], [320, 212.5], 5)
        pygame.draw.line(dis, black, [0, 317.5], [320, 317.5], 5)

    def check_win():
        if board[0][0] == board[1][1] == board[2][2] != 0:
            draw_asc_diagonal()
            return True

        if board[2][0] == board[1][1] == board[0][2] != 0:
            draw_desc_diagonal()
            return True

        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != 0:
                draw_vertical_line(j)
                return True

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                draw_horizontal_line(i)
                return True

    def draw_vertical_line(col):
        pygame.draw.line(dis, black, [(col + 1) * margin + col * size + 50, 15],
                         [(col + 1) * margin + col * size + 50, 300], 7)

    def draw_horizontal_line(line):
        pygame.draw.line(dis, black, [15, (line + 1) * margin + line * size + 50],
                         [300, (line + 1) * margin + line * size + 50], 7)

    def draw_asc_diagonal():
        pygame.draw.line(dis, black, [15, 15], [300, 300], 7)

    def draw_desc_diagonal():
        pygame.draw.line(dis, black, [300, 15], [15, 300], 7)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                quit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
        for row in range(3):
            for column in range(3):
                # pygame.draw.rect(dis, white, pygame.Rect((MARGIN + SIZE) * column + MARGIN,
                #                                          (MARGIN + SIZE) * row + MARGIN, SIZE, SIZE))
                main_map()
                if position:
                    x_from = (row + 1) * margin + row * size
                    x_to = (row + 1) * margin + (row + 1) * size
                    y_from = (column + 1) * margin + column * size
                    y_to = (column + 1) * margin + (column + 1) * size
                    if x_from < position[0] < x_to and y_from < position[1] < y_to:
                        if player1 and board[column][row] == 0:
                            board[column][row] = 1
                            if not check_win():
                                player1 = not player1
                            else:
                                game_over = True
                        elif not player1 and board[column][row] == 0:
                            board[column][row] = 2
                            if not check_win():
                                player1 = not player1
                            else:
                                game_over = True
                        else:
                            flag = True
                            for a in range(3):
                                for b in range(3):
                                    if board[a][b] == 0 and not game_over:
                                        flag = False
                            if flag:
                                draw = True
                                game_over = True

        for row in range(3):
            for column in range(3):
                if board[column][row] == 1:
                    pygame.draw.line(dis, black, [(row + 1) * margin + row * size + 25,
                                                  (column + 1) * margin + column * size + 25],
                                     [(row + 1) * margin + (row + 1) * size - 25,
                                      (column + 1) * margin + (column + 1) * size - 25], 15)
                    pygame.draw.line(dis, black, [(row + 1) * margin + (row + 1) * size - 25,
                                                  (column + 1) * margin + column * size + 25],
                                     [(row + 1) * margin + row * size + 25,
                                      (column + 1) * margin + (column + 1) * size - 25], 15)
                elif board[column][row] == 2:
                    pygame.draw.circle(dis, black, [(row + 1) * margin + row * size + 50,
                                                    (column + 1) * margin + column * size + 50], 35, 9)

        pygame.display.flip()

    if not draw and not quit_game:
        if not player1:
            messagebox.showinfo("Сongratulation", "Player 2 wins!")
        else:
            messagebox.showinfo("Сongratulation", "Player 1 wins!")
    elif draw:
        messagebox.showinfo("Сongratulation", "It’s draw!")

    pygame.quit()
    window.deiconify()


button_play = Button(window, text="Play", height=1, width=10, font=myFont, bd=0, bg="#5f6ffa", command=run_game)
button_play.place(x=70, y=50)

button_exit = Button(window, text="Exit", height=1, width=10, font=myFont, bd=0, bg="#5f6ffa", command=window.destroy)
button_exit.place(x=70, y=140)

window.mainloop()
