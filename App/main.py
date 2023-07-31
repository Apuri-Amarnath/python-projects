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
                         ("C", "CE")
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
        self.input_txt_area.setFont(self.fontstyle)

    def Action(self):
        self.button = self.sender()
        if self.button:
            self.button_text = self.button.text()
            self.input_txt_area.setText(self.button_text)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        widget = Calculator()
        widget.resize(500,500)
        widget.show()
        sys.exit(app.exec())