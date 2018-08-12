#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QDesktopWidget, QDialog
from PyQt5.QtGui import QFont

'''
弹出的各类窗体
'''

class TTL(QDialog):

    def __init__(self, key, title, redis):
        super().__init__()
        self.key = key
        self.title = title
        self.setFixedSize(400, 130)
        self.val_input = QLineEdit()
        self.redis = redis
        self.init_UI()
        
    def init_UI(self):
        '''
        初始化UI
        '''
        self.init_UI_compont()
        self.center()
        self.setWindowTitle('设置' + self.title)
        self.show()

    def init_UI_compont(self):
        '''
        初始化窗体组件
        '''
        self.setFont(QFont('SansSerif', 10))
        widget = QWidget()
        layout = QVBoxLayout(self)

        input_hbox = QHBoxLayout()
        label = QLabel(self.title + ': ')
        
        self.val_input.setFixedWidth(200)
        self.val_input.setFixedHeight(25)
        input_hbox.addStretch(1)
        input_hbox.addWidget(label)
        input_hbox.addWidget(self.val_input)
        input_hbox.addStretch(1)

        hbox = QHBoxLayout()
        ok_btn = QPushButton()
        ok_btn.setText('确认')
        ok_btn.setFixedWidth(50)
        ok_btn.clicked.connect(self.click_ok)
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
    
    def click_ok(self):
        '''
        确认按钮事件
        '''
        print(self.title)
        if (self.title == 'TTL'):
            self.set_ttl()
        if (self.title == 'value'):
            print('正在设置Value')
        self.close()

    def set_ttl(self):
        '''
        设置TTL
        '''
        val = self.val_input.text()
        try:
            val = int(val)
            self.redis.set_key_ttl(self.key, val)
        except ValueError as err:
            print('please input int')

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
