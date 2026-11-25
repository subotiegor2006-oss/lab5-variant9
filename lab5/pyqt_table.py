"""Приложение PyQt с таблицей.

Задание повышенной сложности №9.
"""

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QHeaderView,
)
from PyQt5.QtCore import Qt


SAMPLE_DATA = [
    ("Иванов", "Алексей", "221341", "4.5"),
    ("Петрова", "Мария", "221341", "4.8"),
    ("Сидоров", "Иван", "221342", "3.9"),
    ("Козлова", "Анна", "221341", "5.0"),
    ("Морозов", "Дмитрий", "221343", "4.2"),
]


class TableWindow(QMainWindow):
    """Окно с редактируемой таблицей студентов."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Таблица студентов — PyQt5")
        self.resize(620, 360)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Фамилия", "Имя", "Группа", "Балл"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)

        for row_data in SAMPLE_DATA:
            self._add_row(row_data)

        buttons = QHBoxLayout()
        btn_add = QPushButton("Добавить строку")
        btn_add.clicked.connect(self.add_empty_row)
        btn_del = QPushButton("Удалить выбранную")
        btn_del.clicked.connect(self.delete_selected)
        btn_info = QPushButton("Инфо")
        btn_info.clicked.connect(self.show_info)
        buttons.addWidget(btn_add)
        buttons.addWidget(btn_del)
        buttons.addWidget(btn_info)
        layout.addLayout(buttons)

    def _add_row(self, values: tuple[str, ...]) -> None:
        row = self.table.rowCount()
        self.table.insertRow(row)
        for col, value in enumerate(values):
            item = QTableWidgetItem(value)
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, col, item)

    def add_empty_row(self) -> None:
        self._add_row(("", "", "", ""))

    def delete_selected(self) -> None:
        rows = sorted({idx.row() for idx in self.table.selectedIndexes()}, reverse=True)
        if not rows:
            QMessageBox.information(self, "Удаление", "Выберите строку")
            return
        for row in rows:
            self.table.removeRow(row)

    def show_info(self) -> None:
        count = self.table.rowCount()
        QMessageBox.information(
            self,
            "Информация",
            f"Строк в таблице: {count}\nСтолбцов: {self.table.columnCount()}",
        )


def main() -> None:
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
