# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agilent2DicomQt2.ui'
#
# Created: Tue Sep 15 16:30:25 2015
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1321, 872)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_fdf_2 = QtGui.QWidget()
        self.tab_fdf_2.setObjectName("tab_fdf_2")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_fdf_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_changefdf = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_changefdf.setObjectName("pushButton_changefdf")
        self.gridLayout_4.addWidget(self.pushButton_changefdf, 0, 4, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_fdf_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab_fdf_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_fdf_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 1, 1, 1)
        self.pushButton_changedicom = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_changedicom.setObjectName("pushButton_changedicom")
        self.gridLayout_4.addWidget(self.pushButton_changedicom, 1, 4, 1, 1)
        self.lineEdit_darisid = QtGui.QLineEdit(self.tab_fdf_2)
        self.lineEdit_darisid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_darisid.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_darisid.setObjectName("lineEdit_darisid")
        self.gridLayout_4.addWidget(self.lineEdit_darisid, 2, 3, 1, 1)
        self.lineEdit_fdfpath = QtGui.QLineEdit(self.tab_fdf_2)
        self.lineEdit_fdfpath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_fdfpath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_fdfpath.setObjectName("lineEdit_fdfpath")
        self.gridLayout_4.addWidget(self.lineEdit_fdfpath, 0, 3, 1, 1)
        self.lineEdit_dicompath = QtGui.QLineEdit(self.tab_fdf_2)
        self.lineEdit_dicompath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_dicompath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_dicompath.setObjectName("lineEdit_dicompath")
        self.gridLayout_4.addWidget(self.lineEdit_dicompath, 1, 3, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 5, 3, 1, 1)
        self.Multiecho_2 = QtGui.QTabWidget(self.tab_fdf_2)
        self.Multiecho_2.setEnabled(True)
        self.Multiecho_2.setObjectName("Multiecho_2")
        self.tab_generic_2 = QtGui.QWidget()
        self.tab_generic_2.setObjectName("tab_generic_2")
        self.layoutWidget = QtGui.QWidget(self.tab_generic_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 173, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_7 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.checkBox_debugging = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_debugging.setObjectName("checkBox_debugging")
        self.gridLayout_7.addWidget(self.checkBox_debugging, 0, 0, 1, 1)
        self.checkBox_nodcmulti = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_nodcmulti.setObjectName("checkBox_nodcmulti")
        self.gridLayout_7.addWidget(self.checkBox_nodcmulti, 1, 0, 1, 1)
        self.Multiecho_2.addTab(self.tab_generic_2, "")
        self.gridLayout_4.addWidget(self.Multiecho_2, 4, 3, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.tab_fdf_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 172, 35))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_15 = QtGui.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.FDFprocparInfo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.FDFprocparInfo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.FDFprocparInfo.setObjectName("FDFprocparInfo")
        self.verticalLayout_15.addWidget(self.FDFprocparInfo)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 3, 3, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_convert = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.verticalLayout_4.addWidget(self.pushButton_convert)
        self.pushButton_check = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_check.setEnabled(False)
        self.pushButton_check.setObjectName("pushButton_check")
        self.verticalLayout_4.addWidget(self.pushButton_check)
        self.pushButton_view = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_view.setEnabled(False)
        self.pushButton_view.setObjectName("pushButton_view")
        self.verticalLayout_4.addWidget(self.pushButton_view)
        self.pushButton_send2daris = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_send2daris.setEnabled(False)
        self.pushButton_send2daris.setObjectName("pushButton_send2daris")
        self.verticalLayout_4.addWidget(self.pushButton_send2daris)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 4, 4, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_fdf_2, "")
        self.tab_fid_2 = QtGui.QWidget()
        self.tab_fid_2.setObjectName("tab_fid_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_fid_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_22 = QtGui.QLabel(self.tab_fid_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_11.addWidget(self.label_22, 2, 1, 1, 1)
        self.pushButton_changefid = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_changefid.setObjectName("pushButton_changefid")
        self.gridLayout_11.addWidget(self.pushButton_changefid, 0, 3, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_fid_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_11.addWidget(self.label_24, 0, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_fid_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_11.addWidget(self.label_27, 1, 1, 1, 1)
        self.pushButton_changedicom2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_changedicom2.setObjectName("pushButton_changedicom2")
        self.gridLayout_11.addWidget(self.pushButton_changedicom2, 1, 3, 1, 1)
        self.lineEdit_darisid2 = QtGui.QLineEdit(self.tab_fid_2)
        self.lineEdit_darisid2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_darisid2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_darisid2.setObjectName("lineEdit_darisid2")
        self.gridLayout_11.addWidget(self.lineEdit_darisid2, 2, 2, 1, 1)
        self.lineEdit_fidpath = QtGui.QLineEdit(self.tab_fid_2)
        self.lineEdit_fidpath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_fidpath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_fidpath.setObjectName("lineEdit_fidpath")
        self.gridLayout_11.addWidget(self.lineEdit_fidpath, 0, 2, 1, 1)
        self.lineEdit_dicompath2 = QtGui.QLineEdit(self.tab_fid_2)
        self.lineEdit_dicompath2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_dicompath2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_dicompath2.setObjectName("lineEdit_dicompath2")
        self.gridLayout_11.addWidget(self.lineEdit_dicompath2, 1, 2, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_convertfid = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_convertfid.setObjectName("pushButton_convertfid")
        self.verticalLayout_5.addWidget(self.pushButton_convertfid)
        self.pushButton_check2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_check2.setEnabled(False)
        self.pushButton_check2.setObjectName("pushButton_check2")
        self.verticalLayout_5.addWidget(self.pushButton_check2)
        self.pushButton_view2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_view2.setEnabled(False)
        self.pushButton_view2.setObjectName("pushButton_view2")
        self.verticalLayout_5.addWidget(self.pushButton_view2)
        self.pushButton_send2daris2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_send2daris2.setEnabled(False)
        self.pushButton_send2daris2.setObjectName("pushButton_send2daris2")
        self.verticalLayout_5.addWidget(self.pushButton_send2daris2)
        self.gridLayout_11.addLayout(self.verticalLayout_5, 4, 3, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_fid_2)
        self.tabWidget_3.setEnabled(True)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.tab_7)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.checkBox_magn = QtGui.QCheckBox(self.tab_7)
        self.checkBox_magn.setEnabled(True)
        self.checkBox_magn.setCheckable(True)
        self.checkBox_magn.setChecked(True)
        self.checkBox_magn.setObjectName("checkBox_magn")
        self.horizontalLayout_35.addWidget(self.checkBox_magn)
        self.checkBox_pha = QtGui.QCheckBox(self.tab_7)
        self.checkBox_pha.setObjectName("checkBox_pha")
        self.horizontalLayout_35.addWidget(self.checkBox_pha)
        self.gridLayout_2.addLayout(self.horizontalLayout_35, 5, 0, 1, 1)
        self.line = QtGui.QFrame(self.tab_7)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 8, 0, 1, 1)
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.checkBox_reimag = QtGui.QCheckBox(self.tab_7)
        self.checkBox_reimag.setObjectName("checkBox_reimag")
        self.horizontalLayout_36.addWidget(self.checkBox_reimag)
        self.checkBox_ksp = QtGui.QCheckBox(self.tab_7)
        self.checkBox_ksp.setObjectName("checkBox_ksp")
        self.horizontalLayout_36.addWidget(self.checkBox_ksp)
        self.gridLayout_2.addLayout(self.horizontalLayout_36, 6, 0, 1, 1)
        self.checkBox_nifti = QtGui.QCheckBox(self.tab_7)
        self.checkBox_nifti.setObjectName("checkBox_nifti")
        self.gridLayout_2.addWidget(self.checkBox_nifti, 7, 0, 1, 1)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.checkBox_reimag_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_reimag_raw.setObjectName("checkBox_reimag_raw")
        self.horizontalLayout_37.addWidget(self.checkBox_reimag_raw)
        self.checkBox_ksp_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_ksp_raw.setObjectName("checkBox_ksp_raw")
        self.horizontalLayout_37.addWidget(self.checkBox_ksp_raw)
        self.gridLayout_2.addLayout(self.horizontalLayout_37, 3, 0, 1, 1)
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.checkBox_magn_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_magn_raw.setEnabled(True)
        self.checkBox_magn_raw.setCheckable(True)
        self.checkBox_magn_raw.setChecked(True)
        self.checkBox_magn_raw.setObjectName("checkBox_magn_raw")
        self.horizontalLayout_38.addWidget(self.checkBox_magn_raw)
        self.checkBox_pha_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_pha_raw.setObjectName("checkBox_pha_raw")
        self.horizontalLayout_38.addWidget(self.checkBox_pha_raw)
        self.gridLayout_2.addLayout(self.horizontalLayout_38, 2, 0, 1, 1)
        self.label_36 = QtGui.QLabel(self.tab_7)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_38 = QtGui.QLabel(self.tab_7)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 1, 0, 1, 1)
        self.verticalLayout_22.addLayout(self.gridLayout_2)
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.gridLayout_13.addLayout(self.horizontalLayout_29, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_kspgaussian = QtGui.QCheckBox(self.tab_2)
        self.checkBox_kspgaussian.setObjectName("checkBox_kspgaussian")
        self.horizontalLayout_4.addWidget(self.checkBox_kspgaussian)
        self.checkBox_kspgaussshift = QtGui.QCheckBox(self.tab_2)
        self.checkBox_kspgaussshift.setObjectName("checkBox_kspgaussshift")
        self.horizontalLayout_4.addWidget(self.checkBox_kspgaussshift)
        self.checkBox_kspgauss_super = QtGui.QCheckBox(self.tab_2)
        self.checkBox_kspgauss_super.setObjectName("checkBox_kspgauss_super")
        self.horizontalLayout_4.addWidget(self.checkBox_kspgauss_super)
        self.gridLayout_13.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_39 = QtGui.QLabel(self.tab_2)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_40.addWidget(self.label_39)
        spacerItem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem)
        self.lineEdit_gfsigma = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_gfsigma.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_gfsigma.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_gfsigma.setObjectName("lineEdit_gfsigma")
        self.horizontalLayout_40.addWidget(self.lineEdit_gfsigma)
        self.comboBox_kspgauss_sigunit = QtGui.QComboBox(self.tab_2)
        self.comboBox_kspgauss_sigunit.setObjectName(
            "comboBox_kspgauss_sigunit")
        self.comboBox_kspgauss_sigunit.addItem("")
        self.comboBox_kspgauss_sigunit.addItem("")
        self.comboBox_kspgauss_sigunit.addItem("")
        self.horizontalLayout_40.addWidget(self.comboBox_kspgauss_sigunit)
        self.gridLayout_13.addLayout(self.horizontalLayout_40, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.gridLayout_13.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem2, 4, 0, 1, 1)
        self.radioButton_16 = QtGui.QRadioButton(self.tab_2)
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout_13.addWidget(self.radioButton_16, 3, 0, 1, 1)
        self.verticalLayout_16.addLayout(self.gridLayout_13)
        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.checkBox_kspepa = QtGui.QCheckBox(self.tab)
        self.checkBox_kspepa.setObjectName("checkBox_kspepa")
        self.horizontalLayout_9.addWidget(self.checkBox_kspepa)
        self.checkBox_kspepashift = QtGui.QCheckBox(self.tab)
        self.checkBox_kspepashift.setObjectName("checkBox_kspepashift")
        self.horizontalLayout_9.addWidget(self.checkBox_kspepashift)
        self.checkBox_kspepa_super = QtGui.QCheckBox(self.tab)
        self.checkBox_kspepa_super.setObjectName("checkBox_kspepa_super")
        self.horizontalLayout_9.addWidget(self.checkBox_kspepa_super)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.lineEdit_kspepa_band = QtGui.QLineEdit(self.tab)
        self.lineEdit_kspepa_band.setObjectName("lineEdit_kspepa_band")
        self.horizontalLayout_7.addWidget(self.lineEdit_kspepa_band)
        self.comboBox_kspepa_scaleunit = QtGui.QComboBox(self.tab)
        self.comboBox_kspepa_scaleunit.setObjectName(
            "comboBox_kspepa_scaleunit")
        self.comboBox_kspepa_scaleunit.addItem("")
        self.comboBox_kspepa_scaleunit.addItem("")
        self.comboBox_kspepa_scaleunit.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_kspepa_scaleunit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButton_15 = QtGui.QRadioButton(self.tab)
        self.radioButton_15.setObjectName("radioButton_15")
        self.horizontalLayout_8.addWidget(self.radioButton_15)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem4 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.gridLayout_12.addLayout(self.horizontalLayout_28, 2, 1, 1, 1)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_30 = QtGui.QLabel(self.tab_3)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_32.addWidget(self.label_30)
        spacerItem5 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem5)
        self.lineEdit_gorder = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_gorder.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_gorder.setObjectName("lineEdit_gorder")
        self.horizontalLayout_32.addWidget(self.lineEdit_gorder)
        self.gridLayout_12.addLayout(self.horizontalLayout_32, 3, 0, 1, 1)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_31 = QtGui.QLabel(self.tab_3)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_33.addWidget(self.label_31)
        spacerItem6 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem6)
        self.lineEdit_gsigma = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_gsigma.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_gsigma.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_gsigma.setObjectName("lineEdit_gsigma")
        self.horizontalLayout_33.addWidget(self.lineEdit_gsigma)
        self.comboBox_gauss_sigmascale = QtGui.QComboBox(self.tab_3)
        self.comboBox_gauss_sigmascale.setObjectName(
            "comboBox_gauss_sigmascale")
        self.comboBox_gauss_sigmascale.addItem("")
        self.comboBox_gauss_sigmascale.addItem("")
        self.comboBox_gauss_sigmascale.addItem("")
        self.horizontalLayout_33.addWidget(self.comboBox_gauss_sigmascale)
        self.gridLayout_12.addLayout(self.horizontalLayout_33, 2, 0, 1, 1)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_32 = QtGui.QLabel(self.tab_3)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_34.addWidget(self.label_32)
        self.reflect = QtGui.QRadioButton(self.tab_3)
        self.reflect.setChecked(True)
        self.reflect.setObjectName("reflect")
        self.horizontalLayout_34.addWidget(self.reflect)
        self.nearest = QtGui.QRadioButton(self.tab_3)
        self.nearest.setChecked(False)
        self.nearest.setObjectName("nearest")
        self.horizontalLayout_34.addWidget(self.nearest)
        self.wrap = QtGui.QRadioButton(self.tab_3)
        self.wrap.setObjectName("wrap")
        self.horizontalLayout_34.addWidget(self.wrap)
        self.mirror = QtGui.QRadioButton(self.tab_3)
        self.mirror.setObjectName("mirror")
        self.horizontalLayout_34.addWidget(self.mirror)
        spacerItem7 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem7)
        self.gridLayout_12.addLayout(self.horizontalLayout_34, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_gaussian3D = QtGui.QCheckBox(self.tab_3)
        self.checkBox_gaussian3D.setObjectName("checkBox_gaussian3D")
        self.horizontalLayout.addWidget(self.checkBox_gaussian3D)
        self.checkBox_gaussian2D = QtGui.QCheckBox(self.tab_3)
        self.checkBox_gaussian2D.setObjectName("checkBox_gaussian2D")
        self.horizontalLayout.addWidget(self.checkBox_gaussian2D)
        self.gridLayout_12.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem8, 5, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_12)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_median = QtGui.QCheckBox(self.tab_4)
        self.checkBox_median.setObjectName("checkBox_median")
        self.verticalLayout_9.addWidget(self.checkBox_median)
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_33 = QtGui.QLabel(self.tab_4)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_41.addWidget(self.label_33)
        spacerItem9 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem9)
        self.lineEdit_median_size = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_median_size.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_median_size.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_median_size.setObjectName("lineEdit_median_size")
        self.horizontalLayout_41.addWidget(self.lineEdit_median_size)
        self.verticalLayout_9.addLayout(self.horizontalLayout_41)
        spacerItem10 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.verticalLayout_14.addLayout(self.verticalLayout_9)
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setEnabled(True)
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_wiener = QtGui.QCheckBox(self.tab_8)
        self.checkBox_wiener.setEnabled(True)
        self.checkBox_wiener.setObjectName("checkBox_wiener")
        self.verticalLayout_10.addWidget(self.checkBox_wiener)
        self.horizontalLayout_42 = QtGui.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_34 = QtGui.QLabel(self.tab_8)
        self.label_34.setEnabled(True)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_42.addWidget(self.label_34)
        spacerItem11 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem11)
        self.lineEdit_wiener_size = QtGui.QLineEdit(self.tab_8)
        self.lineEdit_wiener_size.setEnabled(True)
        self.lineEdit_wiener_size.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_wiener_size.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_wiener_size.setObjectName("lineEdit_wiener_size")
        self.horizontalLayout_42.addWidget(self.lineEdit_wiener_size)
        self.verticalLayout_10.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_43 = QtGui.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_35 = QtGui.QLabel(self.tab_8)
        self.label_35.setEnabled(True)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_43.addWidget(self.label_35)
        spacerItem12 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem12)
        self.lineEdit_wiener_noise = QtGui.QLineEdit(self.tab_8)
        self.lineEdit_wiener_noise.setEnabled(True)
        self.lineEdit_wiener_noise.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_wiener_noise.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_wiener_noise.setObjectName("lineEdit_wiener_noise")
        self.horizontalLayout_43.addWidget(self.lineEdit_wiener_noise)
        self.verticalLayout_10.addLayout(self.horizontalLayout_43)
        spacerItem13 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem13)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.gridLayout_14.addLayout(self.horizontalLayout_30, 2, 1, 1, 1)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_37 = QtGui.QLabel(self.tab_5)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_39.addWidget(self.label_37)
        spacerItem14 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem14)
        self.gridLayout_14.addLayout(self.horizontalLayout_39, 3, 0, 1, 1)
        self.horizontalLayout_45 = QtGui.QHBoxLayout()
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_41 = QtGui.QLabel(self.tab_5)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_45.addWidget(self.label_41)
        spacerItem15 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem15)
        self.lineEdit_epaband = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_epaband.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_epaband.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_epaband.setObjectName("lineEdit_epaband")
        self.horizontalLayout_45.addWidget(self.lineEdit_epaband)
        self.comboBox_epabandwidth = QtGui.QComboBox(self.tab_5)
        self.comboBox_epabandwidth.setObjectName("comboBox_epabandwidth")
        self.comboBox_epabandwidth.addItem("")
        self.comboBox_epabandwidth.addItem("")
        self.comboBox_epabandwidth.addItem("")
        self.horizontalLayout_45.addWidget(self.comboBox_epabandwidth)
        self.gridLayout_14.addLayout(self.horizontalLayout_45, 2, 0, 1, 1)
        self.horizontalLayout_46 = QtGui.QHBoxLayout()
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_42 = QtGui.QLabel(self.tab_5)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_46.addWidget(self.label_42)
        self.reflect_epa = QtGui.QRadioButton(self.tab_5)
        self.reflect_epa.setChecked(True)
        self.reflect_epa.setObjectName("reflect_epa")
        self.horizontalLayout_46.addWidget(self.reflect_epa)
        self.nearest_epa = QtGui.QRadioButton(self.tab_5)
        self.nearest_epa.setChecked(False)
        self.nearest_epa.setObjectName("nearest_epa")
        self.horizontalLayout_46.addWidget(self.nearest_epa)
        self.wrap_epa = QtGui.QRadioButton(self.tab_5)
        self.wrap_epa.setObjectName("wrap_epa")
        self.horizontalLayout_46.addWidget(self.wrap_epa)
        self.mirror_epa = QtGui.QRadioButton(self.tab_5)
        self.mirror_epa.setObjectName("mirror_epa")
        self.horizontalLayout_46.addWidget(self.mirror_epa)
        spacerItem16 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem16)
        self.gridLayout_14.addLayout(self.horizontalLayout_46, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_epanechnikov3D = QtGui.QCheckBox(self.tab_5)
        self.checkBox_epanechnikov3D.setObjectName("checkBox_epanechnikov3D")
        self.horizontalLayout_5.addWidget(self.checkBox_epanechnikov3D)
        self.checkBox_epanechnikov2D = QtGui.QCheckBox(self.tab_5)
        self.checkBox_epanechnikov2D.setEnabled(True)
        self.checkBox_epanechnikov2D.setObjectName("checkBox_epanechnikov2D")
        self.horizontalLayout_5.addWidget(self.checkBox_epanechnikov2D)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem17, 5, 0, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_14)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_stdev_cplx = QtGui.QCheckBox(self.tab_6)
        self.checkBox_stdev_cplx.setObjectName("checkBox_stdev_cplx")
        self.horizontalLayout_10.addWidget(self.checkBox_stdev_cplx)
        self.checkBox_stdev_magn = QtGui.QCheckBox(self.tab_6)
        self.checkBox_stdev_magn.setObjectName("checkBox_stdev_magn")
        self.horizontalLayout_10.addWidget(self.checkBox_stdev_magn)
        self.checkBox_stdev_phase = QtGui.QCheckBox(self.tab_6)
        self.checkBox_stdev_phase.setObjectName("checkBox_stdev_phase")
        self.horizontalLayout_10.addWidget(self.checkBox_stdev_phase)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.stdev_window_size_label = QtGui.QLabel(self.tab_6)
        self.stdev_window_size_label.setObjectName("stdev_window_size_label")
        self.horizontalLayout_11.addWidget(self.stdev_window_size_label)
        spacerItem18 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem18)
        self.stdev_window_size = QtGui.QLineEdit(self.tab_6)
        self.stdev_window_size.setObjectName("stdev_window_size")
        self.horizontalLayout_11.addWidget(self.stdev_window_size)
        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 2, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.verticalLayout_8.addWidget(self.tabWidget_3)
        self.gridLayout_11.addLayout(self.verticalLayout_8, 4, 2, 1, 1)
        self.scrollArea_4 = QtGui.QScrollArea(self.tab_fid_2)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtGui.QWidget(self.scrollArea_4)
        self.scrollAreaWidgetContents_4.setGeometry(
            QtCore.QRect(0, 0, 133, 35))
        self.scrollAreaWidgetContents_4.setObjectName(
            "scrollAreaWidgetContents_4")
        self.verticalLayout_21 = QtGui.QVBoxLayout(
            self.scrollAreaWidgetContents_4)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.FIDprocparInfo = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.FIDprocparInfo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.FIDprocparInfo.setObjectName("FIDprocparInfo")
        self.verticalLayout_21.addWidget(self.FIDprocparInfo)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.addWidget(self.scrollArea_4, 3, 2, 1, 1)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        spacerItem20 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem20)
        self.pushButton_CleanUpDicoms = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_CleanUpDicoms.setObjectName("pushButton_CleanUpDicoms")
        self.verticalLayout_18.addWidget(self.pushButton_CleanUpDicoms)
        self.gridLayout_11.addLayout(self.verticalLayout_18, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_11)
        self.tabWidget.addTab(self.tab_fid_2, "")
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.tab_9)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtGui.QLabel(self.tab_9)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_9)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_9)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_ProcOutputfolder = QtGui.QLineEdit(self.tab_9)
        self.lineEdit_ProcOutputfolder.setObjectName(
            "lineEdit_ProcOutputfolder")
        self.horizontalLayout_15.addWidget(self.lineEdit_ProcOutputfolder)
        self.pushButton_procout = QtGui.QPushButton(self.tab_9)
        self.pushButton_procout.setObjectName("pushButton_procout")
        self.horizontalLayout_15.addWidget(self.pushButton_procout)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 3, 1, 1, 1)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lineEdit_ProcInfolder2 = QtGui.QLineEdit(self.tab_9)
        self.lineEdit_ProcInfolder2.setObjectName("lineEdit_ProcInfolder2")
        self.horizontalLayout_16.addWidget(self.lineEdit_ProcInfolder2)
        self.pushButton_processfolder2 = QtGui.QPushButton(self.tab_9)
        self.pushButton_processfolder2.setObjectName(
            "pushButton_processfolder2")
        self.horizontalLayout_16.addWidget(self.pushButton_processfolder2)
        self.pushButton_ChangeNifti2 = QtGui.QPushButton(self.tab_9)
        self.pushButton_ChangeNifti2.setObjectName("pushButton_ChangeNifti2")
        self.horizontalLayout_16.addWidget(self.pushButton_ChangeNifti2)
        self.pushButton_ClearProc2 = QtGui.QPushButton(self.tab_9)
        self.pushButton_ClearProc2.setObjectName("pushButton_ClearProc2")
        self.horizontalLayout_16.addWidget(self.pushButton_ClearProc2)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lineEdit_ProcInfolder1 = QtGui.QLineEdit(self.tab_9)
        self.lineEdit_ProcInfolder1.setObjectName("lineEdit_ProcInfolder1")
        self.horizontalLayout_17.addWidget(self.lineEdit_ProcInfolder1)
        self.pushButton_processfolder1 = QtGui.QPushButton(self.tab_9)
        self.pushButton_processfolder1.setObjectName(
            "pushButton_processfolder1")
        self.horizontalLayout_17.addWidget(self.pushButton_processfolder1)
        self.pushButton_ChangeNifti1 = QtGui.QPushButton(self.tab_9)
        self.pushButton_ChangeNifti1.setObjectName("pushButton_ChangeNifti1")
        self.horizontalLayout_17.addWidget(self.pushButton_ChangeNifti1)
        self.pushButton_ClearProc1 = QtGui.QPushButton(self.tab_9)
        self.pushButton_ClearProc1.setObjectName("pushButton_ClearProc1")
        self.horizontalLayout_17.addWidget(self.pushButton_ClearProc1)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)
        self.tabWidget1 = QtGui.QTabWidget(self.tab_9)
        self.tabWidget1.setObjectName("tabWidget1")
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.tabWidgetPage1)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_26 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_24.addWidget(self.label_26)
        self.lineEdit_swiorder = QtGui.QLineEdit(self.tabWidgetPage1)
        self.lineEdit_swiorder.setObjectName("lineEdit_swiorder")
        self.horizontalLayout_24.addWidget(self.lineEdit_swiorder)
        spacerItem21 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem21)
        self.gridLayout_10.addLayout(self.horizontalLayout_24, 4, 0, 1, 1)
        self.checkBox_swisaveRI = QtGui.QCheckBox(self.tabWidgetPage1)
        self.checkBox_swisaveRI.setObjectName("checkBox_swisaveRI")
        self.gridLayout_10.addWidget(self.checkBox_swisaveRI, 1, 0, 1, 1)
        self.checkBox_swineg = QtGui.QCheckBox(self.tabWidgetPage1)
        self.checkBox_swineg.setChecked(True)
        self.checkBox_swineg.setObjectName("checkBox_swineg")
        self.gridLayout_10.addWidget(self.checkBox_swineg, 2, 0, 1, 1)
        self.checkBox_swipos = QtGui.QCheckBox(self.tabWidgetPage1)
        self.checkBox_swipos.setObjectName("checkBox_swipos")
        self.gridLayout_10.addWidget(self.checkBox_swipos, 3, 0, 1, 1)
        self.horizontalLayout_14.addLayout(self.gridLayout_10)
        self.gridLayout_5.addLayout(self.horizontalLayout_14, 4, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 4, 0, 1, 1)
        self.label_29 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem22 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem22)
        self.pushButton_SWI = QtGui.QPushButton(self.tabWidgetPage1)
        self.pushButton_SWI.setObjectName("pushButton_SWI")
        self.horizontalLayout_27.addWidget(self.pushButton_SWI)
        self.gridLayout_5.addLayout(self.horizontalLayout_27, 5, 1, 1, 1)
        spacerItem23 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem23, 6, 1, 1, 1)
        self.checkBox_swipreprocess = QtGui.QCheckBox(self.tabWidgetPage1)
        self.checkBox_swipreprocess.setObjectName("checkBox_swipreprocess")
        self.gridLayout_5.addWidget(self.checkBox_swipreprocess, 2, 1, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout_5)
        self.tabWidget1.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.tabWidgetPage2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_19 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 0, 0, 1, 1)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_21 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_18.addWidget(self.label_21)
        self.lineEdit_meeorder = QtGui.QLineEdit(self.tabWidgetPage2)
        self.lineEdit_meeorder.setObjectName("lineEdit_meeorder")
        self.horizontalLayout_18.addWidget(self.lineEdit_meeorder)
        spacerItem24 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem24)
        self.gridLayout_6.addLayout(self.horizontalLayout_18, 1, 1, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_meepreproc = QtGui.QCheckBox(self.tabWidgetPage2)
        self.checkBox_meepreproc.setObjectName("checkBox_meepreproc")
        self.gridLayout_9.addWidget(self.checkBox_meepreproc, 0, 0, 1, 1)
        self.checkBox_meesaveRI = QtGui.QCheckBox(self.tabWidgetPage2)
        self.checkBox_meesaveRI.setObjectName("checkBox_meesaveRI")
        self.gridLayout_9.addWidget(self.checkBox_meesaveRI, 2, 0, 1, 1)
        self.checkBox_meeswi = QtGui.QCheckBox(self.tabWidgetPage2)
        self.checkBox_meeswi.setObjectName("checkBox_meeswi")
        self.gridLayout_9.addWidget(self.checkBox_meeswi, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_9, 2, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 2, 0, 1, 1)
        self.label_47 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_47.setObjectName("label_47")
        self.gridLayout_6.addWidget(self.label_47, 1, 0, 1, 1)
        self.horizontalLayout_44 = QtGui.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        spacerItem25 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_44.addItem(spacerItem25)
        self.pushButton_MEE = QtGui.QPushButton(self.tabWidgetPage2)
        self.pushButton_MEE.setObjectName("pushButton_MEE")
        self.horizontalLayout_44.addWidget(self.pushButton_MEE)
        self.gridLayout_6.addLayout(self.horizontalLayout_44, 4, 1, 1, 1)
        spacerItem26 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem26, 5, 1, 1, 1)
        self.horizontalLayout_19.addLayout(self.gridLayout_6)
        self.tabWidget1.addTab(self.tabWidgetPage2, "")
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.tab_11)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_45 = QtGui.QLabel(self.tab_11)
        self.label_45.setObjectName("label_45")
        self.gridLayout_15.addWidget(self.label_45, 2, 0, 1, 1)
        self.horizontalLayout_47 = QtGui.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        spacerItem27 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem27)
        self.pushButton_MCI = QtGui.QPushButton(self.tab_11)
        self.pushButton_MCI.setObjectName("pushButton_MCI")
        self.horizontalLayout_47.addWidget(self.pushButton_MCI)
        self.gridLayout_15.addLayout(self.horizontalLayout_47, 4, 2, 1, 1)
        self.label_43 = QtGui.QLabel(self.tab_11)
        self.label_43.setObjectName("label_43")
        self.gridLayout_15.addWidget(self.label_43, 1, 0, 1, 1)
        self.label_48 = QtGui.QLabel(self.tab_11)
        self.label_48.setObjectName("label_48")
        self.gridLayout_15.addWidget(self.label_48, 1, 2, 1, 1)
        self.radioButton_MCI_RI = QtGui.QRadioButton(self.tab_11)
        self.radioButton_MCI_RI.setObjectName("radioButton_MCI_RI")
        self.gridLayout_15.addWidget(self.radioButton_MCI_RI, 2, 2, 1, 1)
        spacerItem28 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem28, 5, 2, 1, 1)
        self.verticalLayout_19.addLayout(self.gridLayout_15)
        self.tabWidget1.addTab(self.tab_11, "")
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.tab_10)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.radioButton_NLinputRI = QtGui.QRadioButton(self.tab_10)
        self.radioButton_NLinputRI.setObjectName("radioButton_NLinputRI")
        self.horizontalLayout_20.addWidget(self.radioButton_NLinputRI)
        self.line_6 = QtGui.QFrame(self.tab_10)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_20.addWidget(self.line_6)
        self.line_7 = QtGui.QFrame(self.tab_10)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_20.addWidget(self.line_7)
        spacerItem29 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem29)
        self.pushButton_NLpipeline1 = QtGui.QPushButton(self.tab_10)
        self.pushButton_NLpipeline1.setObjectName("pushButton_NLpipeline1")
        self.horizontalLayout_20.addWidget(self.pushButton_NLpipeline1)
        self.gridLayout_8.addLayout(self.horizontalLayout_20, 8, 1, 1, 1)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.checkBox_NLsaveRI = QtGui.QCheckBox(self.tab_10)
        self.checkBox_NLsaveRI.setObjectName("checkBox_NLsaveRI")
        self.horizontalLayout_23.addWidget(self.checkBox_NLsaveRI)
        self.checkBox_NLsavePhase = QtGui.QCheckBox(self.tab_10)
        self.checkBox_NLsavePhase.setObjectName("checkBox_NLsavePhase")
        self.horizontalLayout_23.addWidget(self.checkBox_NLsavePhase)
        self.checkBox_SaveSWIProc3 = QtGui.QCheckBox(self.tab_10)
        self.checkBox_SaveSWIProc3.setObjectName("checkBox_SaveSWIProc3")
        self.horizontalLayout_23.addWidget(self.checkBox_SaveSWIProc3)
        spacerItem30 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem30)
        self.pushButton_NLpipeline3 = QtGui.QPushButton(self.tab_10)
        self.pushButton_NLpipeline3.setObjectName("pushButton_NLpipeline3")
        self.horizontalLayout_23.addWidget(self.pushButton_NLpipeline3)
        self.gridLayout_8.addLayout(self.horizontalLayout_23, 14, 1, 1, 1)
        self.label_44 = QtGui.QLabel(self.tab_10)
        self.label_44.setObjectName("label_44")
        self.gridLayout_8.addWidget(self.label_44, 7, 0, 1, 1)
        self.label_46 = QtGui.QLabel(self.tab_10)
        self.label_46.setObjectName("label_46")
        self.gridLayout_8.addWidget(self.label_46, 7, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_10)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 10, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_10)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 10, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_10)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 13, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_10)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 13, 1, 1, 1)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem31 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem31)
        self.pushButton_NLpipeline2 = QtGui.QPushButton(self.tab_10)
        self.pushButton_NLpipeline2.setObjectName("pushButton_NLpipeline2")
        self.horizontalLayout_22.addWidget(self.pushButton_NLpipeline2)
        self.gridLayout_8.addLayout(self.horizontalLayout_22, 11, 1, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_10)
        self.label_28.setEnabled(True)
        self.label_28.setObjectName("label_28")
        self.gridLayout_8.addWidget(self.label_28, 1, 0, 1, 1)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_40 = QtGui.QLabel(self.tab_10)
        self.label_40.setEnabled(True)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_25.addWidget(self.label_40)
        self.gridLayout_8.addLayout(self.horizontalLayout_25, 1, 1, 1, 1)
        spacerItem32 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem32, 4, 0, 1, 1)
        self.label_49 = QtGui.QLabel(self.tab_10)
        self.label_49.setObjectName("label_49")
        self.gridLayout_8.addWidget(self.label_49, 2, 0, 1, 1)
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.PRINLM = QtGui.QRadioButton(self.tab_10)
        self.PRINLM.setEnabled(False)
        self.PRINLM.setCheckable(False)
        self.PRINLM.setObjectName("PRINLM")
        self.horizontalLayout_31.addWidget(self.PRINLM)
        self.ODCT = QtGui.QRadioButton(self.tab_10)
        self.ODCT.setObjectName("ODCT")
        self.horizontalLayout_31.addWidget(self.ODCT)
        self.MRONLM = QtGui.QRadioButton(self.tab_10)
        self.MRONLM.setChecked(True)
        self.MRONLM.setObjectName("MRONLM")
        self.horizontalLayout_31.addWidget(self.MRONLM)
        self.AONLM = QtGui.QRadioButton(self.tab_10)
        self.AONLM.setObjectName("AONLM")
        self.horizontalLayout_31.addWidget(self.AONLM)
        self.ONLM = QtGui.QRadioButton(self.tab_10)
        self.ONLM.setObjectName("ONLM")
        self.horizontalLayout_31.addWidget(self.ONLM)
        self.gridLayout_8.addLayout(self.horizontalLayout_31, 2, 1, 1, 1)
        spacerItem33 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem33, 16, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab_10)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_8.addWidget(self.line_2, 4, 1, 1, 1)
        self.line_3 = QtGui.QFrame(self.tab_10)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_8.addWidget(self.line_3, 9, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.tab_10)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_8.addWidget(self.line_4, 12, 1, 1, 1)
        self.line_5 = QtGui.QFrame(self.tab_10)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_8.addWidget(self.line_5, 15, 1, 1, 1)
        self.label_52 = QtGui.QLabel(self.tab_10)
        self.label_52.setObjectName("label_52")
        self.gridLayout_8.addWidget(self.label_52, 5, 0, 1, 1)
        self.line_8 = QtGui.QFrame(self.tab_10)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_8.addWidget(self.line_8, 6, 1, 1, 1)
        self.horizontalLayout_50 = QtGui.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.checkBox_NLenableparams = QtGui.QCheckBox(self.tab_10)
        self.checkBox_NLenableparams.setObjectName("checkBox_NLenableparams")
        self.horizontalLayout_50.addWidget(self.checkBox_NLenableparams)
        self.line_9 = QtGui.QFrame(self.tab_10)
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_50.addWidget(self.line_9)
        self.label_15 = QtGui.QLabel(self.tab_10)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_50.addWidget(self.label_15)
        self.lineEdit_NLsigma = QtGui.QLineEdit(self.tab_10)
        self.lineEdit_NLsigma.setObjectName("lineEdit_NLsigma")
        self.horizontalLayout_50.addWidget(self.lineEdit_NLsigma)
        spacerItem34 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem34)
        self.label_51 = QtGui.QLabel(self.tab_10)
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_50.addWidget(self.label_51)
        self.linedit_NLsigmaratio = QtGui.QLineEdit(self.tab_10)
        self.linedit_NLsigmaratio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.linedit_NLsigmaratio.setObjectName("linedit_NLsigmaratio")
        self.horizontalLayout_50.addWidget(self.linedit_NLsigmaratio)
        spacerItem35 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem35)
        self.label_53 = QtGui.QLabel(self.tab_10)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_50.addWidget(self.label_53)
        self.lineEdit_NLsearcharea = QtGui.QLineEdit(self.tab_10)
        self.lineEdit_NLsearcharea.setObjectName("lineEdit_NLsearcharea")
        self.horizontalLayout_50.addWidget(self.lineEdit_NLsearcharea)
        spacerItem36 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_50.addItem(spacerItem36)
        self.label_54 = QtGui.QLabel(self.tab_10)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_50.addWidget(self.label_54)
        self.lineEdit_NLpatcharea = QtGui.QLineEdit(self.tab_10)
        self.lineEdit_NLpatcharea.setObjectName("lineEdit_NLpatcharea")
        self.horizontalLayout_50.addWidget(self.lineEdit_NLpatcharea)
        self.checkBox_NLrician = QtGui.QCheckBox(self.tab_10)
        self.checkBox_NLrician.setChecked(True)
        self.checkBox_NLrician.setObjectName("checkBox_NLrician")
        self.horizontalLayout_50.addWidget(self.checkBox_NLrician)
        self.gridLayout_8.addLayout(self.horizontalLayout_50, 5, 1, 1, 1)
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.CoilSensUnbiasedNL = QtGui.QRadioButton(self.tab_10)
        self.CoilSensUnbiasedNL.setObjectName("CoilSensUnbiasedNL")
        self.gridLayout_16.addWidget(self.CoilSensUnbiasedNL, 0, 0, 1, 1)
        self.MRONLM2 = QtGui.QRadioButton(self.tab_10)
        self.MRONLM2.setObjectName("MRONLM2")
        self.gridLayout_16.addWidget(self.MRONLM2, 0, 3, 1, 1)
        self.PRINLM2 = QtGui.QRadioButton(self.tab_10)
        self.PRINLM2.setObjectName("PRINLM2")
        self.gridLayout_16.addWidget(self.PRINLM2, 0, 1, 1, 1)
        self.AONLM2 = QtGui.QRadioButton(self.tab_10)
        self.AONLM2.setObjectName("AONLM2")
        self.gridLayout_16.addWidget(self.AONLM2, 0, 4, 1, 1)
        self.ODCT2 = QtGui.QRadioButton(self.tab_10)
        self.ODCT2.setObjectName("ODCT2")
        self.gridLayout_16.addWidget(self.ODCT2, 0, 2, 1, 1)
        self.ONLM2 = QtGui.QRadioButton(self.tab_10)
        self.ONLM2.setObjectName("ONLM2")
        self.gridLayout_16.addWidget(self.ONLM2, 0, 5, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_16, 3, 1, 1, 1)
        self.horizontalLayout_21.addLayout(self.gridLayout_8)
        self.tabWidget1.addTab(self.tab_10, "")
        self.gridLayout_3.addWidget(self.tabWidget1, 4, 1, 1, 1)
        self.label_50 = QtGui.QLabel(self.tab_9)
        self.label_50.setObjectName("label_50")
        self.gridLayout_3.addWidget(self.label_50, 2, 0, 1, 1)
        self.horizontalLayout_48 = QtGui.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.lineEdit_CoilSens = QtGui.QLineEdit(self.tab_9)
        self.lineEdit_CoilSens.setObjectName("lineEdit_CoilSens")
        self.horizontalLayout_48.addWidget(self.lineEdit_CoilSens)
        self.pushButton_CoilSensChangeDir = QtGui.QPushButton(self.tab_9)
        self.pushButton_CoilSensChangeDir.setObjectName(
            "pushButton_CoilSensChangeDir")
        self.horizontalLayout_48.addWidget(self.pushButton_CoilSensChangeDir)
        self.pushButton_CoilSensChangeFile = QtGui.QPushButton(self.tab_9)
        self.pushButton_CoilSensChangeFile.setObjectName(
            "pushButton_CoilSensChangeFile")
        self.horizontalLayout_48.addWidget(self.pushButton_CoilSensChangeFile)
        self.pushButton_CoilSensClear = QtGui.QPushButton(self.tab_9)
        self.pushButton_CoilSensClear.setObjectName("pushButton_CoilSensClear")
        self.horizontalLayout_48.addWidget(self.pushButton_CoilSensClear)
        self.gridLayout_3.addLayout(self.horizontalLayout_48, 2, 1, 1, 1)
        self.horizontalLayout_12.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_9, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Version_tag = QtGui.QLabel(self.centralwidget)
        self.Version_tag.setFrameShadow(QtGui.QFrame.Sunken)
        self.Version_tag.setObjectName("Version_tag")
        self.horizontalLayout_3.addWidget(self.Version_tag)
        spacerItem37 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem37)
        self.bottom_tag = QtGui.QLabel(self.centralwidget)
        self.bottom_tag.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bottom_tag.setFrameShape(QtGui.QFrame.NoFrame)
        self.bottom_tag.setFrameShadow(QtGui.QFrame.Sunken)
        self.bottom_tag.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bottom_tag.setOpenExternalLinks(True)
        self.bottom_tag.setObjectName("bottom_tag")
        self.horizontalLayout_3.addWidget(self.bottom_tag)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbort = QtGui.QAction(MainWindow)
        self.actionAbort.setObjectName("actionAbort")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen_FDF_Directory = QtGui.QAction(MainWindow)
        self.actionOpen_FDF_Directory.setObjectName("actionOpen_FDF_Directory")
        self.actionOpen_FID_Directory = QtGui.QAction(MainWindow)
        self.actionOpen_FID_Directory.setObjectName("actionOpen_FID_Directory")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionChange_DICOM_path = QtGui.QAction(MainWindow)
        self.actionChange_DICOM_path.setObjectName("actionChange_DICOM_path")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionConvert_FDF = QtGui.QAction(MainWindow)
        self.actionConvert_FDF.setObjectName("actionConvert_FDF")
        self.actionConvert_FID = QtGui.QAction(MainWindow)
        self.actionConvert_FID.setObjectName("actionConvert_FID")
        self.actionCheck_Dicom = QtGui.QAction(MainWindow)
        self.actionCheck_Dicom.setObjectName("actionCheck_Dicom")
        self.actionView_Dicom = QtGui.QAction(MainWindow)
        self.actionView_Dicom.setObjectName("actionView_Dicom")
        self.actionSend_to_DaRIS = QtGui.QAction(MainWindow)
        self.actionSend_to_DaRIS.setObjectName("actionSend_to_DaRIS")
        self.actionSave_Filter_Outputs_to_Nifti = QtGui.QAction(MainWindow)
        self.actionSave_Filter_Outputs_to_Nifti.setObjectName(
            "actionSave_Filter_Outputs_to_Nifti")
        self.menuFile.addAction(self.actionOpen_FDF_Directory)
        self.menuFile.addAction(self.actionOpen_FID_Directory)
        self.menuFile.addAction(self.actionChange_DICOM_path)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbort)
        self.menuFile.addAction(self.actionClose)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionSave_Filter_Outputs_to_Nifti)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionConvert_FDF)
        self.menuTools.addAction(self.actionConvert_FID)
        self.menuTools.addAction(self.actionCheck_Dicom)
        self.menuTools.addAction(self.actionView_Dicom)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionSend_to_DaRIS)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.label_13.setBuddy(self.lineEdit_fdfpath)
        self.label_16.setBuddy(self.lineEdit_dicompath)
        self.label_17.setBuddy(self.lineEdit_darisid)
        self.label_22.setBuddy(self.lineEdit_darisid2)
        self.label_24.setBuddy(self.lineEdit_fidpath)
        self.label_27.setBuddy(self.lineEdit_dicompath2)
        self.label_39.setBuddy(self.lineEdit_gsigma)
        self.label_30.setBuddy(self.lineEdit_gorder)
        self.label_31.setBuddy(self.lineEdit_gsigma)
        self.label_33.setBuddy(self.lineEdit_median_size)
        self.label_34.setBuddy(self.lineEdit_wiener_size)
        self.label_35.setBuddy(self.lineEdit_wiener_noise)
        self.label_37.setBuddy(self.lineEdit_gorder)
        self.label_41.setBuddy(self.lineEdit_gsigma)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.Multiecho_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget1.setCurrentIndex(3)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(
            "triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actionConvert_FDF, QtCore.SIGNAL(
            "triggered()"), self.pushButton_convert.click)
        QtCore.QObject.connect(self.actionOpen_FDF_Directory, QtCore.SIGNAL(
            "triggered()"), self.pushButton_changefdf.click)
        QtCore.QObject.connect(self.actionView_Dicom, QtCore.SIGNAL(
            "triggered()"), self.pushButton_view.click)
        QtCore.QObject.connect(self.actionSend_to_DaRIS, QtCore.SIGNAL(
            "triggered()"), self.pushButton_send2daris.click)
        QtCore.QObject.connect(self.actionOpen_FID_Directory, QtCore.SIGNAL(
            "triggered()"), self.pushButton_changefid.click)
        QtCore.QObject.connect(self.actionConvert_FID, QtCore.SIGNAL(
            "triggered()"), self.pushButton_convertfid.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "Agilent2Dicom: MBI\'s Agilent 9.4T MR Image Analysis and Dicom Converter Application (2.0.3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changefdf.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change the FDF input directory", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changefdf.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate(
            "MainWindow", "FDF folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate(
            "MainWindow", "Dicom folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate(
            "MainWindow", "DaRIS ID", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changedicom.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change the output DICOM directory.  Only do this if the automatic folder name is already taken.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changedicom.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_darisid.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "DaRIS ID string should automatically update with new FDF folder", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_debugging.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Display more verbose debugging", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_debugging.setText(QtGui.QApplication.translate(
            "MainWindow", "Show debugging", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_nodcmulti.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Do not convert 2D slices to enhance DICOM format", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_nodcmulti.setText(QtGui.QApplication.translate(
            "MainWindow", "Keep 2D DICOM slices", None, QtGui.QApplication.UnicodeUTF8))
        self.Multiecho_2.setTabText(self.Multiecho_2.indexOf(self.tab_generic_2), QtGui.QApplication.translate(
            "MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.FDFprocparInfo.setText(QtGui.QApplication.translate(
            "MainWindow", "Metatdata information: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_convert.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Convert FDF folder to DICOM using fdf2dcm.sh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_convert.setText(QtGui.QApplication.translate(
            "MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_check.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Check dicom output using Dicom3Tool\'s DCIODVFY", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_check.setText(QtGui.QApplication.translate(
            "MainWindow", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "View dicom output using MRtrix\'s MRVIEW", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view.setText(QtGui.QApplication.translate(
            "MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_send2daris.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Send Dicom folder to DaRIS ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_send2daris.setText(QtGui.QApplication.translate(
            "MainWindow", "Send to DaRIS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fdf_2), QtGui.QApplication.translate(
            "MainWindow", "FDF converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate(
            "MainWindow", "DaRIS ID", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changefid.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change the input FID directory", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changefid.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate(
            "MainWindow", "FID folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate(
            "MainWindow", "Dicom folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changedicom2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change the output DICOM directory.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changedicom2.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_darisid2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "DaRIS ID generated from header information in FID procpar.  Do not edit unless you know what you are doing!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_convertfid.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Process FID folder using the fid2dcm.sh script", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_convertfid.setText(QtGui.QApplication.translate(
            "MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_check2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Check the dicom outputs using Dicom3Tool\'s DCIODVFY", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_check2.setText(QtGui.QApplication.translate(
            "MainWindow", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "View the filtered and unfiltered images in MRVIEW", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view2.setText(QtGui.QApplication.translate(
            "MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_send2daris2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Send DICOMs to DaRIS", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_send2daris2.setText(QtGui.QApplication.translate(
            "MainWindow", "Send to DaRIS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setToolTip(QtGui.QApplication.translate("MainWindow", "Multidimensional Gaussian, Epanechnikov, Median, StDev or Wiener filters.  \n"
                                                                 "Warning: use identical sigma values on isotropic images only. Non-isotropic values should be based on image size in comma-serarated list", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_magn.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_pha.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_reimag.setText(QtGui.QApplication.translate(
            "MainWindow", "Save REAL and IMAG", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ksp.setText(QtGui.QApplication.translate(
            "MainWindow", "Save K space data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_nifti.setText(QtGui.QApplication.translate(
            "MainWindow", "Save magnitude as NIFTI (limited header info)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_reimag_raw.setText(QtGui.QApplication.translate(
            "MainWindow", "Save REAL and IMAG", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ksp_raw.setText(QtGui.QApplication.translate(
            "MainWindow", "Save K space data", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_magn_raw.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_pha_raw.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Outputs saved as \"<dicom folder>-<filter type>-<magn or pha or real or imag>.dcm\".  K-space data is saved to MATLAB mat file \"<dicom folder>-<ksp>.mat\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate(
            "MainWindow", "Outputs of filtered image(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Outputs saved as \"<dicom folder>-<filter type>-<magn or pha or real or imag>.dcm\".  K-space data is saved to MATLAB mat file \"<dicom folder>-<ksp>.mat\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate(
            "MainWindow", "Outputs of original reconstructed image:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QtGui.QApplication.translate(
            "MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspgaussian.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "<html><head/><body><p> KSPACEFILTER gaussian filter of complex 3D image</p><p><br/></p><p>    filtered_magnitude = kspacefilter(realimg, imagimg)</p><p><br/></p><p><br/></p><p>    scipy.ndimage.fourier.fourier_gaussian</p><p><br/></p><p>    scipy.ndimage.fourier.fourier_gaussian(input, sigma, n=-1, axis=-1,</p><p>    output=None)[source]</p><p><br/></p><p>    Multi-dimensional Gaussian fourier filter.</p><p><br/></p><p>    The array is multiplied with the fourier transform of a Gaussian kernel.</p><p><br/></p><p>    Parameters:</p><p>    input : array_like</p><p>    The input array.</p><p>    sigma : float or sequence</p><p><br/></p><p>    The sigma of the Gaussian kernel. If a float, sigma is the same</p><p>    for all axes. If a sequence, sigma has to contain one value for</p><p>    each axis.</p><p><br/></p><p>    n : int, optional</p><p><br/></p><p>    If n is negative (default), then the input is assumed to be the</p><p>    result of a complex fft. If n is larger than or equal to zero, the</p><p>    input is assumed to be the result of a real fft, and n gives the</p><p>    length of the array before transformation along the real transform</p><p>    direction.</p><p><br/></p><p>    axis : int, optional</p><p>    The axis of the real transform.</p><p>    output : ndarray, optional</p><p><br/></p><p>    If given, the result of filtering the input is placed in this array. None</p><p>    is returned in this case.</p><p><br/></p><p>    Returns:</p><p>    fourier_gaussian : ndarray or None</p><p>    The filtered input. If output is given as a parameter, None is returned.</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspgaussian.setText(QtGui.QApplication.translate("MainWindow", "Use K-space Gaussian filter\n"
                                                                       "(Fourier domain)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspgaussshift.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Disable centre-shifting in k-space", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspgaussshift.setText(QtGui.QApplication.translate(
            "MainWindow", "Disable centre shift ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspgauss_super.setToolTip(QtGui.QApplication.translate("MainWindow", "Use zero padding in k-space to double image resolution. \n"
                                                                             "\n"
                                                                             "WARNING this will increase 3D volume sizes by a factor of 8.\n"
                                                                             "\n"
                                                                             "Double-resolution uses zero-filled k-space data to double the resolution of the image. \n"
                                                                             "The super-resolution image is saved to NIFTI while the standard is saved to dicom. ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspgauss_super.setText(QtGui.QApplication.translate("MainWindow", "Double-resolution\n"
                                                                          "(Saved to NIFTI only)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setToolTip(QtGui.QApplication.translate("MainWindow", "scalar or sequence of scalars\n"
                                                              "\n"
                                                              "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.\n"
                                                              "\n"
                                                              "Effective Fourier domain sigma is calculated as the image size divided by image domain sigma. sigma.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate(
            "MainWindow", "Effective Image Domain Sigma", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gfsigma.setToolTip(QtGui.QApplication.translate("MainWindow", "scalar or sequence of scalars\n"
                                                                      "\n"
                                                                      "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.  Default value for isotropic GRE scans is 1/sqrt(2)=0.707.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gfsigma.setText(QtGui.QApplication.translate(
            "MainWindow", "0.707,0.707,0.707", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_kspgauss_sigunit.setItemText(0, QtGui.QApplication.translate(
            "MainWindow", "unit voxel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_kspgauss_sigunit.setItemText(1, QtGui.QApplication.translate(
            "MainWindow", "in mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_kspgauss_sigunit.setItemText(2, QtGui.QApplication.translate(
            "MainWindow", "in um", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Actual FT Gaussian sigma\n"
                                                        "(matrix size/sigma)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_16.setText(QtGui.QApplication.translate(
            "MainWindow", "Disable Dicom, use Nifti instead", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QtGui.QApplication.translate(
            "MainWindow", "K-space Gaussian", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspepa.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "3D Epanechnikov filter in k-space (Fourier domain).   FFT of image filter used instead of calculated filter.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspepa.setText(QtGui.QApplication.translate("MainWindow", "Use Kspace Epanechnikov filter\n"
                                                                  "(Fourier domain)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspepashift.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Disable k-space frequency shift", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspepashift.setText(QtGui.QApplication.translate(
            "MainWindow", "No Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspepa_super.setToolTip(QtGui.QApplication.translate("MainWindow", "Use zero padding in k-space to double image resolution. \n"
                                                                           "\n"
                                                                           "!!!WARNING this will increase 3D volume sizes by a factor of 8.!!!\n"
                                                                           "\n"
                                                                           "Double-resolution uses zero-filled k-space data to double the resolution of the image. \n"
                                                                           "The super-resolution image is saved to NIFTI while the standard is saved to dicom. ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_kspepa_super.setText(QtGui.QApplication.translate("MainWindow", "Double-resolution\n"
                                                                        "(Saved to NIFTI only)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Effective Filter Bandwidth\n"
                                                          "(Use Gaussian sigma\n"
                                                          " times sqrt(dimension + 4), \n"
                                                          "eg. sqrt(7)*sqrt(0.5)=1.8707 )", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_kspepa_band.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Bandwidth equivalent in image space.  Comma separated values (no spaces) accepted for non-isotropic slices.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_kspepa_band.setText(QtGui.QApplication.translate(
            "MainWindow", "1.8708,1.8708,1.8708", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_kspepa_scaleunit.setItemText(0, QtGui.QApplication.translate(
            "MainWindow", "unit voxel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_kspepa_scaleunit.setItemText(1, QtGui.QApplication.translate(
            "MainWindow", "mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_kspepa_scaleunit.setItemText(2, QtGui.QApplication.translate(
            "MainWindow", "um", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", " Note: Complex Fourier domain Epanechnikov filter is generated from complex image domain kernel. \n"
                                                          "\n"
                                                          "Pseudo super-resolution does not give additional subvoxel information to the image.  It is a complex interpolation for assisting contrast in rendering \n"
                                                          "", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_15.setText(QtGui.QApplication.translate(
            "MainWindow", "Disable Dicom output, use Nifti instead", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QtGui.QApplication.translate(
            "MainWindow", "K-space Epanechnikov", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setToolTip(QtGui.QApplication.translate("MainWindow", "order : {0, 1, 2, 3} or sequence from same set, optional\n"
                                                              "\n"
                                                              "    The order of the filter along each axis is given as a sequence of integers, or as a single number. An order of 0 corresponds to convolution with a Gaussian kernel. An order of 1, 2, or 3 corresponds to convolution with the first, second or third derivatives of a Gaussian. Higher order derivatives are not implemented\n"
                                                              "", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate(
            "MainWindow", "Order", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gorder.setToolTip(QtGui.QApplication.translate("MainWindow", "order : {0, 1, 2, 3} or sequence from same set, optional\n"
                                                                     "\n"
                                                                     "    The order of the filter along each axis is given as a sequence of integers, \n"
                                                                     "or as a single number. An order of 0 corresponds to convolution with a Gaussian \n"
                                                                     "kernel. An order of 1, 2, or 3 corresponds to convolution with the first, \n"
                                                                     "second or third derivatives of a Gaussian. \n"
                                                                     "Higher order derivatives are not implemented\n"
                                                                     "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gorder.setText(QtGui.QApplication.translate(
            "MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setToolTip(QtGui.QApplication.translate("MainWindow", "scalar or sequence of scalars\n"
                                                              "\n"
                                                              "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate(
            "MainWindow", "Sigma", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gsigma.setToolTip(QtGui.QApplication.translate("MainWindow", "scalar or sequence of scalars\n"
                                                                     "\n"
                                                                     "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.  Default value for isotropic GRE scans is 1/sqrt(2)=0.707.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_gsigma.setText(QtGui.QApplication.translate(
            "MainWindow", "0.707,0.707,0.707", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_gauss_sigmascale.setItemText(0, QtGui.QApplication.translate(
            "MainWindow", "unit voxel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_gauss_sigmascale.setItemText(1, QtGui.QApplication.translate(
            "MainWindow", "in mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_gauss_sigmascale.setItemText(2, QtGui.QApplication.translate(
            "MainWindow", "in um", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                              "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate(
            "MainWindow", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.reflect.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                             "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to constant.", None, QtGui.QApplication.UnicodeUTF8))
        self.reflect.setText(QtGui.QApplication.translate(
            "MainWindow", "Reflect", None, QtGui.QApplication.UnicodeUTF8))
        self.nearest.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                             "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.nearest.setText(QtGui.QApplication.translate(
            "MainWindow", "Nearest", None, QtGui.QApplication.UnicodeUTF8))
        self.wrap.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                          "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.wrap.setText(QtGui.QApplication.translate(
            "MainWindow", "Wrap", None, QtGui.QApplication.UnicodeUTF8))
        self.mirror.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                            "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.mirror.setText(QtGui.QApplication.translate(
            "MainWindow", "Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_gaussian3D.setToolTip(QtGui.QApplication.translate("MainWindow", " scipy.ndimage.filters.gaussian_filter(input, sigma, order=0, output=None, mode=\'reflect\', cval=0.0, truncate=4.0)[source]\n"
                                                                         "\n"
                                                                         "    Multidimensional Gaussian filter.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_gaussian3D.setText(QtGui.QApplication.translate(
            "MainWindow", "Use 3D Gaussian filter", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_gaussian2D.setToolTip(QtGui.QApplication.translate("MainWindow", "Use Guassian filter on 2D slices. \n"
                                                                         "Use the order of the sizes in the information box above to set the sigma values below.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_gaussian2D.setText(QtGui.QApplication.translate(
            "MainWindow", "Use 2D Gaussian filter", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), QtGui.QApplication.translate(
            "MainWindow", "Gaussian", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_median.setToolTip(QtGui.QApplication.translate("MainWindow", "scipy.ndimage.filters.median_filter¶\n"
                                                                     "\n"
                                                                     "scipy.ndimage.filters.median_filter(input, size=None, footprint=None, output=None, mode=\'reflect\', cval=0.0, origin=0)[source]\n"
                                                                     "\n"
                                                                     "    Calculates a multidimensional median filter.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_median.setText(QtGui.QApplication.translate(
            "MainWindow", "Use Median Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setToolTip(QtGui.QApplication.translate("MainWindow", "     \n"
                                                              "\n"
                                                              "size : scalar or tuple, optional\n"
                                                              "\n"
                                                              "    See footprint, below\n"
                                                              "\n"
                                                              "footprint : array, optional\n"
                                                              "\n"
                                                              "    Either size or footprint must be defined. size gives the shape that is taken from the input array, at every element position,\n"
                                                              " to define the input to the filter function. footprint is a boolean array that specifies (implicitly) a shape,\n"
                                                              " but also which of the elements within this shape will get passed to the filter function. Thus size=(n,m) is equivalent to footprint=np.ones((n,m)).\n"
                                                              " We adjust size to the number of dimensions of the input array, so that, if the input array is shape (10,10,10),\n"
                                                              " and size is 2, then the actual size used is (2,2,2).\n"
                                                              "", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate(
            "MainWindow", "Window Size(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_median_size.setToolTip(QtGui.QApplication.translate("MainWindow", "     \n"
                                                                          "\n"
                                                                          "size : scalar or tuple, optional\n"
                                                                          "\n"
                                                                          "    See footprint, below\n"
                                                                          "\n"
                                                                          "footprint : array, optional\n"
                                                                          "\n"
                                                                          "    Either size or footprint must be defined. size gives the shape that is taken from the input array, at every element position,\n"
                                                                          " to define the input to the filter function. footprint is a boolean array that specifies (implicitly) a shape,\n"
                                                                          " but also which of the elements within this shape will get passed to the filter function. Thus size=(n,m) is equivalent to footprint=np.ones((n,m)).\n"
                                                                          " We adjust size to the number of dimensions of the input array, so that, if the input array is shape (10,10,10),\n"
                                                                          " and size is 2, then the actual size used is (2,2,2).\n"
                                                                          "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_median_size.setText(QtGui.QApplication.translate(
            "MainWindow", "5,5,5", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QtGui.QApplication.translate(
            "MainWindow", "Median", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_wiener.setToolTip(QtGui.QApplication.translate("MainWindow", "NOT ENABLED - Speak to MBI Imaging Team\n"
                                                                     "\n"
                                                                     "scipy.signal.wiener(im, mysize=None, noise=None)\n"
                                                                     "\n"
                                                                     "    Perform a Wiener filter on an N-dimensional array.\n"
                                                                     "\n"
                                                                     "    Apply a Wiener filter to the N-dimensional array im.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_wiener.setText(QtGui.QApplication.translate(
            "MainWindow", "Use Wiener Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setToolTip(QtGui.QApplication.translate("MainWindow", "mysize : int or arraylike, optional\n"
                                                              "\n"
                                                              "    A scalar or an N-length list giving the size of the Wiener filter window in each dimension. Elements of mysize should be odd. If mysize is a scalar, then this scalar is used as the size in each dimension.\n"
                                                              "", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate(
            "MainWindow", " Window Size(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_wiener_size.setToolTip(QtGui.QApplication.translate("MainWindow", "mysize : int or arraylike, optional\n"
                                                                          "\n"
                                                                          "    A scalar or an N-length list giving the size of the Wiener filter window in each dimension. Elements of mysize should be odd. If mysize is a scalar, then this scalar is used as the size in each dimension.\n"
                                                                          "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_wiener_size.setText(QtGui.QApplication.translate(
            "MainWindow", "5,5,5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "<html><head/><body><p>noise: Estimation of noise, Set to 0 for local variance to be used.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate(
            "MainWindow", "Noise (Est. variance, 0 uses localised variance) ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_wiener_noise.setToolTip(QtGui.QApplication.translate("MainWindow", "mysize : int or arraylike, optional\n"
                                                                           "\n"
                                                                           "    A scalar or an N-length list giving the size of the Wiener filter window in each dimension. Elements of mysize should be odd. If mysize is a scalar, then this scalar is used as the size in each dimension.\n"
                                                                           "", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_wiener_noise.setText(QtGui.QApplication.translate(
            "MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QtGui.QApplication.translate(
            "MainWindow", "Wiener", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setToolTip(QtGui.QApplication.translate("MainWindow", "order : {0, 1, 2, 3} or sequence from same set, optional\n"
                                                              "\n"
                                                              "    The order of the filter along each axis is given as a sequence of integers, or as a single number. An order of 0 corresponds to convolution with a Gaussian kernel. An order of 1, 2, or 3 corresponds to convolution with the first, second or third derivatives of a Gaussian. Higher order derivatives are not implemented\n"
                                                              "", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate(
            "MainWindow", "bandwidth = gaussian sigma * sqrt(dim + 4) ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setToolTip(QtGui.QApplication.translate("MainWindow", "scalar or sequence of scalars\n"
                                                              "\n"
                                                              "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate(
            "MainWindow", "Bandwidth", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_epaband.setToolTip(QtGui.QApplication.translate("MainWindow", "scalar or sequence of scalars\n"
                                                                      "\n"
                                                                      "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.  Default value for isotropic GRE scans is 1/sqrt(2)=0.707.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_epaband.setText(QtGui.QApplication.translate(
            "MainWindow", "1.8708,1.8708,1.8708", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_epabandwidth.setItemText(0, QtGui.QApplication.translate(
            "MainWindow", "unit voxel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_epabandwidth.setItemText(1, QtGui.QApplication.translate(
            "MainWindow", "in mm", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_epabandwidth.setItemText(2, QtGui.QApplication.translate(
            "MainWindow", "in um", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                              "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate(
            "MainWindow", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.reflect_epa.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                                 "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.reflect_epa.setText(QtGui.QApplication.translate(
            "MainWindow", "Reflect", None, QtGui.QApplication.UnicodeUTF8))
        self.nearest_epa.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                                 "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.nearest_epa.setText(QtGui.QApplication.translate(
            "MainWindow", "Nearest", None, QtGui.QApplication.UnicodeUTF8))
        self.wrap_epa.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                              "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.wrap_epa.setText(QtGui.QApplication.translate(
            "MainWindow", "Wrap", None, QtGui.QApplication.UnicodeUTF8))
        self.mirror_epa.setToolTip(QtGui.QApplication.translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                                                "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None, QtGui.QApplication.UnicodeUTF8))
        self.mirror_epa.setText(QtGui.QApplication.translate(
            "MainWindow", "Mirror", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_epanechnikov3D.setToolTip(QtGui.QApplication.translate("MainWindow", "Bespoke epanechnikov_filter(input, sigma)\n"
                                                                             "\n"
                                                                             "    Fast multidimensional Epanechnikov filter.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_epanechnikov3D.setText(QtGui.QApplication.translate(
            "MainWindow", "Use 3D Epanechnikov filter", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_epanechnikov2D.setText(QtGui.QApplication.translate(
            "MainWindow", "Use 2D Epanechnikov filter", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QtGui.QApplication.translate(
            "MainWindow", "Epanechnikov", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_stdev_cplx.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "<html><head/><body><p>Don\'t use this - use the phase</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_stdev_cplx.setText(QtGui.QApplication.translate(
            "MainWindow", "Use CPLX Std dev filter", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_stdev_magn.setText(QtGui.QApplication.translate(
            "MainWindow", "Use Magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_stdev_phase.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "<html><head/><body><p>Localised standard deviation of the image phase</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_stdev_phase.setText(QtGui.QApplication.translate(
            "MainWindow", "Use Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.stdev_window_size_label.setText(QtGui.QApplication.translate(
            "MainWindow", "Window size (default 5)  ", None, QtGui.QApplication.UnicodeUTF8))
        self.stdev_window_size.setText(QtGui.QApplication.translate(
            "MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QtGui.QApplication.translate(
            "MainWindow", "Stdev", None, QtGui.QApplication.UnicodeUTF8))
        self.FIDprocparInfo.setText(QtGui.QApplication.translate(
            "MainWindow", "Metadata display:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CleanUpDicoms.setText(QtGui.QApplication.translate(
            "MainWindow", "Clean up", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fid_2), QtGui.QApplication.translate(
            "MainWindow", "FID converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Input 2:\n"
                                                          "FID/FDF folder or\n"
                                                          "Nifti file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Input 1\n"
                                                          " FID or FDF dir or\n"
                                                          " Nifti file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Nifti\n"
                                                          "Output\n"
                                                          "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_procout.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_processfolder2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change FID or FDF folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_processfolder2.setText(QtGui.QApplication.translate(
            "MainWindow", "ChangeDir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ChangeNifti2.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change Nifti file", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ChangeNifti2.setText(QtGui.QApplication.translate(
            "MainWindow", "Change File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ClearProc2.setText(QtGui.QApplication.translate(
            "MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_processfolder1.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change FID or FDF folder.  Do not use this for Nifti files.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_processfolder1.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ChangeNifti1.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Change Nifti file.  Use \"Change Dir\" for FID and FDF", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ChangeNifti1.setText(QtGui.QApplication.translate(
            "MainWindow", "Change File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ClearProc1.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Clear input 1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ClearProc1.setText(QtGui.QApplication.translate(
            "MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Homodyne filtered MAGNITUDE and PHASE (or REAL and IMAG) \n"
                                                          "SWI Negative (default output) and Positive contrasts available", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate(
            "MainWindow", "Phase-based processing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate(
            "MainWindow", "SWI order (default 4)", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_swiorder.setText(QtGui.QApplication.translate(
            "MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_swisaveRI.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Real and Imag Homodyne filtered images", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_swineg.setText(QtGui.QApplication.translate(
            "MainWindow", "Produce SWI negative", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_swipos.setText(QtGui.QApplication.translate(
            "MainWindow", "Produce SWI positive", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate(
            "MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate(
            "MainWindow", "Pre-processing", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_SWI.setText(QtGui.QApplication.translate(
            "MainWindow", "Process SWI", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_swipreprocess.setText(QtGui.QApplication.translate(
            "MainWindow", "Use Complex Kspace filtering prior to Phase-based processing ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage1), QtGui.QApplication.translate(
            "MainWindow", "Phase/SWI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Use inverse Sum-of-Squares to condense multi-echo images into one. \n"
                                                           "Let p=2 or 3 for images with susceptibility components. Otherwise use p=-2 or -3.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate(
            "MainWindow", "Multi-echo enhancement (MEE)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate(
            "MainWindow", "p", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_meeorder.setText(QtGui.QApplication.translate(
            "MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_meepreproc.setText(QtGui.QApplication.translate(
            "MainWindow", "Use Complex Kspace filtered image magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_meesaveRI.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Real and Imaginary components", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_meeswi.setText(QtGui.QApplication.translate(
            "MainWindow", "Use SWI magnitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate(
            "MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate(
            "MainWindow", "Order", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_MEE.setText(QtGui.QApplication.translate(
            "MainWindow", "Run MEE", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage2), QtGui.QApplication.translate(
            "MainWindow", "Multi-Echo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate(
            "MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_MCI.setText(QtGui.QApplication.translate(
            "MainWindow", "Run MCI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48.setText(QtGui.QApplication.translate(
            "MainWindow", "Maximum constract imaging", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_MCI_RI.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Real and Imag", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_11), QtGui.QApplication.translate(
            "MainWindow", "MCI", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabToolTip(self.tabWidget1.indexOf(self.tab_11), QtGui.QApplication.translate("MainWindow", "Maximum contrast imaging\n"
                                                                                                         "Optimal vector difference between GM and WM.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_NLinputRI.setText(QtGui.QApplication.translate(
            "MainWindow", "Real and Imag (only valid for Pipeline 1)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NLpipeline1.setText(QtGui.QApplication.translate(
            "MainWindow", "Run Pipeline 1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_NLsaveRI.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Real/Imag", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_NLsavePhase.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_SaveSWIProc3.setText(QtGui.QApplication.translate(
            "MainWindow", "Save SWI (Calc after processing)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NLpipeline3.setText(QtGui.QApplication.translate(
            "MainWindow", "Run Pipeline 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate(
            "MainWindow", "Pipeline 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate(
            "MainWindow", "Magnitude  (Image 1) -> Automatic Non-local means -> Denoised Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Noise Estimated NLm (2 reps required)\n"
                                                           "Magnitude (Image 1) -> Noise Est -> Non-local means -> Denoised Image\n"
                                                           "Magnitude (Image 2) -^", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate(
            "MainWindow", "Pipeline 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate(
            "MainWindow", "Pipeline 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Complex Noise Estimated NLm (2 complex reps required)\n"
                                                           "Complex Image 1 -> Homodyne Filter -> X -> Noise Est (Real)-> Non-local means (Real) -> Denoised Complex Image\n"
                                                           "Complex Image 2 -> Homodyne Filter -^     > Noise Est (Imag)-> Non-local means (Imag) -^", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_NLpipeline2.setText(QtGui.QApplication.translate(
            "MainWindow", "Run Pipeline 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("MainWindow", "Non-local means denoising filters using:\n"
                                                           "1. [In Development] Coil sensitivy Unbiased NL filter (MBI/ others)\n"
                                                           "2. MRIdenoising package (Coupe and Manjon, Univ Bordeaux)\n"
                                                           "MRONLM filter is the preferred filter \n"
                                                           " Note:  Outputs are the magnitude of the NLmeans filter saved as Nifti. If two inputs are included the 2 and 3 pipelines output the average NLmeans result.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_49.setText(QtGui.QApplication.translate(
            "MainWindow", "NL Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.PRINLM.setToolTip(QtGui.QApplication.translate("MainWindow", "The PRINLM filter is described in:                                   \n"
                                                            " JV Manjon, P. Coupe, A Buades, DL Collins, M. Robles  \n"
                                                            " New methods for MRI denoising based on sparseness and self-similarity. \n"
                                                            "Medical Image Analysis, 16(1):18-27, 2012\n"
                                                            "\n"
                                                            " [ imaPRINLM] = MRIDenoisingPRINLM(ima, h, beta=1, rician=1, verbose)", None, QtGui.QApplication.UnicodeUTF8))
        self.PRINLM.setText(QtGui.QApplication.translate(
            "MainWindow", "PRINLM", None, QtGui.QApplication.UnicodeUTF8))
        self.ODCT.setToolTip(QtGui.QApplication.translate("MainWindow", "\n"
                                                          "%   Description: Denoising of a 3D MRI image using the ODCT filter\n"
                                                          "%               \n"
                                                          "%   Usage:      MRIDenoisingODCT(ima, h, rician, verbose)\n"
                                                          "%\n"
                                                          "%   ima:        3D MR image\n"
                                                          "%   h:          std of noise\n"
                                                          "%   rician:     0: Gaussian noise 1: Rician noise \n"
                                                          "%   verbose:    0 no display of graph\n"
                                                          "%               1 display of graph\n"
                                                          "%\n"
                                                          "%                          Details on ODCT filter\n"
                                                          "%**************************************************************************\n"
                                                          "%* The ODCT filter is described in:                                       *\n"
                                                          "%*                                                                        *\n"
                                                          "%* JV Manjon, P. Coupe, A Buades, DL Collins, M. Robles                   *\n"
                                                          "%* New methods for MRI denoising based on sparseness and self-similarity. * \n"
                                                          "%* Medical Image Analysis, 16(1):18-27                                    *\n"
                                                          "%* 2012                                                                   *\n"
                                                          "%**************************************************************************\n"
                                                          "%\n"
                                                          "% Pierrick Coupe - pierrick.coupe@labri.fr\n"
                                                          "% Jose V. Manjon - jmanjon@fis.upv.es\n"
                                                          "%\n"
                                                          "% Universite de Bordeaux\n"
                                                          "% LaBRI, UMR 5800, 33400 Talence\n"
                                                          "%\n"
                                                          "% Copyright (C) 2011 Pierrick Coupe and Jose V. Manjon", None, QtGui.QApplication.UnicodeUTF8))
        self.ODCT.setText(QtGui.QApplication.translate(
            "MainWindow", "ODCT", None, QtGui.QApplication.UnicodeUTF8))
        self.MRONLM.setToolTip(QtGui.QApplication.translate("MainWindow", " The MRONLM filter is described in:    \n"
                                                            "\n"
                                                            "P. Coupe, J.V. Manjon, R. Robles, D.L. Collins    \n"
                                                            " Adaptive Multiresolution Non-Local Means Filter for 3D MR Image \n"
                                                            " Denoising. 6(5): 558-568,  IET Image Processing.      2012  \n"
                                                            "\n"
                                                            "[ MRORNLM] = MRIDenoisingMRONLM(ima, h, beta, patchsize, searcharea, rician, verbose)\n"
                                                            "\n"
                                                            "patchsize=1, searcharea=3, rician=1", None, QtGui.QApplication.UnicodeUTF8))
        self.MRONLM.setText(QtGui.QApplication.translate(
            "MainWindow", "MRONLM", None, QtGui.QApplication.UnicodeUTF8))
        self.AONLM.setToolTip(QtGui.QApplication.translate("MainWindow", "%   Description: Denoising of a 3D MR image using the AONLM filter\n"
                                                           "%\n"
                                                           "%\n"
                                                           "%   Usage:      MRIDenoisingAONLM(ima, patchsize, searcharea, beta, rician, verbose)\n"
                                                           "%\n"
                                                           "%   ima:        3D MRI image\n"
                                                           "%   patchsize:  radius of patch in voxel\n"
                                                           "%   searcharea: radius of search area in voxel\n"
                                                           "%   beta:       smoothing parameter (default 1)\n"
                                                           "%   rician:     0: Gaussian noise 1: Rician noise \n"
                                                           "%   verbose:    0 no display of graph\n"
                                                           "%               1 display of graph\n"
                                                           "%\n"
                                                           "%                          Details on ANLM filter\n"
                                                           "%**************************************************************************\n"
                                                           "%* The AONLM filter is described in:                                      *\n"
                                                           "%*                                                                        *\n"
                                                           "%* J. V. Manjon, P. Coupe, L. Marti-Bonmati, D. L. Collins, M. Robles.    *\n"
                                                           "%* Adaptive Non-Local Means Denoising of MR Images with Spatially         *\n"
                                                           "%* varying Noise Levels.                                                  *\n"
                                                           "%* Journal of Magnetic Resonance Imaging, 31(1):192-203, 2010             *\n"
                                                           "%**************************************************************************\n"
                                                           "%\n"
                                                           "% Pierrick Coupe - pierrick.coupe@labri.fr\n"
                                                           "% Jose V. Manjon - jmanjon@fis.upv.es\n"
                                                           "%\n"
                                                           "% Universit� de Bordeaux\n"
                                                           "% LaBRI, UMR 5800, 33400 Talence\n"
                                                           "%\n"
                                                           "% Copyright (C) 2011 Pierrick Coupe and Jose V. Manjon", None, QtGui.QApplication.UnicodeUTF8))
        self.AONLM.setText(QtGui.QApplication.translate(
            "MainWindow", "AONLM", None, QtGui.QApplication.UnicodeUTF8))
        self.ONLM.setToolTip(QtGui.QApplication.translate("MainWindow", "\n"
                                                          "%   Description:  Denoising of a 3D MRI image using the ONLM filter\n"
                                                          "%               \n"
                                                          "%\n"
                                                          "%   Usage:      MRIDenoisingONLM(ima, h, beta, patchsize, searcharea, rician, verbose)\n"
                                                          "%\n"
                                                          "%   ima:        3D MR image\n"
                                                          "%   h:          std of rician noise\n"
                                                          "%   beta:       smoothing parameter (default 1)\n"
                                                          "%   patchsize:  radius of patch in voxel\n"
                                                          "%   searcharea: radius of search area in voxel\n"
                                                          "%   rician:     0: Gaussian noise 1: Rician noise \n"
                                                          "%   verbose:    0 no display of graph\n"
                                                          "%               1 display of graph\n"
                                                          "%\n"
                                                          "%                          Details on ONLM filter\n"
                                                          "%**************************************************************************\n"
                                                          "%* The ONLM filter is described in:                                       *\n"
                                                          "%*                                                                        *\n"
                                                          "%* P. Coupe, P. Yger, S. Prima, P. Hellier, C. Kervrann, C. Barillot.     *\n"
                                                          "%* An Optimized Blockwise Non Local Means Denoising Filter for 3D Magnetic*\n"
                                                          "%* Resonance Images. IEEE Transactions on Medical Imaging, 27(4):425-441, *\n"
                                                          "%* Avril 2008                                                             *\n"
                                                          "%**************************************************************************\n"
                                                          "%                      Details on Rician adaptation\n"
                                                          "%**************************************************************************\n"
                                                          "%* The adaptation to Rician noise is described in:                        *\n"
                                                          "%*                                                                        *\n"
                                                          "%* N. Wiest-Daessle, S. Prima, P. Coupe, S.P. Morrissey, C. Barillot.     *\n"
                                                          "%* Rician noise removal by non-local means filtering for low              *\n"
                                                          "%* signal-to-noise ratio MRI: Applications to DT-MRI. In 11th             *\n"
                                                          "%* International Conference on Medical Image Computing and                *\n"
                                                          "%* Computer-Assisted Intervention, MICCAI\'2008,                           *\n"
                                                          "%* Pages 171-179, New York, Etats-Unis, Septembre 2008                    *\n"
                                                          "%**************************************************************************\n"
                                                          "%\n"
                                                          "% Pierrick Coupe - pierrick.coupe@labri.fr\n"
                                                          "% Jose V. Manjon - jmanjon@fis.upv.es\n"
                                                          "%\n"
                                                          "% Universit� de Bordeaux\n"
                                                          "% LaBRI, UMR 5800, 33400 Talence\n"
                                                          "%\n"
                                                          "% Copyright (C) 2011 Pierrick Coupe and Jose V. Manjon", None, QtGui.QApplication.UnicodeUTF8))
        self.ONLM.setText(QtGui.QApplication.translate(
            "MainWindow", "ONLM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate(
            "MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_NLenableparams.setToolTip(QtGui.QApplication.translate("MainWindow", "Check enable with you want to modify NL parameters - any changes to default parameters will be ignored if you don\'t click this checkbox\n"
                                                                             "", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_NLenableparams.setText(QtGui.QApplication.translate(
            "MainWindow", "Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setToolTip(QtGui.QApplication.translate("MainWindow", "Sigma = St. dev. of noise.\n"
                                                              "Leave empty for calculation using NoiseEstimation in Pipeline 1 or difference between images in pipelines 2 and 3.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate(
            "MainWindow", "Sigma", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_NLsigma.setToolTip(QtGui.QApplication.translate("MainWindow", "Sigma = St. dev. of noise.\n"
                                                                      "Leave empty for calculation using NoiseEstimation in Pipeline 1 or difference between images in pipelines 2 and 3.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_51.setText(QtGui.QApplication.translate(
            "MainWindow", "Sigma factor (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.linedit_NLsigmaratio.setText(QtGui.QApplication.translate(
            "MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate(
            "MainWindow", "Search Area", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_NLsearcharea.setText(QtGui.QApplication.translate(
            "MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setText(QtGui.QApplication.translate(
            "MainWindow", "Patch Area", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_NLpatcharea.setText(QtGui.QApplication.translate(
            "MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_NLrician.setText(QtGui.QApplication.translate(
            "MainWindow", "Rician", None, QtGui.QApplication.UnicodeUTF8))
        self.CoilSensUnbiasedNL.setText(QtGui.QApplication.translate(
            "MainWindow", "CoilSensUnbiasedNL (In development)", None, QtGui.QApplication.UnicodeUTF8))
        self.MRONLM2.setText(QtGui.QApplication.translate(
            "MainWindow", "MRONLM2", None, QtGui.QApplication.UnicodeUTF8))
        self.PRINLM2.setText(QtGui.QApplication.translate(
            "MainWindow", "PRINLM2", None, QtGui.QApplication.UnicodeUTF8))
        self.AONLM2.setText(QtGui.QApplication.translate(
            "MainWindow", "AONLM2", None, QtGui.QApplication.UnicodeUTF8))
        self.ODCT2.setText(QtGui.QApplication.translate(
            "MainWindow", "ODCT2", None, QtGui.QApplication.UnicodeUTF8))
        self.ONLM2.setText(QtGui.QApplication.translate(
            "MainWindow", "ONLM2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tab_10), QtGui.QApplication.translate(
            "MainWindow", "Non-local means", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("MainWindow", "Coil Sensitivity\n"
                                                           "or B1 image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CoilSensChangeDir.setText(QtGui.QApplication.translate(
            "MainWindow", "Change Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CoilSensChangeFile.setText(QtGui.QApplication.translate(
            "MainWindow", "Change File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_CoilSensClear.setText(QtGui.QApplication.translate(
            "MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QtGui.QApplication.translate(
            "MainWindow", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.Version_tag.setText(QtGui.QApplication.translate(
            "MainWindow", "Agilent2Dicom v2.0.3", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_tag.setText(QtGui.QApplication.translate(
            "MainWindow", "--o--", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate(
            "MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate(
            "MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate(
            "MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate(
            "MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbort.setText(QtGui.QApplication.translate(
            "MainWindow", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbort.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "Ctrl+Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate(
            "MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_FDF_Directory.setText(QtGui.QApplication.translate(
            "MainWindow", "Open FDF Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_FDF_Directory.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F2, Alt+2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_FID_Directory.setText(QtGui.QApplication.translate(
            "MainWindow", "Open FID Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_FID_Directory.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F3, Alt+3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate(
            "MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate(
            "MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChange_DICOM_path.setText(QtGui.QApplication.translate(
            "MainWindow", "Change DICOM path", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChange_DICOM_path.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate(
            "MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert_FDF.setText(QtGui.QApplication.translate(
            "MainWindow", "Convert FDF", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert_FDF.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F4, Alt+4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert_FID.setText(QtGui.QApplication.translate(
            "MainWindow", "Convert FID", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert_FID.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F5, Alt+5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_Dicom.setText(QtGui.QApplication.translate(
            "MainWindow", "Check Dicom", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_Dicom.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F6, Alt+6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Dicom.setText(QtGui.QApplication.translate(
            "MainWindow", "View Dicom", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Dicom.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F7, Alt+7", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSend_to_DaRIS.setText(QtGui.QApplication.translate(
            "MainWindow", "Send to DaRIS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSend_to_DaRIS.setShortcut(QtGui.QApplication.translate(
            "MainWindow", "F8, Ctrl+8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Filter_Outputs_to_Nifti.setText(QtGui.QApplication.translate(
            "MainWindow", "Save Filter Outputs to Nifti", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Filter_Outputs_to_Nifti.setToolTip(QtGui.QApplication.translate(
            "MainWindow", "Save Filter Outputs to skeleton Nifti.  Nifti will not have pixel dimensions or correct orientation.  Only filter magnitude is saved.", None, QtGui.QApplication.UnicodeUTF8))
