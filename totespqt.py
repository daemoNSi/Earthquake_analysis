# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import QSize
# import sys
#
# class MyWindow(QMainWindow):
#
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.setWindowTitle('Test')
#         self.setFixedSize(QSize(400,400))
#         self.staff()
#
#     def staff(self):
#         self.label = QtWidgets.QLabel(self)
#         self.label.setText('text')
#         self.label.move(3,50)
#         self.button = QtWidgets.QPushButton(self)
#         self.button.setText('click')
#         self.button.clicked.connect(self.clicked)
#
#     def clicked(self):
#         self.label.setText('changed to fit the thing')
#         self.updated()
#
#     def updated(self):
#         self.label.adjustSize()
#
#
# app = QApplication(sys.argv)
# win = MyWindow()
#
# win.show()
# sys.exit(app.exec_())