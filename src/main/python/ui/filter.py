# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui',
# licensing of 'filter.ui' applies.
#
# Created: Sun Jun 30 22:06:40 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_editFilterDialog(object):
    def setupUi(self, editFilterDialog):
        editFilterDialog.setObjectName("editFilterDialog")
        editFilterDialog.resize(1390, 665)
        self.panes = QtWidgets.QGridLayout(editFilterDialog)
        self.panes.setObjectName("panes")
        self.viewPane = QtWidgets.QGridLayout()
        self.viewPane.setObjectName("viewPane")
        self.previewChart = MplWidget(editFilterDialog)
        self.previewChart.setObjectName("previewChart")
        self.viewPane.addWidget(self.previewChart, 0, 0, 1, 1)
        self.panes.addLayout(self.viewPane, 0, 1, 1, 1)
        self.paramsPane = QtWidgets.QGridLayout()
        self.paramsPane.setObjectName("paramsPane")
        self.passFilterType = QtWidgets.QComboBox(editFilterDialog)
        self.passFilterType.setEnabled(True)
        self.passFilterType.setObjectName("passFilterType")
        self.paramsPane.addWidget(self.passFilterType, 2, 1, 1, 1)
        self.filterType = QtWidgets.QComboBox(editFilterDialog)
        self.filterType.setObjectName("filterType")
        self.paramsPane.addWidget(self.filterType, 1, 1, 1, 1)
        self.typeLabel = QtWidgets.QLabel(editFilterDialog)
        self.typeLabel.setObjectName("typeLabel")
        self.paramsPane.addWidget(self.typeLabel, 1, 0, 1, 1)
        self.filterOrder = QtWidgets.QSpinBox(editFilterDialog)
        self.filterOrder.setEnabled(True)
        self.filterOrder.setMinimum(1)
        self.filterOrder.setMaximum(24)
        self.filterOrder.setProperty("value", 2)
        self.filterOrder.setObjectName("filterOrder")
        self.paramsPane.addWidget(self.filterOrder, 3, 1, 1, 1)
        self.gainLabel = QtWidgets.QLabel(editFilterDialog)
        self.gainLabel.setObjectName("gainLabel")
        self.paramsPane.addWidget(self.gainLabel, 7, 0, 1, 1)
        self.filterQLabel = QtWidgets.QLabel(editFilterDialog)
        self.filterQLabel.setObjectName("filterQLabel")
        self.paramsPane.addWidget(self.filterQLabel, 5, 0, 1, 1)
        self.sLabel = QtWidgets.QLabel(editFilterDialog)
        self.sLabel.setObjectName("sLabel")
        self.paramsPane.addWidget(self.sLabel, 6, 0, 1, 1)
        self.freqStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.freqStepButton.setObjectName("freqStepButton")
        self.paramsPane.addWidget(self.freqStepButton, 4, 2, 1, 1)
        self.filterQ = QtWidgets.QDoubleSpinBox(editFilterDialog)
        self.filterQ.setDecimals(4)
        self.filterQ.setMinimum(0.001)
        self.filterQ.setMaximum(20.0)
        self.filterQ.setSingleStep(0.0001)
        self.filterQ.setProperty("value", 0.7071)
        self.filterQ.setObjectName("filterQ")
        self.paramsPane.addWidget(self.filterQ, 5, 1, 1, 1)
        self.orderLabel = QtWidgets.QLabel(editFilterDialog)
        self.orderLabel.setObjectName("orderLabel")
        self.paramsPane.addWidget(self.orderLabel, 3, 0, 1, 1)
        self.filterCount = QtWidgets.QSpinBox(editFilterDialog)
        self.filterCount.setMinimum(1)
        self.filterCount.setMaximum(20)
        self.filterCount.setObjectName("filterCount")
        self.paramsPane.addWidget(self.filterCount, 8, 1, 1, 1)
        self.filterGain = QtWidgets.QDoubleSpinBox(editFilterDialog)
        self.filterGain.setDecimals(1)
        self.filterGain.setMinimum(-30.0)
        self.filterGain.setMaximum(30.0)
        self.filterGain.setSingleStep(0.1)
        self.filterGain.setObjectName("filterGain")
        self.paramsPane.addWidget(self.filterGain, 7, 1, 1, 1)
        self.gainStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.gainStepButton.setObjectName("gainStepButton")
        self.paramsPane.addWidget(self.gainStepButton, 7, 2, 1, 1)
        self.freqLabel = QtWidgets.QLabel(editFilterDialog)
        self.freqLabel.setObjectName("freqLabel")
        self.paramsPane.addWidget(self.freqLabel, 4, 0, 1, 1)
        self.freq = QtWidgets.QDoubleSpinBox(editFilterDialog)
        self.freq.setDecimals(1)
        self.freq.setMinimum(1.0)
        self.freq.setMaximum(500.0)
        self.freq.setSingleStep(0.1)
        self.freq.setProperty("value", 40.0)
        self.freq.setObjectName("freq")
        self.paramsPane.addWidget(self.freq, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.paramsPane.addItem(spacerItem, 13, 1, 1, 1)
        self.qStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.qStepButton.setObjectName("qStepButton")
        self.paramsPane.addWidget(self.qStepButton, 5, 2, 1, 1)
        self.sStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.sStepButton.setObjectName("sStepButton")
        self.paramsPane.addWidget(self.sStepButton, 6, 2, 1, 1)
        self.filterS = QtWidgets.QDoubleSpinBox(editFilterDialog)
        self.filterS.setEnabled(False)
        self.filterS.setDecimals(4)
        self.filterS.setMinimum(0.1)
        self.filterS.setMaximum(100.0)
        self.filterS.setSingleStep(0.0001)
        self.filterS.setProperty("value", 1.0)
        self.filterS.setObjectName("filterS")
        self.paramsPane.addWidget(self.filterS, 6, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QToolButton(editFilterDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.saveButton = QtWidgets.QToolButton(editFilterDialog)
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.exitButton = QtWidgets.QToolButton(editFilterDialog)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.limitsButton = QtWidgets.QToolButton(editFilterDialog)
        self.limitsButton.setObjectName("limitsButton")
        self.horizontalLayout.addWidget(self.limitsButton)
        self.paramsPane.addLayout(self.horizontalLayout, 10, 0, 1, 3)
        self.filterSelector = QtWidgets.QComboBox(editFilterDialog)
        self.filterSelector.setObjectName("filterSelector")
        self.paramsPane.addWidget(self.filterSelector, 0, 0, 1, 3)
        self.filterCountLabel = QtWidgets.QLabel(editFilterDialog)
        self.filterCountLabel.setObjectName("filterCountLabel")
        self.paramsPane.addWidget(self.filterCountLabel, 8, 0, 1, 1)
        self.showIndividual = QtWidgets.QCheckBox(editFilterDialog)
        self.showIndividual.setChecked(True)
        self.showIndividual.setObjectName("showIndividual")
        self.paramsPane.addWidget(self.showIndividual, 9, 0, 1, 3)
        self.paramsPane.setColumnStretch(0, 1)
        self.panes.addLayout(self.paramsPane, 0, 0, 1, 1)
        self.panes.setColumnStretch(1, 1)

        self.retranslateUi(editFilterDialog)
        QtCore.QObject.connect(self.filterType, QtCore.SIGNAL("currentTextChanged(QString)"), editFilterDialog.enableFilterParams)
        QtCore.QObject.connect(self.passFilterType, QtCore.SIGNAL("currentTextChanged(QString)"), editFilterDialog.changeOrderStep)
        QtCore.QObject.connect(self.filterGain, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.enableOkIfGainIsValid)
        QtCore.QObject.connect(self.filterQ, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.recalcShelfFromQ)
        QtCore.QObject.connect(self.filterGain, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.recalcShelfFromGain)
        QtCore.QObject.connect(self.filterType, QtCore.SIGNAL("currentIndexChanged(int)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.passFilterType, QtCore.SIGNAL("currentIndexChanged(int)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.filterOrder, QtCore.SIGNAL("valueChanged(int)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.freq, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.filterQ, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.filterGain, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.filterCount, QtCore.SIGNAL("valueChanged(int)"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.filterS, QtCore.SIGNAL("valueChanged(double)"), editFilterDialog.recalcShelfFromS)
        QtCore.QObject.connect(self.sStepButton, QtCore.SIGNAL("clicked()"), editFilterDialog.handleSToolButton)
        QtCore.QObject.connect(self.qStepButton, QtCore.SIGNAL("clicked()"), editFilterDialog.handleQToolButton)
        QtCore.QObject.connect(self.gainStepButton, QtCore.SIGNAL("clicked()"), editFilterDialog.handleGainToolButton)
        QtCore.QObject.connect(self.freqStepButton, QtCore.SIGNAL("clicked()"), editFilterDialog.handleFreqToolButton)
        QtCore.QObject.connect(self.saveButton, QtCore.SIGNAL("clicked()"), editFilterDialog.accept)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL("clicked()"), editFilterDialog.reject)
        QtCore.QObject.connect(self.filterSelector, QtCore.SIGNAL("currentIndexChanged(int)"), editFilterDialog.select_filter)
        QtCore.QObject.connect(self.showIndividual, QtCore.SIGNAL("clicked()"), editFilterDialog.previewFilter)
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL("clicked()"), editFilterDialog.add)
        QtCore.QObject.connect(self.limitsButton, QtCore.SIGNAL("clicked()"), editFilterDialog.show_limits)
        QtCore.QMetaObject.connectSlotsByName(editFilterDialog)
        editFilterDialog.setTabOrder(self.filterType, self.passFilterType)
        editFilterDialog.setTabOrder(self.passFilterType, self.filterOrder)
        editFilterDialog.setTabOrder(self.filterOrder, self.freq)
        editFilterDialog.setTabOrder(self.freq, self.filterQ)
        editFilterDialog.setTabOrder(self.filterQ, self.filterS)
        editFilterDialog.setTabOrder(self.filterS, self.filterGain)
        editFilterDialog.setTabOrder(self.filterGain, self.filterCount)
        editFilterDialog.setTabOrder(self.filterCount, self.freqStepButton)
        editFilterDialog.setTabOrder(self.freqStepButton, self.qStepButton)
        editFilterDialog.setTabOrder(self.qStepButton, self.gainStepButton)
        editFilterDialog.setTabOrder(self.gainStepButton, self.sStepButton)
        editFilterDialog.setTabOrder(self.sStepButton, self.previewChart)

    def retranslateUi(self, editFilterDialog):
        editFilterDialog.setWindowTitle(QtWidgets.QApplication.translate("editFilterDialog", "Create Filter", None, -1))
        self.typeLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "Type", None, -1))
        self.gainLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "Gain", None, -1))
        self.filterQLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "Q", None, -1))
        self.sLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "S", None, -1))
        self.freqStepButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.orderLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "Order", None, -1))
        self.gainStepButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.freqLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "Freq", None, -1))
        self.qStepButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.sStepButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.addButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.saveButton.setToolTip(QtWidgets.QApplication.translate("editFilterDialog", "Save", None, -1))
        self.saveButton.setShortcut(QtWidgets.QApplication.translate("editFilterDialog", "Return", None, -1))
        self.exitButton.setToolTip(QtWidgets.QApplication.translate("editFilterDialog", "Exit", None, -1))
        self.exitButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.limitsButton.setText(QtWidgets.QApplication.translate("editFilterDialog", "...", None, -1))
        self.filterCountLabel.setText(QtWidgets.QApplication.translate("editFilterDialog", "Count", None, -1))
        self.showIndividual.setText(QtWidgets.QApplication.translate("editFilterDialog", "Show Individual Filters", None, -1))

from mpl import MplWidget
