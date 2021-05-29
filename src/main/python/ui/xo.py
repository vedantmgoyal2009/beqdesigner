# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_xoDialog(object):
    def setupUi(self, xoDialog):
        xoDialog.setObjectName("xoDialog")
        xoDialog.resize(886, 820)
        self.verticalLayout = QtWidgets.QVBoxLayout(xoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chartLayout = QtWidgets.QHBoxLayout()
        self.chartLayout.setObjectName("chartLayout")
        self.previewChart = MplWidget(xoDialog)
        self.previewChart.setObjectName("previewChart")
        self.chartLayout.addWidget(self.previewChart)
        self.chartControlsLayout = QtWidgets.QVBoxLayout()
        self.chartControlsLayout.setObjectName("chartControlsLayout")
        self.limitsButton = QtWidgets.QToolButton(xoDialog)
        self.limitsButton.setObjectName("limitsButton")
        self.chartControlsLayout.addWidget(self.limitsButton)
        self.showPhase = QtWidgets.QToolButton(xoDialog)
        self.showPhase.setCheckable(True)
        self.showPhase.setObjectName("showPhase")
        self.chartControlsLayout.addWidget(self.showPhase)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.chartControlsLayout.addItem(spacerItem)
        self.chartLayout.addLayout(self.chartControlsLayout)
        self.verticalLayout.addLayout(self.chartLayout)
        self.xoContainerLayout = QtWidgets.QGridLayout()
        self.xoContainerLayout.setObjectName("xoContainerLayout")
        self.peqScrollArea = QtWidgets.QScrollArea(xoDialog)
        self.peqScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.peqScrollArea.setWidgetResizable(True)
        self.peqScrollArea.setObjectName("peqScrollArea")
        self.channelsFrame = QtWidgets.QFrame()
        self.channelsFrame.setGeometry(QtCore.QRect(0, 0, 868, 257))
        self.channelsFrame.setObjectName("channelsFrame")
        self.channelsLayout = QtWidgets.QVBoxLayout(self.channelsFrame)
        self.channelsLayout.setObjectName("channelsLayout")
        self.peqScrollArea.setWidget(self.channelsFrame)
        self.xoContainerLayout.addWidget(self.peqScrollArea, 1, 0, 1, 5)
        self.lfeAdjustLayout = QtWidgets.QHBoxLayout()
        self.lfeAdjustLayout.setObjectName("lfeAdjustLayout")
        self.lfeAdjustLabel = QtWidgets.QLabel(xoDialog)
        self.lfeAdjustLabel.setEnabled(True)
        self.lfeAdjustLabel.setObjectName("lfeAdjustLabel")
        self.lfeAdjustLayout.addWidget(self.lfeAdjustLabel)
        self.lfeAdjust = QtWidgets.QSpinBox(xoDialog)
        self.lfeAdjust.setEnabled(True)
        self.lfeAdjust.setMinimum(1)
        self.lfeAdjust.setMaximum(9)
        self.lfeAdjust.setProperty("value", 5)
        self.lfeAdjust.setObjectName("lfeAdjust")
        self.lfeAdjustLayout.addWidget(self.lfeAdjust)
        self.showFiltersButton = QtWidgets.QToolButton(xoDialog)
        self.showFiltersButton.setObjectName("showFiltersButton")
        self.lfeAdjustLayout.addWidget(self.showFiltersButton)
        self.xoContainerLayout.addLayout(self.lfeAdjustLayout, 0, 4, 1, 1)
        self.showMatrixButton = QtWidgets.QPushButton(xoDialog)
        self.showMatrixButton.setObjectName("showMatrixButton")
        self.xoContainerLayout.addWidget(self.showMatrixButton, 0, 1, 1, 1)
        self.lfeChannelSelectorLabel = QtWidgets.QLabel(xoDialog)
        self.lfeChannelSelectorLabel.setObjectName("lfeChannelSelectorLabel")
        self.xoContainerLayout.addWidget(self.lfeChannelSelectorLabel, 0, 2, 1, 1)
        self.linkChannelsButton = QtWidgets.QPushButton(xoDialog)
        self.linkChannelsButton.setObjectName("linkChannelsButton")
        self.xoContainerLayout.addWidget(self.linkChannelsButton, 0, 0, 1, 1)
        self.lfeChannelSelector = QtWidgets.QComboBox(xoDialog)
        self.lfeChannelSelector.setObjectName("lfeChannelSelector")
        self.xoContainerLayout.addWidget(self.lfeChannelSelector, 0, 3, 1, 1)
        self.xoContainerLayout.setColumnStretch(0, 1)
        self.xoContainerLayout.setColumnStretch(1, 1)
        self.xoContainerLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.xoContainerLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(xoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(xoDialog)
        self.buttonBox.accepted.connect(xoDialog.accept)
        self.buttonBox.rejected.connect(xoDialog.reject)
        self.showMatrixButton.clicked.connect(xoDialog.show_matrix)
        QtCore.QMetaObject.connectSlotsByName(xoDialog)
        xoDialog.setTabOrder(self.linkChannelsButton, self.showMatrixButton)
        xoDialog.setTabOrder(self.showMatrixButton, self.lfeAdjust)
        xoDialog.setTabOrder(self.lfeAdjust, self.peqScrollArea)
        xoDialog.setTabOrder(self.peqScrollArea, self.limitsButton)
        xoDialog.setTabOrder(self.limitsButton, self.showPhase)
        xoDialog.setTabOrder(self.showPhase, self.previewChart)

    def retranslateUi(self, xoDialog):
        _translate = QtCore.QCoreApplication.translate
        xoDialog.setWindowTitle(_translate("xoDialog", "Crossover Design"))
        self.limitsButton.setText(_translate("xoDialog", "..."))
        self.showPhase.setText(_translate("xoDialog", "..."))
        self.lfeAdjustLabel.setText(_translate("xoDialog", "LFE Headroom"))
        self.lfeAdjust.setSuffix(_translate("xoDialog", " dB"))
        self.showFiltersButton.setText(_translate("xoDialog", "..."))
        self.showMatrixButton.setText(_translate("xoDialog", "Input -> Output Routes"))
        self.lfeChannelSelectorLabel.setText(_translate("xoDialog", "LFE Channel: "))
        self.linkChannelsButton.setText(_translate("xoDialog", "Group Channels"))
from mpl import MplWidget