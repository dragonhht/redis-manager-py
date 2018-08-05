#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class ManagerWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        '''
        初始化UI
        '''
        self.init_menubar()
        self.init_UI_body()
        self.resize(1000, 700)
        self.center()
        self.setWindowTitle("Redis Manager")

        self.set_statusbar('ready')

        #设置icon
        # self.setWindowIcon(QIcon('./icon/redis.png'))
        self.show()

    def init_UI_body(self):
        '''
        初始化窗体内容
        '''
        # 使用网格布局
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)

        layout.addWidget(self.get_show_tree())

        frame = QFrame()
    
        layout.addWidget(frame)

        self.setCentralWidget(widget)

    def get_show_tree(self):
        '''
        设置左侧树
        '''
        tree = QTreeWidget()
        tree.setColumnCount(1)
        tree.setHeaderLabel('数据库')
        tree.setMaximumWidth(200)
        root = QTreeWidgetItem(tree)
        root.setText(0, '连接-1')
        for i in range(10):
            item = QTreeWidgetItem(root)
            item.setText(0, str(i))
            root.addChild(item)

        return tree

    def init_menubar(self):
        '''
        初始化菜单栏
        '''
        menubar = self.menuBar()

        menu = menubar.addMenu('&连接')
        createConnAct = QAction('&新建连接', self)
        createConnAct.setToolTip('新建连接')
        createConnAct.setShortcut('Ctrl+N')

        menu.addAction(createConnAct)
        delConnAct = QAction('&删除连接', self)
        delConnAct.setToolTip('删除连接')
        delConnAct.setShortcut('Ctrl+D')
        menu.addAction(delConnAct)

        exitAct = QAction('&退出',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setToolTip("退出客户端")
        exitAct.triggered.connect(self.close)
        menu.addAction(exitAct)

    def set_statusbar(self, msg):
        '''
        设置状态栏
        '''
        self.statusBar().showMessage(msg)

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
