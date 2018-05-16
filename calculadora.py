import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,QLineEdit,
#                             QHBoxLayout, QVBoxLayout, QPushButton)

class Button:
    def __init__(self, text, res):
        self.text = str(text)
        self.b = QPushButton(self.text)
        self.res = res
        #cria o slot
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    # pega o botão que foi clicado
    def handleInput(self, v):
        try:
            if v == '=':
                self.res.setText(str(eval(self.res.text())))
            elif v == 'AC':
                self.res.setText('')
            elif v == '√':
                value = float(self.res.text())
                self.res.setText(str(math.sqrt(value)))
            elif v == 'DEL':
                current_value = self.res.text()
                self.res.setText(current_value[:-1])
            else:
                current_value = self.res.text()
                new_value = current_value + str(v)
                self.res.setText(new_value)
        except Exception:
             pass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.init_ui()

    def init_ui(self):

        #Cria nosso grid
        grid = QGridLayout()
        res = QLineEdit()

        buttons = ['AC', '√', '%', '/',
                    7,8,9,'*',
                    4,5,6,'-',
                    1,2,3,'+',
                    0, '.', '=']
        row = 1
        col = 0
        grid.addWidget(res,0,0,1,4)

        for button in buttons:
            if col > 3:
                col = 0
                row+= 1
            buttonObject = Button(button,res)
            if button == 0:
                grid.addWidget(buttonObject.b, row, col, 1, 2)
                col+=1
            else:
                grid.addWidget(buttonObject.b, row, col,1,1)
            col+= 1

        self.setLayout(grid)

        self.show()

if __name__ =='__main__':
    app =QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
