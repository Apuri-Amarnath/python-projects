import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMainWindow
from PyQt6.QtGui import QFont

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):

        self.setWindowTitle("Calculator")
        self.buttons = [ ("7", "8", "9", "/"),
                         ("4", "5", "6", "*"),
                         ("1", "2", "3", "-"),
                         ("0", ".", "=", "+"),
                         ("C", "CE","%")
                         ]
        self.layoutv = QVBoxLayout(self)
        self.input_txt_area = QLineEdit(self)
        self.layoutv.addWidget(self.input_txt_area)
        self.fontstyle = QFont()
        self.fontstyle.setPointSize(17)
        for button_r in self.buttons:
            self.layoutH = QHBoxLayout(self)
            for button in button_r:
                self.button = QPushButton(button, self)
                self.layoutH.addWidget(self.button)
                self.button.clicked.connect(self.Action)
                self.button.setFixedSize(110,60)
                self.button.setFont(self.fontstyle)
            self.layoutv.addLayout(self.layoutH)
        self.setLayout(self.layoutv)
        self.input_txt_area.setReadOnly(True)
        self.input_txt_area.setFixedHeight(60)
        self.font = self.input_txt_area.setFont(self.fontstyle)
        self.temp_val = ""
        self.result = None

    def Action(self):
        self.button = self.sender()
        if self.button:
            self.button_text = self.button.text()
            if self.button_text in "0123456789":
                self.temp_val += self.button_text
                self.input_txt_area.setText(self.temp_val)
            elif self.button_text in "*+-/%":
                self.operator_action()
                self.temp_val = ""
            elif self.button_text == "=":
                if self.last_operator:
                    self.operator_action()
                    self.last_operator = None
            elif self.button_text == "C":
                self.input_txt_area.clear()
                self.temp_val = ""
            elif self.button_text == "CE":
                self.input_txt_area.setText("")
                self.temp_val = ""

    def operator_action(self):
        if self.result is None:
            self.result = float(self.temp_val)
        else:
            operand = float(self.temp_val)
            operator = self.input_txt_area.text()[-1]
            if operator == '+':
                self.result += operand
            elif operator == '-':
                self.result -= operand
            elif operator == '*':
                self.result *= operand
            elif operator == '/':
                self.result /= operand
            elif operator == "%":
                self.result %= operand

        self.input_txt_area.setText(str(self.result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Calculator()
    widget.resize(500,500)
    widget.show()
    sys.exit(app.exec())
