# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minidsp.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mergeMinidspDialog(object):
    def setupUi(self, mergeMinidspDialog):
        mergeMinidspDialog.setObjectName("mergeMinidspDialog")
        mergeMinidspDialog.resize(826, 436)
        self.gridLayout = QtWidgets.QGridLayout(mergeMinidspDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(mergeMinidspDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.innerLayout = QtWidgets.QGridLayout()
        self.innerLayout.setObjectName("innerLayout")
        self.totalFiles = QtWidgets.QSpinBox(mergeMinidspDialog)
        self.totalFiles.setReadOnly(True)
        self.totalFiles.setMaximum(10000)
        self.totalFiles.setObjectName("totalFiles")
        self.innerLayout.addWidget(self.totalFiles, 5, 3, 1, 1)
        self.filesProcessed = QtWidgets.QSpinBox(mergeMinidspDialog)
        self.filesProcessed.setReadOnly(True)
        self.filesProcessed.setMaximum(100000)
        self.filesProcessed.setObjectName("filesProcessed")
        self.innerLayout.addWidget(self.filesProcessed, 5, 1, 1, 1)
        self.processFiles = QtWidgets.QToolButton(mergeMinidspDialog)
        self.processFiles.setObjectName("processFiles")
        self.innerLayout.addWidget(self.processFiles, 5, 5, 1, 1)
        self.errors = QtWidgets.QListWidget(mergeMinidspDialog)
        self.errors.setObjectName("errors")
        self.innerLayout.addWidget(self.errors, 6, 1, 1, 4)
        self.configFile = QtWidgets.QLineEdit(mergeMinidspDialog)
        self.configFile.setReadOnly(True)
        self.configFile.setObjectName("configFile")
        self.innerLayout.addWidget(self.configFile, 2, 1, 1, 4)
        self.minidspType = QtWidgets.QComboBox(mergeMinidspDialog)
        self.minidspType.setObjectName("minidspType")
        self.minidspType.addItem("")
        self.minidspType.addItem("")
        self.innerLayout.addWidget(self.minidspType, 4, 1, 1, 4)
        self.configFileLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.configFileLabel.setObjectName("configFileLabel")
        self.innerLayout.addWidget(self.configFileLabel, 2, 0, 1, 1)
        self.configFilePicker = QtWidgets.QToolButton(mergeMinidspDialog)
        self.configFilePicker.setObjectName("configFilePicker")
        self.innerLayout.addWidget(self.configFilePicker, 2, 5, 1, 1)
        self.outputDirectoryLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.outputDirectoryLabel.setObjectName("outputDirectoryLabel")
        self.innerLayout.addWidget(self.outputDirectoryLabel, 3, 0, 1, 1)
        self.outputDirectoryPicker = QtWidgets.QToolButton(mergeMinidspDialog)
        self.outputDirectoryPicker.setObjectName("outputDirectoryPicker")
        self.innerLayout.addWidget(self.outputDirectoryPicker, 3, 5, 1, 1)
        self.outputDirectory = QtWidgets.QLineEdit(mergeMinidspDialog)
        self.outputDirectory.setReadOnly(True)
        self.outputDirectory.setObjectName("outputDirectory")
        self.innerLayout.addWidget(self.outputDirectory, 3, 1, 1, 4)
        self.lastUpdateLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.innerLayout.addWidget(self.lastUpdateLabel, 0, 0, 1, 1)
        self.ofLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.ofLabel.setObjectName("ofLabel")
        self.innerLayout.addWidget(self.ofLabel, 5, 2, 1, 1)
        self.errorsLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.errorsLabel.setObjectName("errorsLabel")
        self.innerLayout.addWidget(self.errorsLabel, 6, 0, 1, 1)
        self.filesProcessedLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.filesProcessedLabel.setObjectName("filesProcessedLabel")
        self.innerLayout.addWidget(self.filesProcessedLabel, 5, 0, 1, 1)
        self.lastCommitDate = QtWidgets.QDateTimeEdit(mergeMinidspDialog)
        self.lastCommitDate.setReadOnly(True)
        self.lastCommitDate.setObjectName("lastCommitDate")
        self.innerLayout.addWidget(self.lastCommitDate, 0, 1, 1, 3)
        self.minidspTypeLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.minidspTypeLabel.setObjectName("minidspTypeLabel")
        self.innerLayout.addWidget(self.minidspTypeLabel, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.innerLayout.addItem(spacerItem, 5, 4, 1, 1)
        self.infoLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.innerLayout.addWidget(self.infoLabel, 0, 4, 1, 1)
        self.refreshGitRepo = QtWidgets.QToolButton(mergeMinidspDialog)
        self.refreshGitRepo.setObjectName("refreshGitRepo")
        self.innerLayout.addWidget(self.refreshGitRepo, 0, 5, 1, 1)
        self.lastCommitMessage = QtWidgets.QPlainTextEdit(mergeMinidspDialog)
        self.lastCommitMessage.setObjectName("lastCommitMessage")
        self.innerLayout.addWidget(self.lastCommitMessage, 1, 1, 1, 4)
        self.innerLayout.setRowStretch(1, 1)
        self.innerLayout.setRowStretch(6, 1)
        self.gridLayout.addLayout(self.innerLayout, 0, 0, 1, 1)

        self.retranslateUi(mergeMinidspDialog)
        self.buttonBox.accepted.connect(mergeMinidspDialog.accept)
        self.buttonBox.rejected.connect(mergeMinidspDialog.reject)
        self.configFilePicker.clicked.connect(mergeMinidspDialog.pick_config_file)
        self.outputDirectoryPicker.clicked.connect(mergeMinidspDialog.pick_output_dir)
        self.processFiles.clicked.connect(mergeMinidspDialog.process_files)
        self.refreshGitRepo.clicked.connect(mergeMinidspDialog.refresh_repo)
        QtCore.QMetaObject.connectSlotsByName(mergeMinidspDialog)

    def retranslateUi(self, mergeMinidspDialog):
        _translate = QtCore.QCoreApplication.translate
        mergeMinidspDialog.setWindowTitle(_translate("mergeMinidspDialog", "Merge Minidsp Config"))
        self.processFiles.setText(_translate("mergeMinidspDialog", "..."))
        self.minidspType.setItemText(0, _translate("mergeMinidspDialog", "2x4 HD"))
        self.minidspType.setItemText(1, _translate("mergeMinidspDialog", "2x4"))
        self.configFileLabel.setText(_translate("mergeMinidspDialog", "Config File"))
        self.configFilePicker.setText(_translate("mergeMinidspDialog", "..."))
        self.outputDirectoryLabel.setText(_translate("mergeMinidspDialog", "Output Directory"))
        self.outputDirectoryPicker.setText(_translate("mergeMinidspDialog", "..."))
        self.lastUpdateLabel.setText(_translate("mergeMinidspDialog", "Last Update"))
        self.ofLabel.setText(_translate("mergeMinidspDialog", "of"))
        self.errorsLabel.setText(_translate("mergeMinidspDialog", "Errors"))
        self.filesProcessedLabel.setText(_translate("mergeMinidspDialog", "Files Processed"))
        self.minidspTypeLabel.setText(_translate("mergeMinidspDialog", "Minidsp Type"))
        self.refreshGitRepo.setText(_translate("mergeMinidspDialog", "..."))


