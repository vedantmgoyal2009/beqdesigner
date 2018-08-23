# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extract.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_extractAudioDialog(object):
    def setupUi(self, extractAudioDialog):
        extractAudioDialog.setObjectName("extractAudioDialog")
        extractAudioDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        extractAudioDialog.resize(880, 794)
        extractAudioDialog.setSizeGripEnabled(True)
        extractAudioDialog.setModal(False)
        self.boxLayout = QtWidgets.QVBoxLayout(extractAudioDialog)
        self.boxLayout.setObjectName("boxLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.audioStreams = QtWidgets.QComboBox(extractAudioDialog)
        self.audioStreams.setObjectName("audioStreams")
        self.gridLayout.addWidget(self.audioStreams, 1, 1, 1, 1)
        self.inputFile = QtWidgets.QLineEdit(extractAudioDialog)
        self.inputFile.setEnabled(False)
        self.inputFile.setObjectName("inputFile")
        self.gridLayout.addWidget(self.inputFile, 0, 1, 1, 1)
        self.inputFileLabel = QtWidgets.QLabel(extractAudioDialog)
        self.inputFileLabel.setObjectName("inputFileLabel")
        self.gridLayout.addWidget(self.inputFileLabel, 0, 0, 1, 1)
        self.inputFilePicker = QtWidgets.QToolButton(extractAudioDialog)
        self.inputFilePicker.setObjectName("inputFilePicker")
        self.gridLayout.addWidget(self.inputFilePicker, 0, 2, 1, 1)
        self.streamsLabel = QtWidgets.QLabel(extractAudioDialog)
        self.streamsLabel.setObjectName("streamsLabel")
        self.gridLayout.addWidget(self.streamsLabel, 1, 0, 1, 1)
        self.outputFilename = QtWidgets.QLineEdit(extractAudioDialog)
        self.outputFilename.setObjectName("outputFilename")
        self.gridLayout.addWidget(self.outputFilename, 4, 1, 1, 1)
        self.targetDirPicker = QtWidgets.QToolButton(extractAudioDialog)
        self.targetDirPicker.setObjectName("targetDirPicker")
        self.gridLayout.addWidget(self.targetDirPicker, 3, 2, 1, 1)
        self.ffmpegOutput = QtWidgets.QPlainTextEdit(extractAudioDialog)
        self.ffmpegOutput.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.ffmpegOutput.setFont(font)
        self.ffmpegOutput.setReadOnly(True)
        self.ffmpegOutput.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.ffmpegOutput.setObjectName("ffmpegOutput")
        self.gridLayout.addWidget(self.ffmpegOutput, 6, 1, 1, 1)
        self.showProbeButton = QtWidgets.QToolButton(extractAudioDialog)
        self.showProbeButton.setObjectName("showProbeButton")
        self.gridLayout.addWidget(self.showProbeButton, 1, 2, 1, 1)
        self.monoMix = QtWidgets.QCheckBox(extractAudioDialog)
        self.monoMix.setEnabled(True)
        self.monoMix.setChecked(True)
        self.monoMix.setObjectName("monoMix")
        self.gridLayout.addWidget(self.monoMix, 2, 1, 1, 1)
        self.outputFilenameLabel = QtWidgets.QLabel(extractAudioDialog)
        self.outputFilenameLabel.setObjectName("outputFilenameLabel")
        self.gridLayout.addWidget(self.outputFilenameLabel, 4, 0, 1, 1)
        self.targetDir = QtWidgets.QLineEdit(extractAudioDialog)
        self.targetDir.setEnabled(False)
        self.targetDir.setObjectName("targetDir")
        self.gridLayout.addWidget(self.targetDir, 3, 1, 1, 1)
        self.targetDirectoryLabel = QtWidgets.QLabel(extractAudioDialog)
        self.targetDirectoryLabel.setObjectName("targetDirectoryLabel")
        self.gridLayout.addWidget(self.targetDirectoryLabel, 3, 0, 1, 1)
        self.ffmpegCommandLine = QtWidgets.QPlainTextEdit(extractAudioDialog)
        self.ffmpegCommandLine.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.ffmpegCommandLine.setFont(font)
        self.ffmpegCommandLine.setReadOnly(True)
        self.ffmpegCommandLine.setObjectName("ffmpegCommandLine")
        self.gridLayout.addWidget(self.ffmpegCommandLine, 5, 1, 1, 1)
        self.ffmpegOutputLabel = QtWidgets.QLabel(extractAudioDialog)
        self.ffmpegOutputLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ffmpegOutputLabel.setObjectName("ffmpegOutputLabel")
        self.gridLayout.addWidget(self.ffmpegOutputLabel, 6, 0, 1, 1)
        self.ffmpegCommandLabel = QtWidgets.QLabel(extractAudioDialog)
        self.ffmpegCommandLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ffmpegCommandLabel.setObjectName("ffmpegCommandLabel")
        self.gridLayout.addWidget(self.ffmpegCommandLabel, 5, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 6)
        self.boxLayout.addLayout(self.gridLayout)
        self.buttonLayout = QtWidgets.QGridLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(extractAudioDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonLayout.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.boxLayout.addLayout(self.buttonLayout)

        self.retranslateUi(extractAudioDialog)
        self.buttonBox.accepted.connect(extractAudioDialog.accept)
        self.buttonBox.rejected.connect(extractAudioDialog.reject)
        self.inputFilePicker.clicked.connect(extractAudioDialog.selectFile)
        self.showProbeButton.clicked.connect(extractAudioDialog.showProbeInDetail)
        self.targetDirPicker.clicked.connect(extractAudioDialog.setTargetDirectory)
        self.outputFilename.editingFinished.connect(extractAudioDialog.updateFfmpegCommand)
        self.audioStreams.currentIndexChanged['int'].connect(extractAudioDialog.updateFfmpegSpec)
        self.outputFilename.editingFinished.connect(extractAudioDialog.updateFfmpegCommand)
        self.monoMix.clicked.connect(extractAudioDialog.toggleMonoMix)
        QtCore.QMetaObject.connectSlotsByName(extractAudioDialog)

    def retranslateUi(self, extractAudioDialog):
        _translate = QtCore.QCoreApplication.translate
        extractAudioDialog.setWindowTitle(_translate("extractAudioDialog", "Extract Audio"))
        self.inputFileLabel.setText(_translate("extractAudioDialog", "File"))
        self.inputFilePicker.setText(_translate("extractAudioDialog", "..."))
        self.streamsLabel.setText(_translate("extractAudioDialog", "Streams"))
        self.targetDirPicker.setText(_translate("extractAudioDialog", "..."))
        self.showProbeButton.setText(_translate("extractAudioDialog", "..."))
        self.monoMix.setText(_translate("extractAudioDialog", "Mix to Mono?"))
        self.outputFilenameLabel.setText(_translate("extractAudioDialog", "Output Filename"))
        self.targetDirectoryLabel.setText(_translate("extractAudioDialog", "Target Directory"))
        self.ffmpegOutputLabel.setText(_translate("extractAudioDialog", "ffmpeg output"))
        self.ffmpegCommandLabel.setText(_translate("extractAudioDialog", "ffmpeg command "))

