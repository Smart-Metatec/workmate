# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/todo_edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_todo_edit(object):
    def setupUi(self, todo_edit):
        todo_edit.setObjectName("todo_edit")
        todo_edit.resize(593, 90)
        self.verticalLayout = QtWidgets.QVBoxLayout(todo_edit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_date = QtWidgets.QLabel(todo_edit)
        self.lbl_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_date.setObjectName("lbl_date")
        self.gridLayout.addWidget(self.lbl_date, 0, 1, 1, 1)
        self.lbl_status = QtWidgets.QLabel(todo_edit)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.gridLayout.addWidget(self.lbl_status, 0, 2, 1, 1)
        self.lbl_name = QtWidgets.QLabel(todo_edit)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.lnedt_name = QtWidgets.QLineEdit(todo_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedt_name.sizePolicy().hasHeightForWidth())
        self.lnedt_name.setSizePolicy(sizePolicy)
        self.lnedt_name.setObjectName("lnedt_name")
        self.gridLayout.addWidget(self.lnedt_name, 1, 0, 1, 1)
        self.dtedt_date = QtWidgets.QDateEdit(todo_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtedt_date.sizePolicy().hasHeightForWidth())
        self.dtedt_date.setSizePolicy(sizePolicy)
        self.dtedt_date.setMinimumSize(QtCore.QSize(150, 0))
        self.dtedt_date.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dtedt_date.setAlignment(QtCore.Qt.AlignCenter)
        self.dtedt_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dtedt_date.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dtedt_date.setCalendarPopup(True)
        self.dtedt_date.setObjectName("dtedt_date")
        self.gridLayout.addWidget(self.dtedt_date, 1, 1, 1, 1)
        self.cmbx_status = QtWidgets.QComboBox(todo_edit)
        self.cmbx_status.setObjectName("cmbx_status")
        self.cmbx_status.addItem("")
        self.cmbx_status.addItem("")
        self.gridLayout.addWidget(self.cmbx_status, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_save = QtWidgets.QPushButton(todo_edit)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(todo_edit)
        QtCore.QMetaObject.connectSlotsByName(todo_edit)

    def retranslateUi(self, todo_edit):
        _translate = QtCore.QCoreApplication.translate
        todo_edit.setWindowTitle(_translate("todo_edit", "Edit Todo"))
        self.lbl_date.setText(_translate("todo_edit", "Date"))
        self.lbl_status.setText(_translate("todo_edit", "Status"))
        self.lbl_name.setText(_translate("todo_edit", "Name"))
        self.cmbx_status.setItemText(0, _translate("todo_edit", "Incomplete"))
        self.cmbx_status.setItemText(1, _translate("todo_edit", "Complete"))
        self.btn_save.setText(_translate("todo_edit", "Save"))
