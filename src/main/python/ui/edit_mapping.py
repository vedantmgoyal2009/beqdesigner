# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_mapping.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editMappingDialog(object):
    def setupUi(self, editMappingDialog):
        editMappingDialog.setObjectName("editMappingDialog")
        editMappingDialog.resize(415, 347)
        self.gridLayout = QtWidgets.QGridLayout(editMappingDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.channelLabel = QtWidgets.QLabel(editMappingDialog)
        self.channelLabel.setObjectName("channelLabel")
        self.gridLayout.addWidget(self.channelLabel, 0, 0, 1, 1)
        self.channels = QtWidgets.QListWidget(editMappingDialog)
        self.channels.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.channels.setObjectName("channels")
        self.gridLayout.addWidget(self.channels, 0, 1, 1, 1)
        self.signalLabel = QtWidgets.QLabel(editMappingDialog)
        self.signalLabel.setObjectName("signalLabel")
        self.gridLayout.addWidget(self.signalLabel, 1, 0, 1, 1)
        self.signal = QtWidgets.QComboBox(editMappingDialog)
        self.signal.setObjectName("signal")
        self.gridLayout.addWidget(self.signal, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(editMappingDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(editMappingDialog)
        self.buttonBox.accepted.connect(editMappingDialog.accept)
        self.buttonBox.rejected.connect(editMappingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(editMappingDialog)

    def retranslateUi(self, editMappingDialog):
        _translate = QtCore.QCoreApplication.translate
        editMappingDialog.setWindowTitle(_translate("editMappingDialog", "Edit Mapping"))
        self.channelLabel.setText(_translate("editMappingDialog", "Channels"))
        self.signalLabel.setText(_translate("editMappingDialog", "Signal"))
