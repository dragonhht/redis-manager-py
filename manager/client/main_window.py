#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class ManagerWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        '''
        初始化UI
        '''
        self.resize(500, 300)
        self.center()
        self.setWindowTitle("Redis Manager")
        #设置icon
        # w.setWindowIcon(QIcon('./icon/redis.png'))
        self.show()

    def closeEvent(self, event):
        '''
        关闭窗口提示
        '''
        replay = QMessageBox.question(self, '提示', '确定退出！！！', QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if replay == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        '''
        将窗口放在屏幕中
        '''
        # 获得这个QT组件的框架位置
        qr = self.frameGeometry()
        # 找到屏幕的中心
        cp = QDesktopWidget().availableGeometry().center()
        # 将这个矩形的中心放在当前这个屏幕的中心
        qr.moveCenter(cp)
        # 将创建的窗口移动
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ManagerWindow()
    sys.exit(app.exec_())
