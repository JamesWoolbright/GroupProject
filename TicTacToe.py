import tkinter as tk
from itertools import cycle
from tkinter import Button, Label, Tk,font
from typing import NamedTuple # imports NamedTuple from typing.
import time as t
from tkinter import ttk

class Player(NamedTuple): # define the Player class
    label: str
    color: str

class Move(NamedTuple): # define the Move class
    row: int
    col: int
    label: str = ""

style = ttk.Style()
style.configure('style1', font=('Times', 30))

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="beige"),
    Player(label="O", color="beige"),
)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self._players)

    def is_valid_move(self, move):
        """Return True if move is valid, and False otherwise."""
        row, col = move.row, move.col # gets the .row and .col coordinates from the input move.
        move_was_not_played = self._current_moves[row][col].label == "" # checks if the move at the current coordinates, [row][col], still holds an empty string as its label.
        no_winner = not self._has_winner # checks if the game doesn’t have a winner yet.
        return no_winner and move_was_not_played

    def process_move(self, move): # defines process_move(), which takes a Move object as an argument.
        """Process the current move and check if it's a win."""
        row, col = move.row, move.col # gets the .row and .col coordinates from the input move.
        self._current_moves[row][col] = move # assigns the input move to the item at [row][col] in the list of current moves.
        for combo in self._winning_combos: # starts a loop over the winning combinations.
            results = set(self._current_moves[n][m].label for n, m in combo) # run a generator expression that retrieves all the labels from the moves in the current winning combination
            is_win = (len(results) == 1) and ("" not in results)
            if is_win: # checks the content of is_win.
                self._has_winner = True
                self.winner_combo = combo # defines a Boolean expression that checks if the current move determined a win or not.
                break

    def has_winner(self):
        """Return True if the game has a winner, and False otherwise."""
        return self._has_winner

    def is_tied(self):
        """Return True if the game is tied, and False otherwise."""
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def reset_game(self):
        """Reset the game state to play again."""
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []
def quit():
    global t1
    t1 = False
class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_menu(self): # defines a helper method called ._create_menu() to handle the menu creation in a single place.
        menu_bar = tk.Menu(master=self) # creates an instance of Menu, which will work as the menu bar
        self.config(menu=menu_bar) # sets the menu bar object as the main menu of your current Tkinter window
        file_menu = tk.Menu(master=menu_bar) #  creates another instance of Menu to provide a File menu
        file_menu.add_command(label="Play Again", command=self.reset_board) # add a new menu option to the File menu using the .add_command() method.
        file_menu.add_separator() #  adds a menu separator using the .add_separator() method
        file_menu.add_command(label="Exit", command=quit) # adds an Exit command to the File menu.
        menu_bar.add_cascade(label="Restart", menu=file_menu) #  adds the File menu to the menu bar by calling .add_cascade() with appropriate arguments.

    def _create_board_display(self):
        display_frame = tk.Frame(master=self) # creates a Frame object to hold the game display.
        display_frame.pack(fill=tk.X) # uses the .pack() geometry manager to place the frame object on the main window’s top border
        display_frame.config(bg='#F5F5DC')
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
            bg="black",
            fg='white'
        ) # creates a Label object
        self.display.config(bg='#F5F5DC', fg='black', font=('Arial', 50, font.BOLD))
        self.display.pack() #  packs the display label inside the frame using the .pack() geometry manager

    def _create_board_grid(self): 
        grid_frame = tk.Frame(master=self) # creates a Frame object to hold the game’s grid of cells
        grid_frame.config(bg='#F5F5DC')
        grid_frame.pack() # uses the .pack() geometry manager to place the frame object on the main window
        for row in range(self._game.board_size): # starts a loop that iterates from 0 to 2.
            self.rowconfigure(row, weight=1, minsize=100) # configure the width and minimum size of every cell on the grid. 
            self.columnconfigure(row, weight=1, minsize=150)
            for col in range(self._game.board_size): # loops over the three column coordinates. 
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=20,
                    height=14,
                    highlightbackground="lightblue",
                ) # create a Button object for every cell on the grid. 
                self._cells[button] = (row, col) # adds every new button to the ._cells dictionary
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew") # add every button to the main window using the .grid() geometry manager.
                button.config(bd='3', relief='solid')

    def play(self, event): # defines play(), which takes a Tkinter event object as an argument.
        """Handle a player's move."""
        clicked_btn = event.widget # retrieves the widget that triggered the current event
        row, col = self._cells[clicked_btn] # unpacks the button’s coordinates into two local variables, row and col.
        move = Move(row, col, self._game.current_player.label) # creates a new Move object using row, col, and the current player’s .label attribute as arguments.
        if self._game.is_valid_move(move): # starts a conditional statement that checks if the player’s move is valid or not
            self._update_button(clicked_btn) # updates the clicked button by calling the ._update_button() method
            self._game.process_move(move) # calls .process_move() on the ._game object using the current move as an argument.
            if self._game.is_tied(): # checks if the game is tied
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner(): # checks if the current player has won the game
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = "Black"
                self._update_display(msg, color)
            else: # runs if the game isn’t tied and there’s no winner
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color, bg='#D2B48C' )

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        """Reset the game's board to play again."""
        self._game.reset_game() # calls .reset_game() to reset the board’s abstract representation.
        self._update_display(msg="Ready?") # updates the board display to hold the initial text, "Ready?"
        for button in self._cells.keys(): # starts a loop over the buttons on the board grid
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black", bg='#F8F0E3') #  restore every button’s highlightbackground, text, and fg properties to their initial state
t1 = True
def main():
    """Create the game's board and run its main loop."""
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.config(bg='#F8F0E3')
    board.attributes('-fullscreen',True)
    while t1 == True:
        board.update()
    board.destroy()
