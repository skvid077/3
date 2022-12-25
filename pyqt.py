import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sqlite3


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        db = sqlite3.connect('coffee.sqlite')
        cur = db.cursor()
        coffee = cur.execute("""SELECT * FROM cof""").fetchall()
        for i in coffee:
            self.lst.addItem(' '. join(list(map(str, list(i)))))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
