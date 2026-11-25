"""Прогрессбар.

Задание средней сложности №6.
"""

import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Прогрессбар")
    root.geometry("400x180")
    root.resizable(False, False)

    status = tk.Label(root, text="Готов", font=("Arial", 11))
    status.pack(pady=10)

    progress = ttk.Progressbar(
        root,
        orient="horizontal",
        length=300,
        mode="determinate",
        maximum=100,
    )
    progress.pack(pady=10)

    percent = tk.Label(root, text="0%", font=("Arial", 10))
    percent.pack()

    def step() -> None:
        value = progress["value"]
        if value < 100:
            progress["value"] = value + 5
            percent.config(text=f"{int(progress['value'])}%")
            status.config(text="Выполняется...")
            root.after(100, step)
        else:
            status.config(text="Готово!")

    def start() -> None:
        progress["value"] = 0
        percent.config(text="0%")
        status.config(text="Выполняется...")
        step()

    def reset() -> None:
        progress["value"] = 0
        percent.config(text="0%")
        status.config(text="Готов")

    frame = tk.Frame(root)
    frame.pack(pady=15)

    tk.Button(frame, text="Старт", width=10, command=start).pack(side=tk.LEFT, padx=5)
    tk.Button(frame, text="Сброс", width=10, command=reset).pack(side=tk.LEFT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
