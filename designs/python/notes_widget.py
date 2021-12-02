# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_notes_tab(object):
    def setupUi(self, notes_tab):
        notes_tab.setObjectName("notes_tab")
        notes_tab.resize(430, 314)
        notes_tab.setMinimumSize(QtCore.QSize(400, 0))
        notes_tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        notes_tab.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(notes_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hbox_notes = QtWidgets.QHBoxLayout()
        self.hbox_notes.setSpacing(6)
        self.hbox_notes.setObjectName("hbox_notes")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_notes.addItem(spacerItem)
        self.btn_note = QtWidgets.QPushButton(notes_tab)
        self.btn_note.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_note.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_note.setObjectName("btn_note")
        self.hbox_notes.addWidget(self.btn_note)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_notes.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.hbox_notes)
        self.gbox_note_container = QtWidgets.QGridLayout()
        self.gbox_note_container.setObjectName("gbox_note_container")
        self.verticalLayout_2.addLayout(self.gbox_note_container)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(notes_tab)
        QtCore.QMetaObject.connectSlotsByName(notes_tab)

    def retranslateUi(self, notes_tab):
        _translate = QtCore.QCoreApplication.translate
        notes_tab.setWindowTitle(_translate("notes_tab", "Form"))
        self.btn_note.setText(_translate("notes_tab", "Add Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notes_tab = QtWidgets.QWidget()
    ui = Ui_notes_tab()
    ui.setupUi(notes_tab)
    notes_tab.show()
    sys.exit(app.exec_())
