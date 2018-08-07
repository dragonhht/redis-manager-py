#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit
from PyQt5.QtGui import QFont

'''
弹出的各类窗体
'''

class TTL(QWidget):

    def __init__(self, key):
        super().__init__()
        self.key = key
        self.setFixedSize(400, 200)
        self.init_UI()
        
    def init_UI(self):
        '''
        初始化UI
        '''
        self.setFont(QFont('SansSerif', 10))
        QLabel('TTL: ', self).move(20, 50)
        val_input = QLineEdit(self)
        val_input.move(110, 45)
        val_input.setFixedWidth(200)
        val_input.setFixedHeight(25)
        self.show()

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