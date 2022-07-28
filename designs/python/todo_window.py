# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/todo_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_todo_edit(object):
    def setupUi(self, todo_edit):
        todo_edit.setObjectName("todo_edit")
        todo_edit.resize(593, 407)
        self.verticalLayout = QtWidgets.QVBoxLayout(todo_edit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_name = QtWidgets.QLabel(todo_edit)
        self.lbl_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout_3.addWidget(self.lbl_name)
        self.lnedt_name = QtWidgets.QLineEdit(todo_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lnedt_name.sizePolicy().hasHeightForWidth())
        self.lnedt_name.setSizePolicy(sizePolicy)
        self.lnedt_name.setObjectName("lnedt_name")
        self.verticalLayout_3.addWidget(self.lnedt_name)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_date = QtWidgets.QLabel(todo_edit)
        self.lbl_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout_4.addWidget(self.lbl_date)
        self.dtedt_date = QtWidgets.QDateEdit(todo_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtedt_date.sizePolicy().hasHeightForWidth())
        self.dtedt_date.setSizePolicy(sizePolicy)
        self.dtedt_date.setMinimumSize(QtCore.QSize(0, 0))
        self.dtedt_date.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dtedt_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dtedt_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dtedt_date.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dtedt_date.setCalendarPopup(True)
        self.dtedt_date.setObjectName("dtedt_date")
        self.verticalLayout_4.addWidget(self.dtedt_date)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lbl_status = QtWidgets.QLabel(todo_edit)
        self.lbl_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.verticalLayout_5.addWidget(self.lbl_status)
        self.cmbx_status = QtWidgets.QComboBox(todo_edit)
        self.cmbx_status.setObjectName("cmbx_status")
        self.cmbx_status.addItem("")
        self.cmbx_status.addItem("")
        self.verticalLayout_5.addWidget(self.cmbx_status)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_description = QtWidgets.QLabel(todo_edit)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout_6.addWidget(self.lbl_description)
        self.txe_description = QtWidgets.QTextEdit(todo_edit)
        self.txe_description.setObjectName("txe_description")
        self.verticalLayout_6.addWidget(self.txe_description)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_save = QtWidgets.QPushButton(todo_edit)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.btn_delete = QtWidgets.QPushButton(todo_edit)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_3.addWidget(self.btn_delete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(todo_edit)
        QtCore.QMetaObject.connectSlotsByName(todo_edit)

    def retranslateUi(self, todo_edit):
        _translate = QtCore.QCoreApplication.translate
        todo_edit.setWindowTitle(_translate("todo_edit", "Edit Todo"))
        self.lbl_name.setText(_translate("todo_edit", "Name"))
        self.lbl_date.setText(_translate("todo_edit", "Date"))
        self.lbl_status.setText(_translate("todo_edit", "Status"))
        self.cmbx_status.setItemText(0, _translate("todo_edit", "Incomplete"))
        self.cmbx_status.setItemText(1, _translate("todo_edit", "Complete"))
        self.lbl_description.setText(_translate("todo_edit", "Description"))
        self.btn_save.setText(_translate("todo_edit", "Save"))
        self.btn_delete.setText(_translate("todo_edit", "Discard"))
