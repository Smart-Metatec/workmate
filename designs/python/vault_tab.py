# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vault_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Vault_tab(object):
    def setupUi(self, Vault_tab):
        Vault_tab.setObjectName("Vault_tab")
        Vault_tab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Vault_tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbl_vault = QtWidgets.QTableWidget(Vault_tab)
        self.tbl_vault.setObjectName("tbl_vault")
        self.tbl_vault.setColumnCount(0)
        self.tbl_vault.setRowCount(0)
        self.verticalLayout.addWidget(self.tbl_vault)

        self.retranslateUi(Vault_tab)
        QtCore.QMetaObject.connectSlotsByName(Vault_tab)

    def retranslateUi(self, Vault_tab):
        _translate = QtCore.QCoreApplication.translate
        Vault_tab.setWindowTitle(_translate("Vault_tab", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vault_tab = QtWidgets.QWidget()
    ui = Ui_Vault_tab()
    ui.setupUi(Vault_tab)
    Vault_tab.show()
    sys.exit(app.exec_())
