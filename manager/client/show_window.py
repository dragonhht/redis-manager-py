#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QDesktopWidget, QDialog
from PyQt5.QtGui import QFont

'''
弹出的各类窗体
'''

class TTL(QDialog):

    def __init__(self, key):
        super().__init__()
        self.key = key
        self.setFixedSize(400, 130)
        self.init_UI()
        
    def init_UI(self):
        '''
        初始化UI
        '''
        self.init_UI_compont()
        self.center()
        self.setWindowTitle('设置TTL')
        self.show()

    def init_UI_compont(self):
        '''
        初始化窗体组件
        '''
        self.setFont(QFont('SansSerif', 10))
        widget = QWidget()
        layout = QVBoxLayout(self)

        input_hbox = QHBoxLayout()
        label = QLabel('TTL: ')
        val_input = QLineEdit()
        val_input.setFixedWidth(200)
        val_input.setFixedHeight(25)
        input_hbox.addStretch(1)
        input_hbox.addWidget(label)
        input_hbox.addWidget(val_input)
        input_hbox.addStretch(1)

        hbox = QHBoxLayout()
        ok_btn = QPushButton()
        ok_btn.setText('确认')
        ok_btn.setFixedWidth(50)
        cancle_btn = QPushButton()
        cancle_btn.setText('取消')
        cancle_btn.setFixedWidth(50)
        cancle_btn.clicked.connect(self.close)
        hbox.addStretch(1)
        hbox.addWidget(ok_btn)
        hbox.addWidget(cancle_btn)
        
        layout.addLayout(input_hbox)
        layout.addLayout(hbox)

        # self.setCentralWidget(widget)

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

def show_TTL_win(key):
    '''
    显示TTL设置窗体
    '''
    app = QApplication(sys.argv)
    win = TTL(key)
    sys.exit(app.exec_())

def main():
    show_TTL_win('test')
 
if __name__ == '__main__':
     main()