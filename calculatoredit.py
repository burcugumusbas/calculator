from calcedit import Ui_back
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


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

        #click check??
        self.add.setCheckable(True)
        self.sub.setCheckable(True)
        self.mul.setCheckable(True)
        self.div.setCheckable(True)

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
        button.setChecked(True)


    #def calculation(self):



    def fequal(self):
        self.result.setText()


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