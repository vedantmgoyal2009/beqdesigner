# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui',
# licensing of 'analysis.ui' applies.
#
# Created: Sun Jun 30 22:06:38 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_analysisDialog(object):
    def setupUi(self, analysisDialog):
        analysisDialog.setObjectName("analysisDialog")
        analysisDialog.resize(1494, 895)
        analysisDialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(analysisDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.analysisGridLayout = QtWidgets.QGridLayout()
        self.analysisGridLayout.setObjectName("analysisGridLayout")
        self.analysisFrame = QtWidgets.QFrame(analysisDialog)
        self.analysisFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.analysisFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.analysisFrame.setObjectName("analysisFrame")
        self.formLayout = QtWidgets.QGridLayout(self.analysisFrame)
        self.formLayout.setObjectName("formLayout")
        self.line = QtWidgets.QFrame(self.analysisFrame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.addWidget(self.line, 5, 1, 1, 2)
        self.copyFilter = QtWidgets.QComboBox(self.analysisFrame)
        self.copyFilter.setObjectName("copyFilter")
        self.formLayout.addWidget(self.copyFilter, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.analysisFrame)
        self.label.setObjectName("label")
        self.formLayout.addWidget(self.label, 6, 1, 1, 1)
        self.file = QtWidgets.QLineEdit(self.analysisFrame)
        self.file.setEnabled(False)
        self.file.setObjectName("file")
        self.formLayout.addWidget(self.file, 0, 2, 1, 1)
        self.startTime = QtWidgets.QTimeEdit(self.analysisFrame)
        self.startTime.setObjectName("startTime")
        self.formLayout.addWidget(self.startTime, 2, 2, 1, 1)
        self.loadButton = QtWidgets.QPushButton(self.analysisFrame)
        self.loadButton.setObjectName("loadButton")
        self.formLayout.addWidget(self.loadButton, 4, 1, 1, 3)
        self.endLabel = QtWidgets.QLabel(self.analysisFrame)
        self.endLabel.setObjectName("endLabel")
        self.formLayout.addWidget(self.endLabel, 3, 1, 1, 1)
        self.fileLabel = QtWidgets.QLabel(self.analysisFrame)
        self.fileLabel.setObjectName("fileLabel")
        self.formLayout.addWidget(self.fileLabel, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.addItem(spacerItem, 10, 1, 1, 3)
        self.channelSelectorLabel = QtWidgets.QLabel(self.analysisFrame)
        self.channelSelectorLabel.setObjectName("channelSelectorLabel")
        self.formLayout.addWidget(self.channelSelectorLabel, 1, 1, 1, 1)
        self.endTime = QtWidgets.QTimeEdit(self.analysisFrame)
        self.endTime.setObjectName("endTime")
        self.formLayout.addWidget(self.endTime, 3, 2, 1, 1)
        self.filePicker = QtWidgets.QToolButton(self.analysisFrame)
        self.filePicker.setObjectName("filePicker")
        self.formLayout.addWidget(self.filePicker, 0, 3, 1, 1)
        self.channelSelector = QtWidgets.QComboBox(self.analysisFrame)
        self.channelSelector.setObjectName("channelSelector")
        self.formLayout.addWidget(self.channelSelector, 1, 2, 1, 1)
        self.startLabel = QtWidgets.QLabel(self.analysisFrame)
        self.startLabel.setObjectName("startLabel")
        self.formLayout.addWidget(self.startLabel, 2, 1, 1, 1)
        self.analysisGridLayout.addWidget(self.analysisFrame, 0, 0, 1, 1)
        self.analysisTabs = QtWidgets.QTabWidget(analysisDialog)
        self.analysisTabs.setObjectName("analysisTabs")
        self.spectrumTab = QtWidgets.QWidget()
        self.spectrumTab.setObjectName("spectrumTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.spectrumTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spectrumControlsLayout = QtWidgets.QGridLayout()
        self.spectrumControlsLayout.setObjectName("spectrumControlsLayout")
        self.buttonBoxLayout = QtWidgets.QVBoxLayout()
        self.buttonBoxLayout.setObjectName("buttonBoxLayout")
        self.saveChart = QtWidgets.QPushButton(self.spectrumTab)
        self.saveChart.setObjectName("saveChart")
        self.buttonBoxLayout.addWidget(self.saveChart)
        self.updateChart = QtWidgets.QPushButton(self.spectrumTab)
        self.updateChart.setObjectName("updateChart")
        self.buttonBoxLayout.addWidget(self.updateChart)
        self.saveLayout = QtWidgets.QPushButton(self.spectrumTab)
        self.saveLayout.setObjectName("saveLayout")
        self.buttonBoxLayout.addWidget(self.saveLayout)
        self.spectrumControlsLayout.addLayout(self.buttonBoxLayout, 0, 10, 3, 1)
        self.colourRangeLabel = QtWidgets.QLabel(self.spectrumTab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.colourRangeLabel.setFont(font)
        self.colourRangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.colourRangeLabel.setObjectName("colourRangeLabel")
        self.spectrumControlsLayout.addWidget(self.colourRangeLabel, 0, 7, 1, 1)
        self.colourLowerLimit = QtWidgets.QSpinBox(self.spectrumTab)
        self.colourLowerLimit.setMinimum(-120)
        self.colourLowerLimit.setMaximum(0)
        self.colourLowerLimit.setProperty("value", -70)
        self.colourLowerLimit.setObjectName("colourLowerLimit")
        self.spectrumControlsLayout.addWidget(self.colourLowerLimit, 2, 7, 1, 1)
        self.colourUpperLimit = QtWidgets.QSpinBox(self.spectrumTab)
        self.colourUpperLimit.setMinimum(-99)
        self.colourUpperLimit.setMaximum(0)
        self.colourUpperLimit.setProperty("value", -10)
        self.colourUpperLimit.setObjectName("colourUpperLimit")
        self.spectrumControlsLayout.addWidget(self.colourUpperLimit, 1, 7, 1, 1)
        self.markerType = QtWidgets.QComboBox(self.spectrumTab)
        self.markerType.setObjectName("markerType")
        self.spectrumControlsLayout.addWidget(self.markerType, 0, 1, 1, 1)
        self.magLimitTypeLabel = QtWidgets.QLabel(self.spectrumTab)
        self.magLimitTypeLabel.setObjectName("magLimitTypeLabel")
        self.spectrumControlsLayout.addWidget(self.magLimitTypeLabel, 2, 0, 1, 1)
        self.markerTypeLabel = QtWidgets.QLabel(self.spectrumTab)
        self.markerTypeLabel.setObjectName("markerTypeLabel")
        self.spectrumControlsLayout.addWidget(self.markerTypeLabel, 0, 0, 1, 1)
        self.analysisResolutionLabel = QtWidgets.QLabel(self.spectrumTab)
        self.analysisResolutionLabel.setObjectName("analysisResolutionLabel")
        self.spectrumControlsLayout.addWidget(self.analysisResolutionLabel, 1, 0, 1, 1)
        self.analysisResolution = QtWidgets.QComboBox(self.spectrumTab)
        self.analysisResolution.setObjectName("analysisResolution")
        self.spectrumControlsLayout.addWidget(self.analysisResolution, 1, 1, 1, 1)
        self.markerSize = QtWidgets.QSpinBox(self.spectrumTab)
        self.markerSize.setMinimum(1)
        self.markerSize.setMaximum(9)
        self.markerSize.setObjectName("markerSize")
        self.spectrumControlsLayout.addWidget(self.markerSize, 0, 3, 1, 1)
        self.magLimitType = QtWidgets.QComboBox(self.spectrumTab)
        self.magLimitType.setObjectName("magLimitType")
        self.magLimitType.addItem("")
        self.magLimitType.addItem("")
        self.magLimitType.addItem("")
        self.spectrumControlsLayout.addWidget(self.magLimitType, 2, 1, 1, 1)
        self.markerSizeLabel = QtWidgets.QLabel(self.spectrumTab)
        self.markerSizeLabel.setObjectName("markerSizeLabel")
        self.spectrumControlsLayout.addWidget(self.markerSizeLabel, 0, 2, 1, 1)
        self.ellipseWidthLabel = QtWidgets.QLabel(self.spectrumTab)
        self.ellipseWidthLabel.setObjectName("ellipseWidthLabel")
        self.spectrumControlsLayout.addWidget(self.ellipseWidthLabel, 1, 2, 1, 1)
        self.ellipseHeight = QtWidgets.QDoubleSpinBox(self.spectrumTab)
        self.ellipseHeight.setMinimum(0.01)
        self.ellipseHeight.setMaximum(100.0)
        self.ellipseHeight.setSingleStep(0.01)
        self.ellipseHeight.setProperty("value", 1.0)
        self.ellipseHeight.setObjectName("ellipseHeight")
        self.spectrumControlsLayout.addWidget(self.ellipseHeight, 2, 3, 1, 1)
        self.ellipseWidth = QtWidgets.QDoubleSpinBox(self.spectrumTab)
        self.ellipseWidth.setMinimum(0.01)
        self.ellipseWidth.setMaximum(100.0)
        self.ellipseWidth.setSingleStep(0.01)
        self.ellipseWidth.setProperty("value", 3.0)
        self.ellipseWidth.setObjectName("ellipseWidth")
        self.spectrumControlsLayout.addWidget(self.ellipseWidth, 1, 3, 1, 1)
        self.ellipseHeightLabel = QtWidgets.QLabel(self.spectrumTab)
        self.ellipseHeightLabel.setObjectName("ellipseHeightLabel")
        self.spectrumControlsLayout.addWidget(self.ellipseHeightLabel, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spectrumControlsLayout.addItem(spacerItem1, 0, 9, 3, 1)
        self.minTime = QtWidgets.QTimeEdit(self.spectrumTab)
        self.minTime.setObjectName("minTime")
        self.spectrumControlsLayout.addWidget(self.minTime, 1, 5, 1, 1)
        self.magLowerLimit = QtWidgets.QDoubleSpinBox(self.spectrumTab)
        self.magLowerLimit.setMinimum(-120.0)
        self.magLowerLimit.setMaximum(0.0)
        self.magLowerLimit.setSingleStep(0.01)
        self.magLowerLimit.setProperty("value", -70.0)
        self.magLowerLimit.setObjectName("magLowerLimit")
        self.spectrumControlsLayout.addWidget(self.magLowerLimit, 2, 8, 1, 1)
        self.signalRangeLabel = QtWidgets.QLabel(self.spectrumTab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.signalRangeLabel.setFont(font)
        self.signalRangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signalRangeLabel.setObjectName("signalRangeLabel")
        self.spectrumControlsLayout.addWidget(self.signalRangeLabel, 0, 8, 1, 1)
        self.magUpperLimit = QtWidgets.QDoubleSpinBox(self.spectrumTab)
        self.magUpperLimit.setEnabled(False)
        self.magUpperLimit.setDecimals(2)
        self.magUpperLimit.setMinimum(-99.0)
        self.magUpperLimit.setMaximum(0.0)
        self.magUpperLimit.setSingleStep(0.001)
        self.magUpperLimit.setProperty("value", -10.0)
        self.magUpperLimit.setObjectName("magUpperLimit")
        self.spectrumControlsLayout.addWidget(self.magUpperLimit, 1, 8, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maxFilteredFreq = QtWidgets.QSpinBox(self.spectrumTab)
        self.maxFilteredFreq.setMinimum(1)
        self.maxFilteredFreq.setMaximum(24000)
        self.maxFilteredFreq.setProperty("value", 40)
        self.maxFilteredFreq.setObjectName("maxFilteredFreq")
        self.horizontalLayout.addWidget(self.maxFilteredFreq)
        self.maxUnfilteredFreq = QtWidgets.QSpinBox(self.spectrumTab)
        self.maxUnfilteredFreq.setMinimum(10)
        self.maxUnfilteredFreq.setMaximum(24000)
        self.maxUnfilteredFreq.setProperty("value", 80)
        self.maxUnfilteredFreq.setObjectName("maxUnfilteredFreq")
        self.horizontalLayout.addWidget(self.maxUnfilteredFreq)
        self.spectrumControlsLayout.addLayout(self.horizontalLayout, 2, 6, 1, 1)
        self.timeRangeLabe = QtWidgets.QLabel(self.spectrumTab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.timeRangeLabe.setFont(font)
        self.timeRangeLabe.setAlignment(QtCore.Qt.AlignCenter)
        self.timeRangeLabe.setObjectName("timeRangeLabe")
        self.spectrumControlsLayout.addWidget(self.timeRangeLabe, 0, 5, 1, 1)
        self.minLabel = QtWidgets.QLabel(self.spectrumTab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.minLabel.setFont(font)
        self.minLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.minLabel.setObjectName("minLabel")
        self.spectrumControlsLayout.addWidget(self.minLabel, 1, 4, 1, 1)
        self.freqRangeLabel = QtWidgets.QLabel(self.spectrumTab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.freqRangeLabel.setFont(font)
        self.freqRangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.freqRangeLabel.setObjectName("freqRangeLabel")
        self.spectrumControlsLayout.addWidget(self.freqRangeLabel, 0, 6, 1, 1)
        self.maxTime = QtWidgets.QTimeEdit(self.spectrumTab)
        self.maxTime.setObjectName("maxTime")
        self.spectrumControlsLayout.addWidget(self.maxTime, 2, 5, 1, 1)
        self.minFreq = QtWidgets.QSpinBox(self.spectrumTab)
        self.minFreq.setObjectName("minFreq")
        self.spectrumControlsLayout.addWidget(self.minFreq, 1, 6, 1, 1)
        self.maxLabel = QtWidgets.QLabel(self.spectrumTab)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.maxLabel.setFont(font)
        self.maxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.maxLabel.setObjectName("maxLabel")
        self.spectrumControlsLayout.addWidget(self.maxLabel, 2, 4, 1, 1)
        self.gridLayout_3.addLayout(self.spectrumControlsLayout, 0, 0, 1, 1)
        self.spectrumChart = MplWidget(self.spectrumTab)
        self.spectrumChart.setObjectName("spectrumChart")
        self.gridLayout_3.addWidget(self.spectrumChart, 3, 0, 1, 1)
        self.analysisTabs.addTab(self.spectrumTab, "")
        self.waveformTab = QtWidgets.QWidget()
        self.waveformTab.setObjectName("waveformTab")
        self.gridLayout = QtWidgets.QGridLayout(self.waveformTab)
        self.gridLayout.setObjectName("gridLayout")
        self.waveformChart = MplWidget(self.waveformTab)
        self.waveformChart.setObjectName("waveformChart")
        self.gridLayout.addWidget(self.waveformChart, 1, 0, 1, 1)
        self.waveformControls = QtWidgets.QGridLayout()
        self.waveformControls.setObjectName("waveformControls")
        self.magnitudeDecibels = QtWidgets.QCheckBox(self.waveformTab)
        self.magnitudeDecibels.setObjectName("magnitudeDecibels")
        self.waveformControls.addWidget(self.magnitudeDecibels, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.waveformControls.addItem(spacerItem2, 0, 4, 1, 1)
        self.headroomLabel = QtWidgets.QLabel(self.waveformTab)
        self.headroomLabel.setObjectName("headroomLabel")
        self.waveformControls.addWidget(self.headroomLabel, 0, 1, 1, 1)
        self.headroom = QtWidgets.QDoubleSpinBox(self.waveformTab)
        self.headroom.setEnabled(True)
        self.headroom.setDecimals(3)
        self.headroom.setMinimum(-100.0)
        self.headroom.setMaximum(100.0)
        self.headroom.setSingleStep(0.001)
        self.headroom.setObjectName("headroom")
        self.waveformControls.addWidget(self.headroom, 0, 2, 1, 1)
        self.showLimitsButton = QtWidgets.QToolButton(self.waveformTab)
        self.showLimitsButton.setObjectName("showLimitsButton")
        self.waveformControls.addWidget(self.showLimitsButton, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.waveformControls, 0, 0, 1, 1)
        self.analysisTabs.addTab(self.waveformTab, "")
        self.analysisGridLayout.addWidget(self.analysisTabs, 0, 1, 2, 1)
        self.signalFrame = QtWidgets.QFrame(analysisDialog)
        self.signalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.signalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.signalFrame.setObjectName("signalFrame")
        self.signalLayout = QtWidgets.QGridLayout(self.signalFrame)
        self.signalLayout.setObjectName("signalLayout")
        self.leftSignal = QtWidgets.QComboBox(self.signalFrame)
        self.leftSignal.setObjectName("leftSignal")
        self.signalLayout.addWidget(self.leftSignal, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.signalLayout.addItem(spacerItem3, 3, 0, 1, 2)
        self.rightSignal = QtWidgets.QComboBox(self.signalFrame)
        self.rightSignal.setObjectName("rightSignal")
        self.signalLayout.addWidget(self.rightSignal, 1, 1, 1, 1)
        self.leftSignalLabel = QtWidgets.QLabel(self.signalFrame)
        self.leftSignalLabel.setObjectName("leftSignalLabel")
        self.signalLayout.addWidget(self.leftSignalLabel, 0, 0, 1, 1)
        self.rightSignalLabel = QtWidgets.QLabel(self.signalFrame)
        self.rightSignalLabel.setObjectName("rightSignalLabel")
        self.signalLayout.addWidget(self.rightSignalLabel, 1, 0, 1, 1)
        self.compareSignalsButton = QtWidgets.QPushButton(self.signalFrame)
        self.compareSignalsButton.setObjectName("compareSignalsButton")
        self.signalLayout.addWidget(self.compareSignalsButton, 2, 0, 1, 2)
        self.filterLeft = QtWidgets.QCheckBox(self.signalFrame)
        self.filterLeft.setText("")
        self.filterLeft.setObjectName("filterLeft")
        self.signalLayout.addWidget(self.filterLeft, 0, 2, 1, 1)
        self.filterRight = QtWidgets.QCheckBox(self.signalFrame)
        self.filterRight.setText("")
        self.filterRight.setObjectName("filterRight")
        self.signalLayout.addWidget(self.filterRight, 1, 2, 1, 1)
        self.signalLayout.setColumnStretch(1, 1)
        self.analysisGridLayout.addWidget(self.signalFrame, 1, 0, 1, 1)
        self.analysisGridLayout.setColumnStretch(1, 1)
        self.gridLayout_2.addLayout(self.analysisGridLayout, 0, 0, 1, 1)

        self.retranslateUi(analysisDialog)
        self.analysisTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.filePicker, QtCore.SIGNAL("clicked()"), analysisDialog.select_wav_file)
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL("clicked()"), analysisDialog.load_file)
        QtCore.QObject.connect(self.analysisTabs, QtCore.SIGNAL("currentChanged(int)"), analysisDialog.show_chart)
        QtCore.QObject.connect(self.showLimitsButton, QtCore.SIGNAL("clicked()"), analysisDialog.show_limits)
        QtCore.QObject.connect(self.magnitudeDecibels, QtCore.SIGNAL("clicked()"), analysisDialog.show_chart)
        QtCore.QObject.connect(self.magLimitType, QtCore.SIGNAL("currentIndexChanged(QString)"), analysisDialog.set_mag_range_type)
        QtCore.QObject.connect(self.copyFilter, QtCore.SIGNAL("currentIndexChanged(int)"), analysisDialog.update_filter)
        QtCore.QObject.connect(self.markerType, QtCore.SIGNAL("currentIndexChanged(QString)"), analysisDialog.update_marker_type)
        QtCore.QObject.connect(self.saveChart, QtCore.SIGNAL("clicked()"), analysisDialog.save_chart)
        QtCore.QObject.connect(self.updateChart, QtCore.SIGNAL("clicked()"), analysisDialog.update_chart)
        QtCore.QObject.connect(self.saveLayout, QtCore.SIGNAL("clicked()"), analysisDialog.save_layout)
        QtCore.QObject.connect(self.leftSignal, QtCore.SIGNAL("currentIndexChanged(QString)"), analysisDialog.enable_compare)
        QtCore.QObject.connect(self.rightSignal, QtCore.SIGNAL("currentIndexChanged(QString)"), analysisDialog.enable_compare)
        QtCore.QObject.connect(self.compareSignalsButton, QtCore.SIGNAL("clicked()"), analysisDialog.compare_signals)
        QtCore.QObject.connect(self.filterLeft, QtCore.SIGNAL("clicked()"), analysisDialog.enable_compare)
        QtCore.QObject.connect(self.filterRight, QtCore.SIGNAL("clicked()"), analysisDialog.enable_compare)
        QtCore.QMetaObject.connectSlotsByName(analysisDialog)

    def retranslateUi(self, analysisDialog):
        analysisDialog.setWindowTitle(QtWidgets.QApplication.translate("analysisDialog", "Analysis", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("analysisDialog", "Filter", None, -1))
        self.startTime.setDisplayFormat(QtWidgets.QApplication.translate("analysisDialog", "HH:mm:ss.zzz", None, -1))
        self.loadButton.setText(QtWidgets.QApplication.translate("analysisDialog", "Load", None, -1))
        self.endLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "End", None, -1))
        self.fileLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "File", None, -1))
        self.channelSelectorLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Channel", None, -1))
        self.endTime.setDisplayFormat(QtWidgets.QApplication.translate("analysisDialog", "HH:mm:ss.zzz", None, -1))
        self.filePicker.setText(QtWidgets.QApplication.translate("analysisDialog", "...", None, -1))
        self.startLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Start", None, -1))
        self.saveChart.setText(QtWidgets.QApplication.translate("analysisDialog", "Save Chart", None, -1))
        self.updateChart.setText(QtWidgets.QApplication.translate("analysisDialog", "Update", None, -1))
        self.saveLayout.setText(QtWidgets.QApplication.translate("analysisDialog", "Save Layout", None, -1))
        self.colourRangeLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Colour", None, -1))
        self.magLimitTypeLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Filter Type", None, -1))
        self.markerTypeLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Type", None, -1))
        self.analysisResolutionLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Resolution", None, -1))
        self.magLimitType.setItemText(0, QtWidgets.QApplication.translate("analysisDialog", "Constant", None, -1))
        self.magLimitType.setItemText(1, QtWidgets.QApplication.translate("analysisDialog", "Peak", None, -1))
        self.magLimitType.setItemText(2, QtWidgets.QApplication.translate("analysisDialog", "Average", None, -1))
        self.markerSizeLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Marker Size", None, -1))
        self.ellipseWidthLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Ellipse Width", None, -1))
        self.ellipseHeightLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Ellipse Height", None, -1))
        self.minTime.setDisplayFormat(QtWidgets.QApplication.translate("analysisDialog", "HH:mm:ss", None, -1))
        self.signalRangeLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Signal", None, -1))
        self.timeRangeLabe.setText(QtWidgets.QApplication.translate("analysisDialog", "Time", None, -1))
        self.minLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Min", None, -1))
        self.freqRangeLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Freq", None, -1))
        self.maxTime.setDisplayFormat(QtWidgets.QApplication.translate("analysisDialog", "HH:mm:ss", None, -1))
        self.maxLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Max", None, -1))
        self.analysisTabs.setTabText(self.analysisTabs.indexOf(self.spectrumTab), QtWidgets.QApplication.translate("analysisDialog", "Peak Spectrum", None, -1))
        self.magnitudeDecibels.setText(QtWidgets.QApplication.translate("analysisDialog", "Waveform in dBFS?", None, -1))
        self.headroomLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Headroom (dB)", None, -1))
        self.showLimitsButton.setText(QtWidgets.QApplication.translate("analysisDialog", "...", None, -1))
        self.analysisTabs.setTabText(self.analysisTabs.indexOf(self.waveformTab), QtWidgets.QApplication.translate("analysisDialog", "Waveform", None, -1))
        self.leftSignalLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Left", None, -1))
        self.rightSignalLabel.setText(QtWidgets.QApplication.translate("analysisDialog", "Right", None, -1))
        self.compareSignalsButton.setText(QtWidgets.QApplication.translate("analysisDialog", "Compare", None, -1))

from mpl import MplWidget
