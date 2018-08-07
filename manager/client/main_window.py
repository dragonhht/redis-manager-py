#!/usr/bin/python
# -*- coding: UTF-8 -*- 

'''
主窗体
'''

import sys

from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QWidget, QTabWidget, QHBoxLayout, QFrame, QPushButton, QLabel, QLineEdit, QTextEdit, QTableWidget, QAbstractItemView, QTableWidgetItem, QTreeWidgetItem, QAction, QMessageBox, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class ManagerWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700)
        # 标签页设置
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        # 设置标签页关闭
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabel('数据库')
        self.tree.setMaximumWidth(200)

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

        # self.set_statusbar('ready')

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

        self.set_show_tree()
        for index in range(10):
            self.create_tab('str' + str(index))

        layout.addWidget(self.tree)
        layout.addWidget(self.tabs)

        self.setCentralWidget(widget)

    def create_tab(self, tab_name):
        '''
        创建标签页
        '''
        frame = QFrame() 
        
        # 设置字号
        font = QFont('SansSerif', 10)
        frame.setFont(font)
        
        self.set_show_label(frame)
        self.set_key_value(frame)
        self.set_show_btn(frame)
        self.set_show_data(frame)
        self.tabs.addTab(frame, tab_name)

    def close_tab(self, index):
        '''
        关闭标签页
        '''
        if index > -1:
            self.tabs.removeTab(index)

    def set_show_btn(self, frame):
        '''
        设置展示面板的按钮
        '''
        # 设置TTL
        ttl_btn = QPushButton('set TTL', frame)
        ttl_btn.move(200, 5)
        ttl_btn.clicked.connect(self.set_TTL_btn)
        # 刷新数据
        reload_btn = QPushButton('reload data', frame)
        reload_btn.move(300, 5)
        reload_btn.clicked.connect(self.reload_data)
        # 删除
        del_btn = QPushButton('delete', frame)
        del_btn.move(400, 5)
        del_btn.clicked.connect(self.del_data)
        # 设置值
        reset_btn = QPushButton('set value', frame)
        reset_btn.move(600, 100)
        reset_btn.clicked.connect(self.reset_data)

    def set_TTL_btn(self, key):
        '''
        设置TTL按钮的点击事件
        '''
        # TODO 设置TTL事件
        pass

    def reload_data(self, key):
        '''
        刷新面板数据
        '''
        # TODO 刷新面板数据
        pass

    def del_data(self, key):
        '''
        删除数据
        '''
        # TODO 删除数据
        pass

    def reset_data(self, key):
        '''
        设置键的值
        '''
        # TODO 设置键的值
        pass

    def set_show_label(self, frame):
        '''
        设置展示的label
        '''
        # 使用绝对定位添加label
        QLabel('type： ', frame).move(5, 10)
        QLabel('String', frame).move(40, 10)
        QLabel('TTL : ',frame).move(100, 10)
        QLabel('-1', frame).move(140, 10)
        QLabel('key： ', frame).move(5, 500)
        QLabel('value: ', frame).move(5, 540)

    def set_key_value(self, frame):
        '''
        设置键值显示框
        '''
        key_text = QLineEdit(frame)
        key_text.move(50, 495)
        key_text.setFixedWidth(500)

        val_text = QTextEdit(frame)
        val_text.move(50, 540)
        val_text.setFixedWidth(500)
        val_text.setFixedHeight(80)

    def set_show_data(self, frame):
        '''
        设置展示数据的列表
        '''
        # 展示数据的Table
        data_table = QTableWidget(10, 2, frame)
        # 设置表头
        data_table.setHorizontalHeaderLabels(['键', '值'])
        data_table.move(5, 50)
        data_table.setFixedWidth(560)
        data_table.setFixedHeight(430)
        # 禁止编辑
        data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择
        data_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置单元格宽度，参数： （单元格索引， 宽度）
        data_table.setColumnWidth(0, 267)
        data_table.setColumnWidth(1, 267)

        # 添加数据
        for col in range(2):
            for row in range(10):
                data_table.setItem(row, col, QTableWidgetItem(str(col) +' : ' + str(row)))

    def set_show_tree(self):
        '''
        设置左侧树组件
        '''
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '连接-1')
        for i in range(10):
            item = QTreeWidgetItem(root)
            item.setText(0, str(i))
            root.addChild(item)

    def init_menubar(self):
        '''
        初始化菜单栏
        '''
        menubar = self.menuBar()

        menu = menubar.addMenu('&connect')
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