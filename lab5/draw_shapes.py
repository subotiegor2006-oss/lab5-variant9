"""Рисование фигур мышью.

Задание повышенной сложности №2.
"""

import tkinter as tk
from tkinter import ttk


class DrawingApp:
    """Простой редактор: линии, прямоугольники и овалы мышью."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Рисование фигур мышью")
        self.root.geometry("640x480")

        self.shape = tk.StringVar(value="line")
        self.color = tk.StringVar(value="black")
        self.start_x = 0
        self.start_y = 0
        self.current_id: int | None = None

        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        tk.Label(toolbar, text="Фигура:").pack(side=tk.LEFT)
        for value, text in [("line", "Линия"), ("rect", "Прямоугольник"), ("oval", "Овал")]:
            ttk.Radiobutton(
                toolbar, text=text, value=value, variable=self.shape
            ).pack(side=tk.LEFT, padx=4)

        tk.Label(toolbar, text="Цвет:").pack(side=tk.LEFT, padx=(12, 0))
        for c in ("black", "red", "blue", "green"):
            ttk.Radiobutton(
                toolbar, text=c, value=c, variable=self.color
            ).pack(side=tk.LEFT, padx=2)

        ttk.Button(toolbar, text="Очистить", command=self.clear).pack(side=tk.RIGHT)

        self.canvas = tk.Canvas(root, bg="white", cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event: tk.Event) -> None:
        self.start_x = event.x
        self.start_y = event.y
        self.current_id = None

    def on_drag(self, event: tk.Event) -> None:
        if self.current_id is not None:
            self.canvas.delete(self.current_id)

        shape = self.shape.get()
        color = self.color.get()

        if shape == "line":
            self.current_id = self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y, fill=color, width=2
            )
        elif shape == "rect":
            self.current_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, event.x, event.y, outline=color, width=2
            )
        else:
            self.current_id = self.canvas.create_oval(
                self.start_x, self.start_y, event.x, event.y, outline=color, width=2
            )

    def on_release(self, event: tk.Event) -> None:
        self.current_id = None

    def clear(self) -> None:
        self.canvas.delete("all")


def main() -> None:
    root = tk.Tk()
    DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
