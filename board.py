from tkinter import Button, Label
import random
import sys
import config


class Cell:
    all = []
    cell_count = config.cell_count
    mine_count = config.mine_count
    mine_count_label = None

    def __init__(self, x, y, is_mine = False):
        self.x = x 
        self.y = y
        self.is_mine = is_mine
        self.button = None
        self.is_open = False
        self.can_be_mine = False

        Cell.all.append(self)

    def create_button(self, location):
        button = Button(location, 
                        bg = "lightpink2",
                        width = 1, 
                        height = 1) 
            
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-3>", self.right_click)

        self.button = button

    @staticmethod
    def create_mine_count_label(location):
        label = Label(
            location,
            bg = "light blue",
            fg = "black",
            text = f"Flags: {Cell.mine_count}",
            font = ("12") 
        )
        Cell.mine_count_label = label

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_mine_count == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
            self.show_cell()
            
            if Cell.cell_count == config.mine_count:
                sys.exit()

        self.button.unbind("<Button-1>")
        self.button.unbind("<Button-3>")

    def cell_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property            
    def surrounding_cells(self):
        cells = [self.cell_axis(self.x-1, self.y-1),
                self.cell_axis(self.x, self.y-1),
                self.cell_axis(self.x+1, self.y-1),
                self.cell_axis(self.x+1, self.y),
                self.cell_axis(self.x+1, self.y+1),
                self.cell_axis(self.x, self.y+1),
                self.cell_axis(self.x-1, self.y+1),
                self.cell_axis(self.x-1, self.y),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property    
    def surrounding_mine_count(self):
        count = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                count += 1
        return count
    
    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.button.configure(text = self.surrounding_mine_count)
            self.button.configure(bg = "lightpink2")
        self.is_open = True

    def show_mine(self):
        self.button.configure(bg = "red")

    def right_click(self, event):
        if not self.can_be_mine:
            self.button.configure(bg = "deep pink")
            self.can_be_mine = True
            Cell.mine_count -= 1
            if Cell.mine_count_label:
                Cell.mine_count_label.configure(text = f"Flags: {Cell.mine_count}")
        else:
            self.button.configure(bg = "lightpink2")
            self.can_be_mine = False

    @staticmethod
    def random_mines():
        chosen_cells = random.sample(Cell.all, config.mine_count)
        for cell in chosen_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell{self.x}, {self.y}"