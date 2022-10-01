import os
import sys
from PyQt5.QtWidgets import (
    QPushButton, QApplication,QMessageBox,QDesktopWidget,QMainWindow)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(background.png)}")

        btn1 = QPushButton('设置翻译区域', self)  # 按钮
        btn1.resize(100,50)
        btn1.move(700, 100)
        btn1.clicked.connect(self.buttonClicked)

        btn2 = QPushButton('开始翻译', self)  # 按钮
        btn2.resize(100, 50)
        btn2.move(700, 300)
        btn2.clicked.connect(self.buttonClicked)

        self.resize(942, 659)
        self.center()
        self.setWindowTitle('清雨翻译器')
        self.setWindowIcon(QIcon('qq.jpg'))
        self.show()

    def center(self):  # 窗口居中

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):#关闭窗口时提示
        reply = QMessageBox.question(self, 'Message',
                                     "您确定要关闭吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == '设置翻译区域':
            self.hide()
            os.system('python 设置翻译区域.py')
            self.show()
        if sender.text() == '开始翻译':
            os.system("python 图片展示.py")


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())#窗口退出


if __name__ == '__main__':
    main()