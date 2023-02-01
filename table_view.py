from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='earthquake_analysis',
    autocommit=True
)

mycursor = db.cursor(buffered=True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, column_name, row_name, table_name):
        self.table_name = table_name
        self.max_column = len(column_name)
        self.max_row = row_name
        width = self.max_column*106
        height = self.max_row*32

        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        if width <= 1920 and height <= 1080:
            MainWindow.resize(width, height)
            self.tableWidget.setGeometry(QtCore.QRect(0, 0, self.max_row*57, self.max_column*57))
        else:
            MainWindow.resize(1920, 1080)
            self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(self.max_column)
        self.tableWidget.setRowCount(self.max_row)
        self.tableWidget.setHorizontalHeaderLabels(column_name)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        column = 0
        row = 0
        mycursor.execute(f'select * from {self.table_name}')
        for values in mycursor:
            for item in values:
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
                if column == self.max_column:
                    column = 0
                    row += 1


# if __name__ == "__main__":
def create_table(column_name, row_name, table_name):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, column_name, row_name, table_name)
    MainWindow.show()
    sys.exit(app.exec_())
