import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow, QFileSystemModel, QTableWidget,QTreeWidget,QTreeView,QMenu
from PyQt5 import QtCore
from PyQt5 import QtGui


class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.getdata()
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.contextMenu)


    def init_ui(self):
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layoutV = QVBoxLayout(self)
        layoutH = QHBoxLayout(main_widget)

        widget_left = QWidget()
        widget_right = QWidget()
        #left - right
        layoutH.addWidget(widget_left, 30)
        layoutH.addWidget(widget_right, 70)

        widget_left.setFixedHeight(800)
        widget_right.setFixedHeight(800)

        #widget_right.setStyleSheet("background-color: red;")
        #right Header
        layoutH = QHBoxLayout(widget_right)
        Header = QTableWidget(0, 4)
        Header.setHorizontalHeaderLabels(["Name", "Date Modified", "Type", "Size"])
        layoutH.addWidget(Header)

        #Left - tree
        self.tree = QTreeView(widget_left)
        layoutV.addWidget(self.tree)
        self.tree.setFixedHeight(800)
        self.tree.setHeaderHidden(True)
        #context menu

        #Right - tree

    def contextMenu(self,pos):
        menu = QMenu()
        open =  menu.addAction("Open")
        opennew =  menu.addAction("Open in a new window")
        open.triggered.connect(self.openfile)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
    def openfile(self):
        pass
    def opennewwindow(self):
        pass
    def getdata(self):
        path = "C:\Windows"
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.tree.setModel(self.model)
        #self.tree_right.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.resize(1000, 800)
    window.show()
    sys.exit(app.exec_())
