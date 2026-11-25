"""Меню запуска заданий лабораторной работы №5."""

import tkinter as tk
from tkinter import messagebox


def run_hello() -> None:
    from lab5.hello_button import main as hello_main
    hello_main()


def run_progress() -> None:
    from lab5.progress_bar import main as progress_main
    progress_main()


def run_color() -> None:
    from lab5.color_panel import main as color_main
    color_main()


def run_draw() -> None:
    from lab5.draw_shapes import main as draw_main
    draw_main()


def run_pyqt() -> None:
    try:
        from lab5.pyqt_table import main as pyqt_main
        pyqt_main()
    except ImportError:
        messagebox.showerror(
            "PyQt5",
            "Не установлен PyQt5.\nУстановите: pip install PyQt5",
        )


def main() -> None:
    root = tk.Tk()
    root.title("ЛР №5 — вариант 9")
    root.geometry("360x340")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Лабораторная работа №5\nВариант 9",
        font=("Arial", 13, "bold"),
    ).pack(pady=12)

    tk.Label(root, text="Субботин Егор Сергеевич, 221341").pack()

    frame = tk.Frame(root)
    frame.pack(pady=16)

    buttons = [
        ("№1  Кнопка «Привет»", run_hello),
        ("№6  Прогрессбар", run_progress),
        ("№9  Цветная панель", run_color),
        ("№2↑ Рисование мышью", run_draw),
        ("№9↑ PyQt таблица", run_pyqt),
    ]

    for text, cmd in buttons:
        tk.Button(frame, text=text, width=28, command=cmd).pack(pady=4)

    root.mainloop()


if __name__ == "__main__":
    main()
