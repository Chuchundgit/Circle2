import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)

        self.pushButton = QtWidgets.QPushButton("Add Circle", self)
        self.pushButton.setGeometry(0, 260, 800, 80)

        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(circle[3])
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        diameter = random.randint(20, 200)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = self.random_color()
        self.circles.append((x, y, diameter, color))
        self.update()

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return QColor(r, g, b)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())