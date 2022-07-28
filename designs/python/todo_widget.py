# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/todo_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_todo_tab(object):
    def setupUi(self, todo_tab):
        todo_tab.setObjectName("todo_tab")
        todo_tab.resize(573, 332)
        todo_tab.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(todo_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_todo = QtWidgets.QPushButton(todo_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_todo.sizePolicy().hasHeightForWidth())
        self.btn_add_todo.setSizePolicy(sizePolicy)
        self.btn_add_todo.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_add_todo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_add_todo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_todo.setObjectName("btn_add_todo")
        self.horizontalLayout.addWidget(self.btn_add_todo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.todo_container = QtWidgets.QGridLayout()
        self.todo_container.setObjectName("todo_container")
        self.verticalLayout_2.addLayout(self.todo_container)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(todo_tab)
        QtCore.QMetaObject.connectSlotsByName(todo_tab)

    def retranslateUi(self, todo_tab):
        _translate = QtCore.QCoreApplication.translate
        todo_tab.setWindowTitle(_translate("todo_tab", "Form"))
        self.btn_add_todo.setText(_translate("todo_tab", "Add To-do"))
