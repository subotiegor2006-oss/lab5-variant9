# Лабораторная работа №5

Субботин Егор Сергеевич, группа 221341, вариант 9, лабораторная №5.

## Задания варианта

Средняя сложность:

- №1 — окно с кнопкой «Привет»
- №6 — прогрессбар
- №9 — цветная панель (меняет цвет по кнопке)

Повышенная сложность:

- №2 — рисование фигур мышью
- №9 — приложение PyQt с таблицей

## Зависимости

```bash
pip install -r requirements.txt
```

(PyQt5 нужен только для задания №9 повышенной сложности)

## Запуск

```bash
# Все примеры (меню выбора)
python -m lab5

# По отдельности
python -m lab5.hello_button
python -m lab5.progress_bar
python -m lab5.color_panel
python -m lab5.draw_shapes
python -m lab5.pyqt_table
```

## Структура

```text
lab5/
├── __init__.py
├── __main__.py          # меню запуска
├── hello_button.py      # №1
├── progress_bar.py      # №6
├── color_panel.py       # №9
├── draw_shapes.py       # №2 (повышенная)
└── pyqt_table.py        # №9 (повышенная)
```
