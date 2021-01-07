# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editFilterDialog(object):
    def setupUi(self, editFilterDialog):
        editFilterDialog.setObjectName("editFilterDialog")
        editFilterDialog.resize(1390, 982)
        self.panes = QtWidgets.QGridLayout(editFilterDialog)
        self.panes.setObjectName("panes")
        self.viewPane = QtWidgets.QGridLayout()
        self.viewPane.setObjectName("viewPane")
        self.previewChart = MplWidget(editFilterDialog)
        self.previewChart.setObjectName("previewChart")
        self.viewPane.addWidget(self.previewChart, 0, 0, 1, 1)
        self.panes.addLayout(self.viewPane, 0, 1, 1, 1)
        self.graphButtonsLayout = QtWidgets.QVBoxLayout()
        self.graphButtonsLayout.setObjectName("graphButtonsLayout")
        self.limitsButton = QtWidgets.QToolButton(editFilterDialog)
        self.limitsButton.setObjectName("limitsButton")
        self.graphButtonsLayout.addWidget(self.limitsButton)
        self.fullRangeButton = QtWidgets.QToolButton(editFilterDialog)
        self.fullRangeButton.setObjectName("fullRangeButton")
        self.graphButtonsLayout.addWidget(self.fullRangeButton)
        self.subOnlyButton = QtWidgets.QToolButton(editFilterDialog)
        self.subOnlyButton.setObjectName("subOnlyButton")
        self.graphButtonsLayout.addWidget(self.subOnlyButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.graphButtonsLayout.addItem(spacerItem)
        self.panes.addLayout(self.graphButtonsLayout, 0, 2, 1, 1)
        self.paramsPane = QtWidgets.QGridLayout()
        self.paramsPane.setObjectName("paramsPane")
        self.filterCountLabel = QtWidgets.QLabel(editFilterDialog)
        self.filterCountLabel.setObjectName("filterCountLabel")
        self.paramsPane.addWidget(self.filterCountLabel, 10, 0, 1, 1)
        self.filterType = QtWidgets.QComboBox(editFilterDialog)
        self.filterType.setObjectName("filterType")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.filterType.addItem("")
        self.paramsPane.addWidget(self.filterType, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.paramsPane.addItem(spacerItem1, 15, 1, 1, 1)
        self.gainLabel = QtWidgets.QLabel(editFilterDialog)
        self.gainLabel.setObjectName("gainLabel")
        self.paramsPane.addWidget(self.gainLabel, 9, 0, 1, 1)
        self.ltInLabel = QtWidgets.QLabel(editFilterDialog)
        self.ltInLabel.setObjectName("ltInLabel")
        self.paramsPane.addWidget(self.ltInLabel, 11, 0, 1, 1)
        self.headerLabel = QtWidgets.QLabel(editFilterDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.headerLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.headerLabel.setText("")
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.paramsPane.addWidget(self.headerLabel, 1, 0, 1, 2)
        self.snapLayout = QtWidgets.QHBoxLayout()
        self.snapLayout.setObjectName("snapLayout")
        self.snapLabel = QtWidgets.QLabel(editFilterDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.snapLabel.setFont(font)
        self.snapLabel.setObjectName("snapLabel")
        self.snapLayout.addWidget(self.snapLabel)
        self.snapFilterButton = QtWidgets.QToolButton(editFilterDialog)
        self.snapFilterButton.setObjectName("snapFilterButton")
        self.snapLayout.addWidget(self.snapFilterButton)
        self.loadSnapButton = QtWidgets.QToolButton(editFilterDialog)
        self.loadSnapButton.setObjectName("loadSnapButton")
        self.snapLayout.addWidget(self.loadSnapButton)
        self.acceptSnapButton = QtWidgets.QToolButton(editFilterDialog)
        self.acceptSnapButton.setObjectName("acceptSnapButton")
        self.snapLayout.addWidget(self.acceptSnapButton)
        self.resetButton = QtWidgets.QToolButton(editFilterDialog)
        self.resetButton.setObjectName("resetButton")
        self.snapLayout.addWidget(self.resetButton)
        self.paramsPane.addLayout(self.snapLayout, 16, 0, 1, 2)
        self.passFilterType = QtWidgets.QComboBox(editFilterDialog)
        self.passFilterType.setEnabled(True)
        self.passFilterType.setObjectName("passFilterType")
        self.passFilterType.addItem("")
        self.passFilterType.addItem("")
        self.paramsPane.addWidget(self.passFilterType, 4, 1, 1, 1)
        self.qStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.qStepButton.setObjectName("qStepButton")
        self.paramsPane.addWidget(self.qStepButton, 7, 2, 1, 1)
        self.freqStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.freqStepButton.setObjectName("freqStepButton")
        self.paramsPane.addWidget(self.freqStepButton, 6, 2, 1, 1)
        self.filterGain = NoFillDoubleSpinBox(editFilterDialog)
        self.filterGain.setDecimals(2)
        self.filterGain.setMinimum(-30.0)
        self.filterGain.setMaximum(30.0)
        self.filterGain.setSingleStep(0.01)
        self.filterGain.setObjectName("filterGain")
        self.paramsPane.addWidget(self.filterGain, 9, 1, 1, 1)
        self.snapshotFilterView = QtWidgets.QTableView(editFilterDialog)
        self.snapshotFilterView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.snapshotFilterView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.snapshotFilterView.setObjectName("snapshotFilterView")
        self.paramsPane.addWidget(self.snapshotFilterView, 18, 0, 1, 2)
        self.freqLabel = QtWidgets.QLabel(editFilterDialog)
        self.freqLabel.setObjectName("freqLabel")
        self.paramsPane.addWidget(self.freqLabel, 6, 0, 1, 1)
        self.ltOutLayout = QtWidgets.QHBoxLayout()
        self.ltOutLayout.setObjectName("ltOutLayout")
        self.fp = NoFillDoubleSpinBox(editFilterDialog)
        self.fp.setDecimals(1)
        self.fp.setMinimum(1.0)
        self.fp.setMaximum(400.0)
        self.fp.setSingleStep(0.1)
        self.fp.setProperty("value", 30.0)
        self.fp.setObjectName("fp")
        self.ltOutLayout.addWidget(self.fp)
        self.qp = NoFillDoubleSpinBox(editFilterDialog)
        self.qp.setDecimals(3)
        self.qp.setMinimum(0.001)
        self.qp.setMaximum(3.0)
        self.qp.setSingleStep(0.001)
        self.qp.setProperty("value", 0.707)
        self.qp.setObjectName("qp")
        self.ltOutLayout.addWidget(self.qp)
        self.paramsPane.addLayout(self.ltOutLayout, 12, 1, 1, 1)
        self.typeLabel = QtWidgets.QLabel(editFilterDialog)
        self.typeLabel.setObjectName("typeLabel")
        self.paramsPane.addWidget(self.typeLabel, 3, 0, 1, 1)
        self.filterQ = NoFillDoubleSpinBox(editFilterDialog)
        self.filterQ.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.filterQ.setDecimals(4)
        self.filterQ.setMinimum(0.001)
        self.filterQ.setMaximum(20.0)
        self.filterQ.setSingleStep(0.0001)
        self.filterQ.setProperty("value", 0.7071)
        self.filterQ.setObjectName("filterQ")
        self.paramsPane.addWidget(self.filterQ, 7, 1, 1, 1)
        self.workingViewButtonWidget = QtWidgets.QWidget(editFilterDialog)
        self.workingViewButtonWidget.setObjectName("workingViewButtonWidget")
        self.workingViewButtonLayout = QtWidgets.QVBoxLayout(self.workingViewButtonWidget)
        self.workingViewButtonLayout.setObjectName("workingViewButtonLayout")
        self.addWorkingRowButton = QtWidgets.QToolButton(self.workingViewButtonWidget)
        self.addWorkingRowButton.setObjectName("addWorkingRowButton")
        self.workingViewButtonLayout.addWidget(self.addWorkingRowButton)
        self.removeWorkingRowButton = QtWidgets.QToolButton(self.workingViewButtonWidget)
        self.removeWorkingRowButton.setObjectName("removeWorkingRowButton")
        self.workingViewButtonLayout.addWidget(self.removeWorkingRowButton)
        self.pasteWorkingRowButton = QtWidgets.QToolButton(self.workingViewButtonWidget)
        self.pasteWorkingRowButton.setObjectName("pasteWorkingRowButton")
        self.workingViewButtonLayout.addWidget(self.pasteWorkingRowButton)
        self.importWorkingButton = QtWidgets.QToolButton(self.workingViewButtonWidget)
        self.importWorkingButton.setObjectName("importWorkingButton")
        self.workingViewButtonLayout.addWidget(self.importWorkingButton)
        self.paramsPane.addWidget(self.workingViewButtonWidget, 0, 2, 1, 1)
        self.orderLabel = QtWidgets.QLabel(editFilterDialog)
        self.orderLabel.setObjectName("orderLabel")
        self.paramsPane.addWidget(self.orderLabel, 5, 0, 1, 1)
        self.filterS = NoFillDoubleSpinBox(editFilterDialog)
        self.filterS.setEnabled(False)
        self.filterS.setDecimals(4)
        self.filterS.setMinimum(0.1)
        self.filterS.setMaximum(100.0)
        self.filterS.setSingleStep(0.0001)
        self.filterS.setProperty("value", 1.0)
        self.filterS.setObjectName("filterS")
        self.paramsPane.addWidget(self.filterS, 8, 1, 1, 1)
        self.snapshotViewButtonWidget = QtWidgets.QWidget(editFilterDialog)
        self.snapshotViewButtonWidget.setObjectName("snapshotViewButtonWidget")
        self.snapshotViewButtonLayout = QtWidgets.QVBoxLayout(self.snapshotViewButtonWidget)
        self.snapshotViewButtonLayout.setObjectName("snapshotViewButtonLayout")
        self.addSnapshotRowButton = QtWidgets.QToolButton(self.snapshotViewButtonWidget)
        self.addSnapshotRowButton.setObjectName("addSnapshotRowButton")
        self.snapshotViewButtonLayout.addWidget(self.addSnapshotRowButton)
        self.removeSnapshotRowButton = QtWidgets.QToolButton(self.snapshotViewButtonWidget)
        self.removeSnapshotRowButton.setObjectName("removeSnapshotRowButton")
        self.snapshotViewButtonLayout.addWidget(self.removeSnapshotRowButton)
        self.pasteSnapshotRowButton = QtWidgets.QToolButton(self.snapshotViewButtonWidget)
        self.pasteSnapshotRowButton.setObjectName("pasteSnapshotRowButton")
        self.snapshotViewButtonLayout.addWidget(self.pasteSnapshotRowButton)
        self.importSnapshotButton = QtWidgets.QToolButton(self.snapshotViewButtonWidget)
        self.importSnapshotButton.setObjectName("importSnapshotButton")
        self.snapshotViewButtonLayout.addWidget(self.importSnapshotButton)
        self.paramsPane.addWidget(self.snapshotViewButtonWidget, 18, 2, 1, 1)
        self.sStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.sStepButton.setObjectName("sStepButton")
        self.paramsPane.addWidget(self.sStepButton, 8, 2, 1, 1)
        self.ltInLayout = QtWidgets.QHBoxLayout()
        self.ltInLayout.setObjectName("ltInLayout")
        self.f0 = NoFillDoubleSpinBox(editFilterDialog)
        self.f0.setDecimals(1)
        self.f0.setMinimum(1.0)
        self.f0.setMaximum(400.0)
        self.f0.setSingleStep(0.1)
        self.f0.setProperty("value", 40.0)
        self.f0.setObjectName("f0")
        self.ltInLayout.addWidget(self.f0)
        self.q0 = NoFillDoubleSpinBox(editFilterDialog)
        self.q0.setDecimals(3)
        self.q0.setMinimum(0.001)
        self.q0.setMaximum(3.0)
        self.q0.setSingleStep(0.001)
        self.q0.setProperty("value", 0.707)
        self.q0.setObjectName("q0")
        self.ltInLayout.addWidget(self.q0)
        self.paramsPane.addLayout(self.ltInLayout, 11, 1, 1, 1)
        self.filterQLabel = QtWidgets.QLabel(editFilterDialog)
        self.filterQLabel.setObjectName("filterQLabel")
        self.paramsPane.addWidget(self.filterQLabel, 7, 0, 1, 1)
        self.optimiseLayout = QtWidgets.QHBoxLayout()
        self.optimiseLayout.setObjectName("optimiseLayout")
        self.optimiseLabel = QtWidgets.QLabel(editFilterDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.optimiseLabel.setFont(font)
        self.optimiseLabel.setObjectName("optimiseLabel")
        self.optimiseLayout.addWidget(self.optimiseLabel)
        self.optimiseButton = QtWidgets.QToolButton(editFilterDialog)
        self.optimiseButton.setObjectName("optimiseButton")
        self.optimiseLayout.addWidget(self.optimiseButton)
        self.targetBiquadCount = QtWidgets.QSpinBox(editFilterDialog)
        self.targetBiquadCount.setMinimum(1)
        self.targetBiquadCount.setMaximum(20)
        self.targetBiquadCount.setProperty("value", 6)
        self.targetBiquadCount.setObjectName("targetBiquadCount")
        self.optimiseLayout.addWidget(self.targetBiquadCount)
        self.paramsPane.addLayout(self.optimiseLayout, 17, 0, 1, 2)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.saveButton = QtWidgets.QToolButton(editFilterDialog)
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        self.exitButton = QtWidgets.QToolButton(editFilterDialog)
        self.exitButton.setObjectName("exitButton")
        self.buttonLayout.addWidget(self.exitButton)
        self.paramsPane.addLayout(self.buttonLayout, 14, 0, 1, 2)
        self.ltOutLabel = QtWidgets.QLabel(editFilterDialog)
        self.ltOutLabel.setObjectName("ltOutLabel")
        self.paramsPane.addWidget(self.ltOutLabel, 12, 0, 1, 1)
        self.gainStepButton = QtWidgets.QToolButton(editFilterDialog)
        self.gainStepButton.setObjectName("gainStepButton")
        self.paramsPane.addWidget(self.gainStepButton, 9, 2, 1, 1)
        self.sLabel = QtWidgets.QLabel(editFilterDialog)
        self.sLabel.setObjectName("sLabel")
        self.paramsPane.addWidget(self.sLabel, 8, 0, 1, 1)
        self.freq = NoFillDoubleSpinBox(editFilterDialog)
        self.freq.setDecimals(2)
        self.freq.setMinimum(1.0)
        self.freq.setMaximum(24000.0)
        self.freq.setSingleStep(0.1)
        self.freq.setProperty("value", 40.0)
        self.freq.setObjectName("freq")
        self.paramsPane.addWidget(self.freq, 6, 1, 1, 1)
        self.filterCount = QtWidgets.QSpinBox(editFilterDialog)
        self.filterCount.setMinimum(1)
        self.filterCount.setMaximum(20)
        self.filterCount.setObjectName("filterCount")
        self.paramsPane.addWidget(self.filterCount, 10, 1, 1, 1)
        self.filterOrder = QtWidgets.QSpinBox(editFilterDialog)
        self.filterOrder.setEnabled(True)
        self.filterOrder.setMinimum(1)
        self.filterOrder.setMaximum(24)
        self.filterOrder.setProperty("value", 2)
        self.filterOrder.setObjectName("filterOrder")
        self.paramsPane.addWidget(self.filterOrder, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.paramsPane.addItem(spacerItem2, 19, 1, 1, 1)
        self.workingFilterView = QtWidgets.QTableView(editFilterDialog)
        self.workingFilterView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.workingFilterView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.workingFilterView.setObjectName("workingFilterView")
        self.paramsPane.addWidget(self.workingFilterView, 0, 0, 1, 2)
        self.shortcutLayout = QtWidgets.QHBoxLayout()
        self.shortcutLayout.setObjectName("shortcutLayout")
        self.addWorkingPeakingButton = QtWidgets.QToolButton(editFilterDialog)
        self.addWorkingPeakingButton.setObjectName("addWorkingPeakingButton")
        self.shortcutLayout.addWidget(self.addWorkingPeakingButton)
        self.addWorkingLowShelfButton = QtWidgets.QToolButton(editFilterDialog)
        self.addWorkingLowShelfButton.setObjectName("addWorkingLowShelfButton")
        self.shortcutLayout.addWidget(self.addWorkingLowShelfButton)
        self.addWorkingHighShelfButton = QtWidgets.QToolButton(editFilterDialog)
        self.addWorkingHighShelfButton.setObjectName("addWorkingHighShelfButton")
        self.shortcutLayout.addWidget(self.addWorkingHighShelfButton)
        self.paramsPane.addLayout(self.shortcutLayout, 2, 0, 1, 2)
        self.checkboxLayout = QtWidgets.QHBoxLayout()
        self.checkboxLayout.setObjectName("checkboxLayout")
        self.showIndividual = QtWidgets.QCheckBox(editFilterDialog)
        self.showIndividual.setChecked(True)
        self.showIndividual.setObjectName("showIndividual")
        self.checkboxLayout.addWidget(self.showIndividual)
        self.showPhase = QtWidgets.QCheckBox(editFilterDialog)
        self.showPhase.setChecked(False)
        self.showPhase.setObjectName("showPhase")
        self.checkboxLayout.addWidget(self.showPhase)
        self.paramsPane.addLayout(self.checkboxLayout, 13, 0, 1, 3)
        self.paramsPane.setColumnStretch(0, 1)
        self.paramsPane.setColumnStretch(1, 4)
        self.panes.addLayout(self.paramsPane, 0, 0, 1, 1)
        self.panes.setColumnStretch(0, 1)
        self.panes.setColumnStretch(1, 3)

        self.retranslateUi(editFilterDialog)
        self.filterType.currentTextChanged['QString'].connect(editFilterDialog.enableFilterParams)
        self.passFilterType.currentTextChanged['QString'].connect(editFilterDialog.changeOrderStep)
        self.filterQ.valueChanged['double'].connect(editFilterDialog.recalcShelfFromQ)
        self.filterGain.valueChanged['double'].connect(editFilterDialog.recalcShelfFromGain)
        self.filterType.currentIndexChanged['int'].connect(editFilterDialog.previewFilter)
        self.passFilterType.currentIndexChanged['int'].connect(editFilterDialog.previewFilter)
        self.filterOrder.valueChanged['int'].connect(editFilterDialog.previewFilter)
        self.freq.valueChanged['double'].connect(editFilterDialog.previewFilter)
        self.filterQ.valueChanged['double'].connect(editFilterDialog.previewFilter)
        self.filterGain.valueChanged['double'].connect(editFilterDialog.previewFilter)
        self.filterCount.valueChanged['int'].connect(editFilterDialog.previewFilter)
        self.filterS.valueChanged['double'].connect(editFilterDialog.recalcShelfFromS)
        self.sStepButton.clicked.connect(editFilterDialog.handleSToolButton)
        self.qStepButton.clicked.connect(editFilterDialog.handleQToolButton)
        self.gainStepButton.clicked.connect(editFilterDialog.handleGainToolButton)
        self.freqStepButton.clicked.connect(editFilterDialog.handleFreqToolButton)
        self.saveButton.clicked.connect(editFilterDialog.accept)
        self.exitButton.clicked.connect(editFilterDialog.reject)
        self.showIndividual.clicked.connect(editFilterDialog.previewFilter)
        self.limitsButton.clicked.connect(editFilterDialog.show_limits)
        self.fullRangeButton.clicked.connect(editFilterDialog.show_full_range)
        self.subOnlyButton.clicked.connect(editFilterDialog.show_sub_only)
        self.showPhase.clicked.connect(editFilterDialog.show_phase_response)
        self.f0.valueChanged['double'].connect(editFilterDialog.previewFilter)
        self.q0.valueChanged['double'].connect(editFilterDialog.previewFilter)
        self.fp.valueChanged['double'].connect(editFilterDialog.previewFilter)
        self.qp.valueChanged['double'].connect(editFilterDialog.previewFilter)
        QtCore.QMetaObject.connectSlotsByName(editFilterDialog)
        editFilterDialog.setTabOrder(self.filterType, self.passFilterType)
        editFilterDialog.setTabOrder(self.passFilterType, self.filterOrder)
        editFilterDialog.setTabOrder(self.filterOrder, self.freq)
        editFilterDialog.setTabOrder(self.freq, self.filterQ)
        editFilterDialog.setTabOrder(self.filterQ, self.filterS)
        editFilterDialog.setTabOrder(self.filterS, self.filterGain)
        editFilterDialog.setTabOrder(self.filterGain, self.filterCount)
        editFilterDialog.setTabOrder(self.filterCount, self.f0)
        editFilterDialog.setTabOrder(self.f0, self.q0)
        editFilterDialog.setTabOrder(self.q0, self.fp)
        editFilterDialog.setTabOrder(self.fp, self.qp)
        editFilterDialog.setTabOrder(self.qp, self.freqStepButton)
        editFilterDialog.setTabOrder(self.freqStepButton, self.qStepButton)
        editFilterDialog.setTabOrder(self.qStepButton, self.sStepButton)
        editFilterDialog.setTabOrder(self.sStepButton, self.gainStepButton)
        editFilterDialog.setTabOrder(self.gainStepButton, self.previewChart)
        editFilterDialog.setTabOrder(self.previewChart, self.limitsButton)
        editFilterDialog.setTabOrder(self.limitsButton, self.fullRangeButton)
        editFilterDialog.setTabOrder(self.fullRangeButton, self.subOnlyButton)
        editFilterDialog.setTabOrder(self.subOnlyButton, self.snapFilterButton)
        editFilterDialog.setTabOrder(self.snapFilterButton, self.loadSnapButton)
        editFilterDialog.setTabOrder(self.loadSnapButton, self.acceptSnapButton)
        editFilterDialog.setTabOrder(self.acceptSnapButton, self.resetButton)
        editFilterDialog.setTabOrder(self.resetButton, self.saveButton)
        editFilterDialog.setTabOrder(self.saveButton, self.exitButton)
        editFilterDialog.setTabOrder(self.exitButton, self.snapshotFilterView)
        editFilterDialog.setTabOrder(self.snapshotFilterView, self.workingFilterView)
        editFilterDialog.setTabOrder(self.workingFilterView, self.showIndividual)
        editFilterDialog.setTabOrder(self.showIndividual, self.showPhase)
        editFilterDialog.setTabOrder(self.showPhase, self.addSnapshotRowButton)
        editFilterDialog.setTabOrder(self.addSnapshotRowButton, self.removeSnapshotRowButton)
        editFilterDialog.setTabOrder(self.removeSnapshotRowButton, self.importSnapshotButton)
        editFilterDialog.setTabOrder(self.importSnapshotButton, self.optimiseButton)
        editFilterDialog.setTabOrder(self.optimiseButton, self.targetBiquadCount)
        editFilterDialog.setTabOrder(self.targetBiquadCount, self.addWorkingRowButton)
        editFilterDialog.setTabOrder(self.addWorkingRowButton, self.removeWorkingRowButton)
        editFilterDialog.setTabOrder(self.removeWorkingRowButton, self.importWorkingButton)

    def retranslateUi(self, editFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        editFilterDialog.setWindowTitle(_translate("editFilterDialog", "Create Filter"))
        self.limitsButton.setText(_translate("editFilterDialog", "..."))
        self.fullRangeButton.setText(_translate("editFilterDialog", "..."))
        self.subOnlyButton.setText(_translate("editFilterDialog", "..."))
        self.filterCountLabel.setText(_translate("editFilterDialog", "Count"))
        self.filterType.setItemText(0, _translate("editFilterDialog", "Low Shelf"))
        self.filterType.setItemText(1, _translate("editFilterDialog", "High Shelf"))
        self.filterType.setItemText(2, _translate("editFilterDialog", "PEQ"))
        self.filterType.setItemText(3, _translate("editFilterDialog", "Gain"))
        self.filterType.setItemText(4, _translate("editFilterDialog", "Linkwitz Transform"))
        self.filterType.setItemText(5, _translate("editFilterDialog", "Variable Q LPF"))
        self.filterType.setItemText(6, _translate("editFilterDialog", "Variable Q HPF"))
        self.filterType.setItemText(7, _translate("editFilterDialog", "Low Pass"))
        self.filterType.setItemText(8, _translate("editFilterDialog", "High Pass"))
        self.gainLabel.setText(_translate("editFilterDialog", "Gain"))
        self.ltInLabel.setText(_translate("editFilterDialog", "F(0) / Q(0)"))
        self.snapLabel.setText(_translate("editFilterDialog", "Compare"))
        self.snapFilterButton.setText(_translate("editFilterDialog", "..."))
        self.loadSnapButton.setText(_translate("editFilterDialog", "..."))
        self.acceptSnapButton.setText(_translate("editFilterDialog", "..."))
        self.resetButton.setText(_translate("editFilterDialog", "..."))
        self.passFilterType.setItemText(0, _translate("editFilterDialog", "Butterworth"))
        self.passFilterType.setItemText(1, _translate("editFilterDialog", "Linkwitz-Riley"))
        self.qStepButton.setText(_translate("editFilterDialog", "..."))
        self.freqStepButton.setText(_translate("editFilterDialog", "..."))
        self.freqLabel.setText(_translate("editFilterDialog", "Freq"))
        self.typeLabel.setText(_translate("editFilterDialog", "Type"))
        self.addWorkingRowButton.setText(_translate("editFilterDialog", "..."))
        self.addWorkingRowButton.setShortcut(_translate("editFilterDialog", "="))
        self.removeWorkingRowButton.setText(_translate("editFilterDialog", "..."))
        self.removeWorkingRowButton.setShortcut(_translate("editFilterDialog", "-"))
        self.pasteWorkingRowButton.setText(_translate("editFilterDialog", "..."))
        self.pasteWorkingRowButton.setShortcut(_translate("editFilterDialog", "V"))
        self.importWorkingButton.setText(_translate("editFilterDialog", "..."))
        self.orderLabel.setText(_translate("editFilterDialog", "Order"))
        self.addSnapshotRowButton.setText(_translate("editFilterDialog", "..."))
        self.removeSnapshotRowButton.setText(_translate("editFilterDialog", "..."))
        self.pasteSnapshotRowButton.setText(_translate("editFilterDialog", "..."))
        self.importSnapshotButton.setText(_translate("editFilterDialog", "..."))
        self.sStepButton.setText(_translate("editFilterDialog", "..."))
        self.filterQLabel.setText(_translate("editFilterDialog", "Q"))
        self.optimiseLabel.setText(_translate("editFilterDialog", "Optimise"))
        self.optimiseButton.setText(_translate("editFilterDialog", "..."))
        self.saveButton.setShortcut(_translate("editFilterDialog", "Return"))
        self.exitButton.setText(_translate("editFilterDialog", "..."))
        self.ltOutLabel.setText(_translate("editFilterDialog", "F(p) / Q(p)"))
        self.gainStepButton.setText(_translate("editFilterDialog", "..."))
        self.sLabel.setText(_translate("editFilterDialog", "S"))
        self.addWorkingPeakingButton.setText(_translate("editFilterDialog", "PEQ"))
        self.addWorkingPeakingButton.setShortcut(_translate("editFilterDialog", "Ctrl+Alt+1"))
        self.addWorkingLowShelfButton.setText(_translate("editFilterDialog", "LS"))
        self.addWorkingLowShelfButton.setShortcut(_translate("editFilterDialog", "Ctrl+Alt+2"))
        self.addWorkingHighShelfButton.setText(_translate("editFilterDialog", "HS"))
        self.addWorkingHighShelfButton.setShortcut(_translate("editFilterDialog", "Ctrl+Alt+3"))
        self.showIndividual.setText(_translate("editFilterDialog", "Show Individual Filters"))
        self.showPhase.setText(_translate("editFilterDialog", "Show Phase Response"))
from app import NoFillDoubleSpinBox
from mpl import MplWidget
