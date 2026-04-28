import tkinter as tk
import copy
from core.astar import a_star
from ui.colors import tile_colors, bg_color, board_bg
from models.state import start, goal

class Puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("A* 8 Puzzle")
        self.root.configure(bg=bg_color)

        self.size = 90

        top = tk.Frame(root, bg=bg_color)
        top.pack(pady=15)

        # Current
        current_frame = tk.Frame(top, bg=bg_color)
        current_frame.pack(side="left", padx=20)

        tk.Label(current_frame, text="Current",
                 bg=bg_color, fg="white").pack()

        self.main_canvas = tk.Canvas(current_frame, width=270, height=270,
                                     bg=board_bg, highlightthickness=0)
        self.main_canvas.pack()

        # Goal
        goal_frame = tk.Frame(top, bg=bg_color)
        goal_frame.pack(side="left", padx=20)

        tk.Label(goal_frame, text="Goal",
                 bg=bg_color, fg="white").pack()

        self.goal_canvas = tk.Canvas(goal_frame, width=270, height=270,
                                     bg=board_bg, highlightthickness=0)
        self.goal_canvas.pack()

        # Info
        self.moves = 0
        self.moves_label = tk.Label(root, text="Moves: 0",
                                    bg=bg_color, fg="white")
        self.moves_label.pack()

        self.msg = tk.Label(root, text="",
                            bg=bg_color, fg="#22c55e")
        self.msg.pack()

        # Buttons
        btns = tk.Frame(root, bg=bg_color)
        btns.pack(pady=10)

        tk.Button(btns, text="Start Solve",
                  command=self.solve).grid(row=0, column=0, padx=5)

        tk.Button(btns, text="Reset",
                  command=self.reset).grid(row=0, column=1, padx=5)

        self.state = copy.deepcopy(start)
        self.solution = []
        self.step = 0

        self.draw_board(self.goal_canvas, goal)
        self.draw_board(self.main_canvas, self.state)

    def draw_board(self, canvas, state):
        canvas.delete("all")

        for i in range(3):
            for j in range(3):
                v = state[i][j]

                x1 = j * self.size
                y1 = i * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size

                if v == 0:
                    canvas.create_rectangle(x1, y1, x2, y2,
                                            fill="#0f172a")
                    continue

                color = tile_colors.get(v)

                canvas.create_rectangle(
                    x1+5, y1+5, x2-5, y2-5,
                    fill=color
                )

                canvas.create_text(
                    x1 + self.size/2,
                    y1 + self.size/2,
                    text=str(v),
                    fill="white"
                )

    def animate(self):
        if self.step >= len(self.solution):
            self.msg.config(text="Solved >>>>siiiiiiiiiii<<<<< ")
            return

        self.state = self.solution[self.step]
        self.step += 1
        self.moves += 1

        self.moves_label.config(text=f"Moves: {self.moves}")
        self.draw_board(self.main_canvas, self.state)

        self.root.after(500, self.animate)

    def solve(self):
        self.msg.config(text="Solving...")

        self.solution = a_star(self.state, goal)
        self.step = 0
        self.moves = 0

        if not self.solution:
            self.msg.config(text="No solution")
            return

        self.animate()

    def reset(self):
        self.state = copy.deepcopy(start)
        self.solution = []
        self.step = 0
        self.moves = 0

        self.moves_label.config(text="Moves: 0")
        self.msg.config(text="")
        self.draw_board(self.main_canvas, self.state)