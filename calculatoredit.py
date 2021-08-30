from calcedit import Ui_back
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from math import *


class calculator(QMainWindow, Ui_back):

    def __init__(self):
        super(calculator, self).__init__()
        self.setupUi(self)

        #number buttons
        self.one.clicked.connect(self.fpress)
        self.two.clicked.connect(self.fpress)
        self.three.clicked.connect(self.fpress)
        self.four.clicked.connect(self.fpress)
        self.five.clicked.connect(self.fpress)
        self.six.clicked.connect(self.fpress)
        self.seven.clicked.connect(self.fpress)
        self.eight.clicked.connect(self.fpress)
        self.nine.clicked.connect(self.fpress)
        self.zero.clicked.connect(self.fpress)

        #calculation buttons
        self.add.clicked.connect(self.fcalculation)
        self.sub.clicked.connect(self.fcalculation)
        self.mul.clicked.connect(self.fcalculation)
        self.div.clicked.connect(self.fcalculation)

        #equal button
        self.equal.clicked.connect(self.fequal)

        #c button
        self.c.clicked.connect(self.fc)

        #parentheses buttons
        self.openpar.clicked.connect(self.fpar)
        self.closepar.clicked.connect(self.fpar)


    def fpress(self):
        button  = self.sender()
        self.result.setText(self.result.text() + button.text())


    def fcalculation(self):
        button = self.sender()
        self.result.setText(self.result.text() + button.text())



    def calculation(self):
        importance = {'+': 1, '-': 1, '*': 2, '/': 2}
        ch = self.sender()
        self.stack = []
        self.exp = []



        if ch in "012356789":
            self.stack.push()
        elif ch == '(':
            self.stack.push()
        elif ch == '+' or '-' or '*' or '/':
            if self.stack.peek() == '(':
                self.stack.push()
            elif self.stack.peek.importance() > ch.importance():
                self.stack.push()
            elif self.stack.peek.importance() <= ch.importance():
                ch = self.stack.peek.pop()
                self.exp.push(ch)
            elif self.stack.peek() == ')':
                while self.stack.peek() != '(':
                    self.stack.push()

        if self.equal.clicked:
            if "012345679" in self.exp:
                self.stack.push()
            right = self.stack.pop()
            left = self.stack.pop()
            answer = 0

            if self.exp.pop() == '+':
                answer = left + right
            if self.exp.pop() == '-':
                answer = left - right
            if self.exp.pop() == '*':
                answer = left * right
            if self.exp.pop() == '/':
                answer = left / right

            self.stack.push(answer)




    def fequal(self, stack):
        self.stack = self.result.text()
        try:
            self.result.setText(self.calculation.stack)
        except:
            self.result.setText("ERROR")



    def fc(self):
        self.result.setText(None)


    def fpar(self):
        button = self.sender()
        self.result.setText(self.result.text() + button.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = calculator()
    calc.show()
    sys.exit(app.exec_())
