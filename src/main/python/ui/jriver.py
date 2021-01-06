# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jriver.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jriverDspDialog(object):
    def setupUi(self, jriverDspDialog):
        jriverDspDialog.setObjectName("jriverDspDialog")
        jriverDspDialog.resize(1703, 698)
        self.dialogLayout = QtWidgets.QGridLayout(jriverDspDialog)
        self.dialogLayout.setObjectName("dialogLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(jriverDspDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.dialogLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.previewChart = MplWidget(jriverDspDialog)
        self.previewChart.setObjectName("previewChart")
        self.dialogLayout.addWidget(self.previewChart, 1, 1, 1, 1)
        self.chartControlLayout = QtWidgets.QHBoxLayout()
        self.chartControlLayout.setObjectName("chartControlLayout")
        self.limitsButton = QtWidgets.QToolButton(jriverDspDialog)
        self.limitsButton.setObjectName("limitsButton")
        self.chartControlLayout.addWidget(self.limitsButton)
        self.fullRangeButton = QtWidgets.QToolButton(jriverDspDialog)
        self.fullRangeButton.setObjectName("fullRangeButton")
        self.chartControlLayout.addWidget(self.fullRangeButton)
        self.subOnlyButton = QtWidgets.QToolButton(jriverDspDialog)
        self.subOnlyButton.setObjectName("subOnlyButton")
        self.chartControlLayout.addWidget(self.subOnlyButton)
        self.showPhase = QtWidgets.QCheckBox(jriverDspDialog)
        self.showPhase.setObjectName("showPhase")
        self.chartControlLayout.addWidget(self.showPhase)
        self.dialogLayout.addLayout(self.chartControlLayout, 0, 1, 1, 1)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.configLayout = QtWidgets.QHBoxLayout()
        self.configLayout.setObjectName("configLayout")
        self.filenameLabel = QtWidgets.QLabel(jriverDspDialog)
        self.filenameLabel.setObjectName("filenameLabel")
        self.configLayout.addWidget(self.filenameLabel)
        self.filename = QtWidgets.QLineEdit(jriverDspDialog)
        self.filename.setReadOnly(True)
        self.filename.setObjectName("filename")
        self.configLayout.addWidget(self.filename)
        self.findFilenameButton = QtWidgets.QToolButton(jriverDspDialog)
        self.findFilenameButton.setObjectName("findFilenameButton")
        self.configLayout.addWidget(self.findFilenameButton)
        self.blockSelector = QtWidgets.QComboBox(jriverDspDialog)
        self.blockSelector.setObjectName("blockSelector")
        self.blockSelector.addItem("")
        self.blockSelector.addItem("")
        self.configLayout.addWidget(self.blockSelector)
        self.configLayout.setStretch(1, 4)
        self.configLayout.setStretch(3, 2)
        self.mainLayout.addLayout(self.configLayout)
        self.selectorLayout = QtWidgets.QHBoxLayout()
        self.selectorLayout.setObjectName("selectorLayout")
        self.channelList = QtWidgets.QListWidget(jriverDspDialog)
        self.channelList.setProperty("showDropIndicator", False)
        self.channelList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.channelList.setObjectName("channelList")
        self.selectorLayout.addWidget(self.channelList)
        self.filterList = QtWidgets.QListWidget(jriverDspDialog)
        self.filterList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.filterList.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.filterList.setObjectName("filterList")
        self.selectorLayout.addWidget(self.filterList)
        self.selectorLayout.setStretch(1, 1)
        self.mainLayout.addLayout(self.selectorLayout)
        self.perChannelLayout = QtWidgets.QHBoxLayout()
        self.perChannelLayout.setObjectName("perChannelLayout")
        self.mainLayout.addLayout(self.perChannelLayout)
        self.dialogLayout.addLayout(self.mainLayout, 0, 0, 2, 1)
        self.dialogLayout.setColumnStretch(0, 2)
        self.dialogLayout.setColumnStretch(1, 3)

        self.retranslateUi(jriverDspDialog)
        self.buttonBox.accepted.connect(jriverDspDialog.accept)
        self.buttonBox.rejected.connect(jriverDspDialog.reject)
        self.findFilenameButton.clicked.connect(jriverDspDialog.find_dsp_file)
        self.channelList.itemSelectionChanged.connect(jriverDspDialog.show_channel_filters)
        self.showPhase.stateChanged['int'].connect(jriverDspDialog.show_phase_response)
        self.subOnlyButton.clicked.connect(jriverDspDialog.show_sub_only)
        self.fullRangeButton.clicked.connect(jriverDspDialog.show_full_range)
        self.limitsButton.clicked.connect(jriverDspDialog.show_limits)
        self.blockSelector.currentTextChanged['QString'].connect(jriverDspDialog.show_filters)
        QtCore.QMetaObject.connectSlotsByName(jriverDspDialog)

    def retranslateUi(self, jriverDspDialog):
        _translate = QtCore.QCoreApplication.translate
        jriverDspDialog.setWindowTitle(_translate("jriverDspDialog", "JRiver Media Center DSP Editor"))
        self.limitsButton.setText(_translate("jriverDspDialog", "..."))
        self.fullRangeButton.setText(_translate("jriverDspDialog", "..."))
        self.subOnlyButton.setText(_translate("jriverDspDialog", "..."))
        self.showPhase.setText(_translate("jriverDspDialog", "Show Phase Response"))
        self.filenameLabel.setText(_translate("jriverDspDialog", "Config"))
        self.findFilenameButton.setText(_translate("jriverDspDialog", "..."))
        self.blockSelector.setItemText(0, _translate("jriverDspDialog", "Parametric Equaliser 1"))
        self.blockSelector.setItemText(1, _translate("jriverDspDialog", "Parametric Equaliser 2"))
from mpl import MplWidget