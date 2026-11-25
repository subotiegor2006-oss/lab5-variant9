"""Окно с кнопкой «Привет».

Задание средней сложности №1.
"""

import tkinter as tk
from tkinter import messagebox


def main() -> None:
    root = tk.Tk()
    root.title("Привет")
    root.geometry("320x160")
    root.resizable(False, False)

    label = tk.Label(root, text="Нажми кнопку", font=("Arial", 14))
    label.pack(pady=20)

    def on_click() -> None:
        messagebox.showinfo("Привет", "Привет!")
        label.config(text="Привет!")

    button = tk.Button(
        root,
        text="Привет",
        font=("Arial", 12),
        width=12,
        command=on_click,
    )
    button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
