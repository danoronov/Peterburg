import sys

import random
from PyQt5.QtGui import QPainter, QColor 
from PyQt5.QtWidgets import QApplication, QMainWindow
from setupui import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow): # наследование от двух классов
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint) # запуск рисования
        self.do_paint = False # пока нет рисования

    
    def paintEvent(self, event): # стандартная функция организации рисования
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self): # выдача разрешения на рисование
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp): # рисование цветного круга
        qp.setBrush(QColor(random.randint(0, 255),
                           random.randint(0, 255), random.randint(0, 255)))
        d = random.randint(20, 150)
        qp.drawEllipse(100 - d // 2, 100 - d // 2, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
