#!/usr/bin/python
# -*- coding: UTF-8 -*- 

from PyQt5.QtWidgets import QApplication, QWidget
import sys

def main():
    # 创建应用
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    w.resize(500, 150)
    w.move(100, 100)
    w.setWindowTitle("Redis Manager")
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()