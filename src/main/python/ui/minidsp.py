# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minidsp.ui',
# licensing of 'minidsp.ui' applies.
#
# Created: Sun Jun 30 22:06:42 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mergeMinidspDialog(object):
    def setupUi(self, mergeMinidspDialog):
        mergeMinidspDialog.setObjectName("mergeMinidspDialog")
        mergeMinidspDialog.resize(617, 508)
        self.gridLayout = QtWidgets.QGridLayout(mergeMinidspDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(mergeMinidspDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.innerLayout = QtWidgets.QGridLayout()
        self.innerLayout.setObjectName("innerLayout")
        self.filesProcessed = QtWidgets.QSpinBox(mergeMinidspDialog)
        self.filesProcessed.setReadOnly(True)
        self.filesProcessed.setMaximum(100000)
        self.filesProcessed.setObjectName("filesProcessed")
        self.innerLayout.addWidget(self.filesProcessed, 6, 1, 1, 1)
        self.minidspTypeLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.minidspTypeLabel.setObjectName("minidspTypeLabel")
        self.innerLayout.addWidget(self.minidspTypeLabel, 5, 0, 1, 1)
        self.processFiles = QtWidgets.QToolButton(mergeMinidspDialog)
        self.processFiles.setObjectName("processFiles")
        self.innerLayout.addWidget(self.processFiles, 6, 5, 1, 1)
        self.outputDirectoryLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.outputDirectoryLabel.setObjectName("outputDirectoryLabel")
        self.innerLayout.addWidget(self.outputDirectoryLabel, 4, 0, 1, 1)
        self.configFile = QtWidgets.QLineEdit(mergeMinidspDialog)
        self.configFile.setEnabled(False)
        self.configFile.setReadOnly(True)
        self.configFile.setObjectName("configFile")
        self.innerLayout.addWidget(self.configFile, 3, 1, 1, 4)
        self.ofLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.ofLabel.setObjectName("ofLabel")
        self.innerLayout.addWidget(self.ofLabel, 6, 2, 1, 1)
        self.infoLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.innerLayout.addWidget(self.infoLabel, 0, 4, 1, 1)
        self.userSourceDirPicker = QtWidgets.QToolButton(mergeMinidspDialog)
        self.userSourceDirPicker.setObjectName("userSourceDirPicker")
        self.innerLayout.addWidget(self.userSourceDirPicker, 2, 5, 1, 1)
        self.totalFiles = QtWidgets.QSpinBox(mergeMinidspDialog)
        self.totalFiles.setReadOnly(True)
        self.totalFiles.setMaximum(10000)
        self.totalFiles.setObjectName("totalFiles")
        self.innerLayout.addWidget(self.totalFiles, 6, 3, 1, 1)
        self.lastUpdateLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.lastUpdateLabel.setObjectName("lastUpdateLabel")
        self.innerLayout.addWidget(self.lastUpdateLabel, 0, 0, 1, 1)
        self.lastCommitMessage = QtWidgets.QPlainTextEdit(mergeMinidspDialog)
        self.lastCommitMessage.setReadOnly(True)
        self.lastCommitMessage.setObjectName("lastCommitMessage")
        self.innerLayout.addWidget(self.lastCommitMessage, 1, 1, 1, 4)
        self.outputDirectoryPicker = QtWidgets.QToolButton(mergeMinidspDialog)
        self.outputDirectoryPicker.setObjectName("outputDirectoryPicker")
        self.innerLayout.addWidget(self.outputDirectoryPicker, 4, 5, 1, 1)
        self.errorsLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.errorsLabel.setObjectName("errorsLabel")
        self.innerLayout.addWidget(self.errorsLabel, 7, 0, 1, 1)
        self.configFileLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.configFileLabel.setObjectName("configFileLabel")
        self.innerLayout.addWidget(self.configFileLabel, 3, 0, 1, 1)
        self.userSourceDirLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.userSourceDirLabel.setObjectName("userSourceDirLabel")
        self.innerLayout.addWidget(self.userSourceDirLabel, 2, 0, 1, 1)
        self.minidspType = QtWidgets.QComboBox(mergeMinidspDialog)
        self.minidspType.setObjectName("minidspType")
        self.minidspType.addItem("")
        self.minidspType.addItem("")
        self.minidspType.addItem("")
        self.innerLayout.addWidget(self.minidspType, 5, 1, 1, 4)
        self.filesProcessedLabel = QtWidgets.QLabel(mergeMinidspDialog)
        self.filesProcessedLabel.setObjectName("filesProcessedLabel")
        self.innerLayout.addWidget(self.filesProcessedLabel, 6, 0, 1, 1)
        self.configFilePicker = QtWidgets.QToolButton(mergeMinidspDialog)
        self.configFilePicker.setObjectName("configFilePicker")
        self.innerLayout.addWidget(self.configFilePicker, 3, 5, 1, 1)
        self.refreshGitRepo = QtWidgets.QToolButton(mergeMinidspDialog)
        self.refreshGitRepo.setObjectName("refreshGitRepo")
        self.innerLayout.addWidget(self.refreshGitRepo, 0, 5, 1, 1)
        self.errors = QtWidgets.QListWidget(mergeMinidspDialog)
        self.errors.setEnabled(False)
        self.errors.setObjectName("errors")
        self.innerLayout.addWidget(self.errors, 7, 1, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.innerLayout.addItem(spacerItem, 6, 4, 1, 1)
        self.lastCommitDate = QtWidgets.QDateTimeEdit(mergeMinidspDialog)
        self.lastCommitDate.setReadOnly(True)
        self.lastCommitDate.setObjectName("lastCommitDate")
        self.innerLayout.addWidget(self.lastCommitDate, 0, 1, 1, 3)
        self.outputDirectory = QtWidgets.QLineEdit(mergeMinidspDialog)
        self.outputDirectory.setEnabled(False)
        self.outputDirectory.setReadOnly(True)
        self.outputDirectory.setObjectName("outputDirectory")
        self.innerLayout.addWidget(self.outputDirectory, 4, 1, 1, 4)
        self.userSourceDirLayout = QtWidgets.QHBoxLayout()
        self.userSourceDirLayout.setObjectName("userSourceDirLayout")
        self.userSourceDir = QtWidgets.QLineEdit(mergeMinidspDialog)
        self.userSourceDir.setReadOnly(True)
        self.userSourceDir.setObjectName("userSourceDir")
        self.userSourceDirLayout.addWidget(self.userSourceDir)
        self.clearUserSourceDir = QtWidgets.QToolButton(mergeMinidspDialog)
        self.clearUserSourceDir.setObjectName("clearUserSourceDir")
        self.userSourceDirLayout.addWidget(self.clearUserSourceDir)
        self.innerLayout.addLayout(self.userSourceDirLayout, 2, 1, 1, 4)
        self.gridLayout.addLayout(self.innerLayout, 0, 0, 1, 1)

        self.retranslateUi(mergeMinidspDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), mergeMinidspDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), mergeMinidspDialog.reject)
        QtCore.QObject.connect(self.configFilePicker, QtCore.SIGNAL("clicked()"), mergeMinidspDialog.pick_config_file)
        QtCore.QObject.connect(self.outputDirectoryPicker, QtCore.SIGNAL("clicked()"), mergeMinidspDialog.pick_output_dir)
        QtCore.QObject.connect(self.processFiles, QtCore.SIGNAL("clicked()"), mergeMinidspDialog.process_files)
        QtCore.QObject.connect(self.refreshGitRepo, QtCore.SIGNAL("clicked()"), mergeMinidspDialog.refresh_repo)
        QtCore.QObject.connect(self.userSourceDirPicker, QtCore.SIGNAL("clicked()"), mergeMinidspDialog.pick_user_source_dir)
        QtCore.QObject.connect(self.clearUserSourceDir, QtCore.SIGNAL("clicked()"), mergeMinidspDialog.clear_user_source_dir)
        QtCore.QMetaObject.connectSlotsByName(mergeMinidspDialog)

    def retranslateUi(self, mergeMinidspDialog):
        mergeMinidspDialog.setWindowTitle(QtWidgets.QApplication.translate("mergeMinidspDialog", "Merge Minidsp Config", None, -1))
        self.minidspTypeLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "Minidsp Type", None, -1))
        self.processFiles.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "...", None, -1))
        self.outputDirectoryLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "Output Directory", None, -1))
        self.ofLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "of", None, -1))
        self.userSourceDirPicker.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "...", None, -1))
        self.lastUpdateLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "Last Update", None, -1))
        self.outputDirectoryPicker.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "...", None, -1))
        self.errorsLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "Errors", None, -1))
        self.configFileLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "Config File", None, -1))
        self.userSourceDirLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "User Source Directory", None, -1))
        self.minidspType.setItemText(0, QtWidgets.QApplication.translate("mergeMinidspDialog", "2x4 HD", None, -1))
        self.minidspType.setItemText(1, QtWidgets.QApplication.translate("mergeMinidspDialog", "2x4", None, -1))
        self.minidspType.setItemText(2, QtWidgets.QApplication.translate("mergeMinidspDialog", "10x10 HD", None, -1))
        self.filesProcessedLabel.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "Files Processed", None, -1))
        self.configFilePicker.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "...", None, -1))
        self.refreshGitRepo.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "...", None, -1))
        self.clearUserSourceDir.setText(QtWidgets.QApplication.translate("mergeMinidspDialog", "...", None, -1))

