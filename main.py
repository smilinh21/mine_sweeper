from tkinter import *
import config
from board import Cell

root = Tk()

root.configure(bg = "mint cream")

root.geometry(f'{config.width}x{config.height}')

root.title("Minesweeper")

root.resizable(False, False)

top_frame = Frame(root, bg = "pale green",
                  width = config.width,
                  height = config.height_pct(10))

top_frame.place(x = 0, y = 0)

game_title = Label(
    top_frame,
    bg = "pale green",
    fg = "black",
    text = "Minesweeper",
    font = ('', 25)
)

game_title.place(relx = 0.5, rely = 0.5, anchor = "center")


center_frame = Frame(root, bg  = "antique white",
                     width = config.width_pct(70),
                     height = config.height_pct(70))

center_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

bottom_frame = Frame(root, bg = "light blue",
                  width = config.width,
                  height = config.height_pct(10))

bottom_frame.place(x = 0, y = config.height_pct(90))


for x in range(config.num_rows):
    for y in range(config.num_rows):
        c = Cell(x, y)
        c.create_button(center_frame)
        c.button.grid(column = x, row = y)


Cell.create_mine_count_label(bottom_frame)
Cell.mine_count_label.place(relx = 0.5, rely = 0.5, anchor = "center")

Cell.random_mines()


root.mainloop()
