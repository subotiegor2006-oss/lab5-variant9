"""Цветная панель — меняет цвет по кнопке.

Задание средней сложности №9.
"""

import tkinter as tk
from itertools import cycle

COLORS = [
    ("#e74c3c", "Красный"),
    ("#3498db", "Синий"),
    ("#2ecc71", "Зелёный"),
    ("#f1c40f", "Жёлтый"),
    ("#9b59b6", "Фиолетовый"),
    ("#1abc9c", "Бирюзовый"),
    ("#e67e22", "Оранжевый"),
    ("#34495e", "Тёмно-серый"),
]


def main() -> None:
    root = tk.Tk()
    root.title("Цветная панель")
    root.geometry("420x280")
    root.resizable(False, False)

    color_cycle = cycle(COLORS)
    current = next(color_cycle)

    panel = tk.Frame(root, bg=current[0], width=380, height=160)
    panel.pack(pady=20, padx=20)
    panel.pack_propagate(False)

    name_label = tk.Label(
        panel,
        text=current[1],
        font=("Arial", 16, "bold"),
        bg=current[0],
        fg="white",
    )
    name_label.place(relx=0.5, rely=0.5, anchor="center")

    def change_color() -> None:
        color, name = next(color_cycle)
        panel.config(bg=color)
        name_label.config(text=name, bg=color)

    tk.Button(
        root,
        text="Сменить цвет",
        font=("Arial", 12),
        width=16,
        command=change_color,
    ).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
