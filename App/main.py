import os
import re
import sys
import traceback

from PyQt6.QtCore import QRegularExpression
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMainWindow, \
    QTextEdit
from PyQt6.QtGui import QFont, QValidator, QRegularExpressionValidator


class CalcTextInputValidator(QValidator):
    def __init__(self, inputTextBox, parent=None):
        super().__init__(parent)
        self.inputTextBox = inputTextBox

    def validate(self, input_str, pos):
        # Reject if there are consecutive '+' characters
        regexValidator = re.compile(r"\d+([+]|\/|[%]|[-]|[*])")
        if regexValidator.match(input_str):
            return QValidator.State.Acceptable, input_str, pos

        return QValidator.State.Invalid, "", pos


class Calculator(QWidget):
    result: int
    temp_val = ""
    input_txt_area = None
    sub_text_area = None
    new = 0
    newValue =""

    def __init__(self):
        super().__init__()
        self.ui()

    def button_actions(self, buttonTxt):
        try:
            if buttonTxt in "0123456789*+-/%.":
                self.temp_val += buttonTxt
                self.input_txt_area.setText(self.temp_val)

                # if len(newValue) > 1 and newValue[-1] not in "*+-/%":
                #    self.result = eval(newValue)
                #    self.input_txt_area.setText(f"{self.result}")
                #    self.sub_text_area.setText(f"{newValue}")
                # elif (len(newValue) == 1 and newValue in "*+-/%") or (
                #        len(newValue) > 2 and newValue[-2] in "*+-/%" and newValue[-1] in "*+-/%"):
                #    self.input_txt_area.setText(newValue[:-1])
                # else:
                #    self.input_txt_area.setText(newValue)
                # if len(newValue) == 2:
                #     if self.temp_val[-1] in "*+-/%":
                #         pass

            if buttonTxt == "C":
                self.new = 0
                self.newValue = ""
                self.temp_val = ""
                self.input_txt_area.clear()
                self.sub_text_area.clear()
            if buttonTxt == "=":
                try:
                    if len(self.temp_val) > 1 and self.temp_val[-1] in "*+-/%":
                        self.input_txt_area.setText(self.temp_val[:-1])
                    self.newValue = self.input_txt_area.text()
                    self.result = eval(self.newValue)
                    self.sub_text_area.setText(f"{self.newValue}")
                    self.temp_val = str(self.result)
                    self.input_txt_area.setText(self.temp_val)
                    if len(self.temp_val) != 0:
                        self.new += self.result
                        self.input_txt_area.setText(str(f"{self.new}"))
                except Exception as f:
                    self.input_txt_area.setText("ERROR")
                    print("Error:", f)
            if buttonTxt == "CE":
                self.new = 0
                self.newValue = ""
                self.temp_val = ""
                self.input_txt_area.clear()
                self.sub_text_area.clear()
        except Exception as e:
            traceback.print_exception(e)

    def ui(self):

        self.setWindowTitle("Calculator")
        self.buttons = [("7", "8", "9", "/"),
                        ("4", "5", "6", "*"),
                        ("1", "2", "3", "-"),
                        ("0", ".", "=", "+"),
                        ("C", "CE", "%")
                        ]
        layoutv = QVBoxLayout(self)
        self.input_txt_area = QLineEdit(self)
        self.sub_text_area = QLineEdit(self)
        layoutv.addWidget(self.sub_text_area)
        layoutv.addWidget(self.input_txt_area)
        self.fontstyle = QFont()
        self.fontstyle.setPointSize(17)
        for button_r in self.buttons:
            layoutH = QHBoxLayout(self)
            for buttonTxt in button_r:
                button = QPushButton(buttonTxt, self)
                layoutH.addWidget(button)
                button.clicked.connect(lambda _, text=buttonTxt: self.button_actions(text))
                button.setFixedSize(110, 60)
                button.setFont(self.fontstyle)
            layoutv.addLayout(layoutH)

        self.setLayout(layoutv)
        self.input_txt_area.setReadOnly(True)
        self.sub_text_area.setReadOnly(True)
        self.input_txt_area.setFixedHeight(60)
        self.font = self.input_txt_area.setFont(self.fontstyle)
        q_validator = CalcTextInputValidator(
            self.input_txt_area)  # QRegularExpressionValidator(QRegularExpression(r"(\d+[+]|\/|%|-|[*]\d+)"))
        # self.input_txt_area.setValidator(q_validator)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Calculator()
    widget.resize(500, 500)
    widget.show()
    sys.exit(app.exec())
