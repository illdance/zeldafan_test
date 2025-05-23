from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

def show_win():
    victory_window = QMessageBox()
    victory_window.setText('Да вы настоящий фанат! Но я знаю что ты гуглил!')
    victory_window.exec()

def show_lose():
    victory_window = QMessageBox()
    victory_window.setText('Так-то их 900... ПОЗОР!')
    victory_window.exec()

app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест на фаната Zelda')
window.resize(800, 250)
text = QLabel('Сколько короков в "The Legend of Zelda: Breath of The Wild"?')

r_btn1 = QRadioButton('940')
r_btn1.clicked.connect(show_lose)
r_btn2 = QRadioButton('421')
r_btn2.clicked.connect(show_lose)
r_btn3 = QRadioButton('900')
r_btn3.clicked.connect(show_win)
r_btn4 = QRadioButton('1250')
r_btn4.clicked.connect(show_lose)

v_line = QVBoxLayout()
h_line = QHBoxLayout()
h_line0 = QHBoxLayout()
h_line1 = QHBoxLayout()

h_line.addWidget(text, alignment = Qt.AlignCenter)
h_line0.addWidget(r_btn1, alignment = Qt.AlignCenter)
h_line0.addWidget(r_btn2, alignment = Qt.AlignCenter)
h_line1.addWidget(r_btn3, alignment = Qt.AlignCenter)
h_line1.addWidget(r_btn4, alignment = Qt.AlignCenter)

v_line.addLayout(h_line)
v_line.addLayout(h_line0)
v_line.addLayout(h_line1)

window.setLayout(v_line)
window.show()
app.exec()