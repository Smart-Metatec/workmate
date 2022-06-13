# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './xml/vault_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Vault_tab(object):
    def setupUi(self, Vault_tab):
        Vault_tab.setObjectName("Vault_tab")
        Vault_tab.resize(640, 382)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Vault_tab.sizePolicy().hasHeightForWidth())
        Vault_tab.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Vault_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hbox_controls = QtWidgets.QHBoxLayout()
        self.hbox_controls.setObjectName("hbox_controls")
        self.chk_edit = QtWidgets.QCheckBox(Vault_tab)
        self.chk_edit.setObjectName("chk_edit")
        self.hbox_controls.addWidget(self.chk_edit)
        self.chk_delete = QtWidgets.QCheckBox(Vault_tab)
        self.chk_delete.setObjectName("chk_delete")
        self.hbox_controls.addWidget(self.chk_delete)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_controls.addItem(spacerItem)
        self.btn_add = QtWidgets.QPushButton(Vault_tab)
        self.btn_add.setObjectName("btn_add")
        self.hbox_controls.addWidget(self.btn_add)
        self.btn_login = QtWidgets.QPushButton(Vault_tab)
        self.btn_login.setObjectName("btn_login")
        self.hbox_controls.addWidget(self.btn_login)
        self.verticalLayout.addLayout(self.hbox_controls)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_app_vault = QtWidgets.QLabel(Vault_tab)
        self.lbl_app_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_app_vault.setObjectName("lbl_app_vault")
        self.verticalLayout_2.addWidget(self.lbl_app_vault)
        self.vbox_app_vault = QtWidgets.QVBoxLayout()
        self.vbox_app_vault.setObjectName("vbox_app_vault")
        self.verticalLayout_2.addLayout(self.vbox_app_vault)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame = QtWidgets.QFrame(Vault_tab)
        self.frame.setMinimumSize(QtCore.QSize(3, 0))
        self.frame.setStyleSheet("background-color: #9ecd16;")
        self.frame.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_crypto_vault = QtWidgets.QLabel(Vault_tab)
        self.lbl_crypto_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_crypto_vault.setObjectName("lbl_crypto_vault")
        self.verticalLayout_3.addWidget(self.lbl_crypto_vault)
        self.vbox_crypto_vault = QtWidgets.QVBoxLayout()
        self.vbox_crypto_vault.setObjectName("vbox_crypto_vault")
        self.verticalLayout_3.addLayout(self.vbox_crypto_vault)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.frame_2 = QtWidgets.QFrame(Vault_tab)
        self.frame_2.setMinimumSize(QtCore.QSize(3, 0))
        self.frame_2.setStyleSheet("background-color: #9ecd16;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_general_vault = QtWidgets.QLabel(Vault_tab)
        self.lbl_general_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_general_vault.setObjectName("lbl_general_vault")
        self.verticalLayout_4.addWidget(self.lbl_general_vault)
        self.vbox_general_vault = QtWidgets.QVBoxLayout()
        self.vbox_general_vault.setObjectName("vbox_general_vault")
        self.verticalLayout_4.addLayout(self.vbox_general_vault)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Vault_tab)
        QtCore.QMetaObject.connectSlotsByName(Vault_tab)

    def retranslateUi(self, Vault_tab):
        _translate = QtCore.QCoreApplication.translate
        Vault_tab.setWindowTitle(_translate("Vault_tab", "Form"))
        self.chk_edit.setText(_translate("Vault_tab", "Edit Secret"))
        self.chk_delete.setText(_translate("Vault_tab", "Delete Secret"))
        self.btn_add.setText(_translate("Vault_tab", "Add Secret"))
        self.btn_login.setText(_translate("Vault_tab", "Login"))
        self.lbl_app_vault.setText(_translate("Vault_tab", "App Vault"))
        self.lbl_crypto_vault.setText(_translate("Vault_tab", "Crypto Vault"))
        self.lbl_general_vault.setText(_translate("Vault_tab", "General Vault"))
