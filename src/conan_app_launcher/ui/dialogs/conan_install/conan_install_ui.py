# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\repos\app_grid_conan\src\conan_app_launcher\ui\dialogs\conan_install\conan_install.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(274, 116)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(200, 100))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.install_icon = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.install_icon.sizePolicy().hasHeightForWidth())
        self.install_icon.setSizePolicy(sizePolicy)
        self.install_icon.setMinimumSize(QtCore.QSize(30, 0))
        self.install_icon.setMaximumSize(QtCore.QSize(30, 16777215))
        self.install_icon.setObjectName("install_icon")
        self.horizontalLayout.addWidget(self.install_icon)
        self.conan_ref_line_edit = ConanRefLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conan_ref_line_edit.sizePolicy().hasHeightForWidth())
        self.conan_ref_line_edit.setSizePolicy(sizePolicy)
        self.conan_ref_line_edit.setMinimumSize(QtCore.QSize(0, 0))
        self.conan_ref_line_edit.setMaximumSize(QtCore.QSize(1024, 16777215))
        self.conan_ref_line_edit.setText("")
        self.conan_ref_line_edit.setMaxLength(1024)
        self.conan_ref_line_edit.setFrame(True)
        self.conan_ref_line_edit.setObjectName("conan_ref_line_edit")
        self.horizontalLayout.addWidget(self.conan_ref_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.auto_install_check_box = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_install_check_box.sizePolicy().hasHeightForWidth())
        self.auto_install_check_box.setSizePolicy(sizePolicy)
        self.auto_install_check_box.setObjectName("auto_install_check_box")
        self.verticalLayout.addWidget(self.auto_install_check_box)
        self.update_check_box = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_check_box.sizePolicy().hasHeightForWidth())
        self.update_check_box.setSizePolicy(sizePolicy)
        self.update_check_box.setObjectName("update_check_box")
        self.verticalLayout.addWidget(self.update_check_box)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept) # type: ignore
        self.button_box.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Conan Install"))
        self.install_icon.setText(_translate("Dialog", "Icon"))
        self.auto_install_check_box.setText(_translate("Dialog", "Automatically determine best matching package"))
        self.update_check_box.setText(_translate("Dialog", "Update (-u)"))
from conan_app_launcher.ui.widgets.conan_line_edit import ConanRefLineEdit