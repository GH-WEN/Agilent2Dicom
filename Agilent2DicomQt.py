# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agilent2DicomQt.ui'
#
# Created: Thu Mar  5 09:59:11 2015
#      by: PyQt4 UI code generator 4.11
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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1146, 611)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_fdf_2 = QtGui.QWidget()
        self.tab_fdf_2.setObjectName(_fromUtf8("tab_fdf_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_fdf_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton_changefdf = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_changefdf.setObjectName(
            _fromUtf8("pushButton_changefdf"))
        self.gridLayout_4.addWidget(self.pushButton_changefdf, 0, 4, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_fdf_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab_fdf_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_4.addWidget(self.label_16, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_fdf_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 1, 1, 1)
        self.pushButton_changedicom = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_changedicom.setObjectName(
            _fromUtf8("pushButton_changedicom"))
        self.gridLayout_4.addWidget(self.pushButton_changedicom, 1, 4, 1, 1)
        self.lineEdit_darisid = QtGui.QLineEdit(self.tab_fdf_2)
        self.lineEdit_darisid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_darisid.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_darisid.setObjectName(_fromUtf8("lineEdit_darisid"))
        self.gridLayout_4.addWidget(self.lineEdit_darisid, 2, 3, 1, 1)
        self.lineEdit_fdfpath = QtGui.QLineEdit(self.tab_fdf_2)
        self.lineEdit_fdfpath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_fdfpath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_fdfpath.setObjectName(_fromUtf8("lineEdit_fdfpath"))
        self.gridLayout_4.addWidget(self.lineEdit_fdfpath, 0, 3, 1, 1)
        self.lineEdit_dicompath = QtGui.QLineEdit(self.tab_fdf_2)
        self.lineEdit_dicompath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_dicompath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_dicompath.setObjectName(_fromUtf8("lineEdit_dicompath"))
        self.gridLayout_4.addWidget(self.lineEdit_dicompath, 1, 3, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 5, 3, 1, 1)
        self.Multiecho_2 = QtGui.QTabWidget(self.tab_fdf_2)
        self.Multiecho_2.setEnabled(True)
        self.Multiecho_2.setObjectName(_fromUtf8("Multiecho_2"))
        self.tab_generic_2 = QtGui.QWidget()
        self.tab_generic_2.setObjectName(_fromUtf8("tab_generic_2"))
        self.layoutWidget = QtGui.QWidget(self.tab_generic_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 168, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.checkBox_debugging = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_debugging.setObjectName(_fromUtf8("checkBox_debugging"))
        self.gridLayout_7.addWidget(self.checkBox_debugging, 0, 0, 1, 1)
        self.checkBox_nodcmulti = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_nodcmulti.setObjectName(_fromUtf8("checkBox_nodcmulti"))
        self.gridLayout_7.addWidget(self.checkBox_nodcmulti, 1, 0, 1, 1)
        self.Multiecho_2.addTab(self.tab_generic_2, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.Multiecho_2, 4, 3, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.tab_fdf_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 917, 187))
        self.scrollAreaWidgetContents.setObjectName(
            _fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.FDFprocparInfo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.FDFprocparInfo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.FDFprocparInfo.setObjectName(_fromUtf8("FDFprocparInfo"))
        self.verticalLayout_15.addWidget(self.FDFprocparInfo)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 3, 3, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pushButton_convert = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_convert.setObjectName(_fromUtf8("pushButton_convert"))
        self.verticalLayout_4.addWidget(self.pushButton_convert)
        self.pushButton_check = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_check.setEnabled(False)
        self.pushButton_check.setObjectName(_fromUtf8("pushButton_check"))
        self.verticalLayout_4.addWidget(self.pushButton_check)
        self.pushButton_view = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_view.setEnabled(False)
        self.pushButton_view.setObjectName(_fromUtf8("pushButton_view"))
        self.verticalLayout_4.addWidget(self.pushButton_view)
        self.pushButton_send2daris = QtGui.QPushButton(self.tab_fdf_2)
        self.pushButton_send2daris.setEnabled(False)
        self.pushButton_send2daris.setObjectName(
            _fromUtf8("pushButton_send2daris"))
        self.verticalLayout_4.addWidget(self.pushButton_send2daris)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 4, 4, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_fdf_2, _fromUtf8(""))
        self.tab_fid_2 = QtGui.QWidget()
        self.tab_fid_2.setObjectName(_fromUtf8("tab_fid_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_fid_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.label_22 = QtGui.QLabel(self.tab_fid_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_11.addWidget(self.label_22, 2, 1, 1, 1)
        self.pushButton_changefid = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_changefid.setObjectName(
            _fromUtf8("pushButton_changefid"))
        self.gridLayout_11.addWidget(self.pushButton_changefid, 0, 3, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_fid_2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_11.addWidget(self.label_24, 0, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_fid_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_11.addWidget(self.label_27, 1, 1, 1, 1)
        self.pushButton_changedicom2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_changedicom2.setObjectName(
            _fromUtf8("pushButton_changedicom2"))
        self.gridLayout_11.addWidget(self.pushButton_changedicom2, 1, 3, 1, 1)
        self.lineEdit_darisid2 = QtGui.QLineEdit(self.tab_fid_2)
        self.lineEdit_darisid2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_darisid2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_darisid2.setObjectName(_fromUtf8("lineEdit_darisid2"))
        self.gridLayout_11.addWidget(self.lineEdit_darisid2, 2, 2, 1, 1)
        self.lineEdit_fidpath = QtGui.QLineEdit(self.tab_fid_2)
        self.lineEdit_fidpath.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_fidpath.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_fidpath.setObjectName(_fromUtf8("lineEdit_fidpath"))
        self.gridLayout_11.addWidget(self.lineEdit_fidpath, 0, 2, 1, 1)
        self.lineEdit_dicompath2 = QtGui.QLineEdit(self.tab_fid_2)
        self.lineEdit_dicompath2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_dicompath2.setText(_fromUtf8(""))
        self.lineEdit_dicompath2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_dicompath2.setObjectName(
            _fromUtf8("lineEdit_dicompath2"))
        self.gridLayout_11.addWidget(self.lineEdit_dicompath2, 1, 2, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.pushButton_convertfid = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_convertfid.setObjectName(
            _fromUtf8("pushButton_convertfid"))
        self.verticalLayout_5.addWidget(self.pushButton_convertfid)
        self.pushButton_check2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_check2.setEnabled(False)
        self.pushButton_check2.setObjectName(_fromUtf8("pushButton_check2"))
        self.verticalLayout_5.addWidget(self.pushButton_check2)
        self.pushButton_view2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_view2.setEnabled(False)
        self.pushButton_view2.setObjectName(_fromUtf8("pushButton_view2"))
        self.verticalLayout_5.addWidget(self.pushButton_view2)
        self.pushButton_send2daris2 = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_send2daris2.setEnabled(False)
        self.pushButton_send2daris2.setObjectName(
            _fromUtf8("pushButton_send2daris2"))
        self.verticalLayout_5.addWidget(self.pushButton_send2daris2)
        self.gridLayout_11.addLayout(self.verticalLayout_5, 4, 3, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_fid_2)
        self.tabWidget_3.setEnabled(True)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.tab_7)
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(
            _fromUtf8("horizontalLayout_35"))
        self.checkBox_magn = QtGui.QCheckBox(self.tab_7)
        self.checkBox_magn.setEnabled(True)
        self.checkBox_magn.setCheckable(True)
        self.checkBox_magn.setChecked(True)
        self.checkBox_magn.setObjectName(_fromUtf8("checkBox_magn"))
        self.horizontalLayout_35.addWidget(self.checkBox_magn)
        self.checkBox_pha = QtGui.QCheckBox(self.tab_7)
        self.checkBox_pha.setObjectName(_fromUtf8("checkBox_pha"))
        self.horizontalLayout_35.addWidget(self.checkBox_pha)
        self.gridLayout_2.addLayout(self.horizontalLayout_35, 5, 0, 1, 1)
        self.line = QtGui.QFrame(self.tab_7)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 8, 0, 1, 1)
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName(
            _fromUtf8("horizontalLayout_36"))
        self.checkBox_reimag = QtGui.QCheckBox(self.tab_7)
        self.checkBox_reimag.setObjectName(_fromUtf8("checkBox_reimag"))
        self.horizontalLayout_36.addWidget(self.checkBox_reimag)
        self.checkBox_ksp = QtGui.QCheckBox(self.tab_7)
        self.checkBox_ksp.setObjectName(_fromUtf8("checkBox_ksp"))
        self.horizontalLayout_36.addWidget(self.checkBox_ksp)
        self.gridLayout_2.addLayout(self.horizontalLayout_36, 6, 0, 1, 1)
        self.checkBox_nifti = QtGui.QCheckBox(self.tab_7)
        self.checkBox_nifti.setObjectName(_fromUtf8("checkBox_nifti"))
        self.gridLayout_2.addWidget(self.checkBox_nifti, 7, 0, 1, 1)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(
            _fromUtf8("horizontalLayout_37"))
        self.checkBox_reimag_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_reimag_raw.setObjectName(
            _fromUtf8("checkBox_reimag_raw"))
        self.horizontalLayout_37.addWidget(self.checkBox_reimag_raw)
        self.checkBox_ksp_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_ksp_raw.setObjectName(_fromUtf8("checkBox_ksp_raw"))
        self.horizontalLayout_37.addWidget(self.checkBox_ksp_raw)
        self.gridLayout_2.addLayout(self.horizontalLayout_37, 3, 0, 1, 1)
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName(
            _fromUtf8("horizontalLayout_38"))
        self.checkBox_magn_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_magn_raw.setEnabled(True)
        self.checkBox_magn_raw.setCheckable(True)
        self.checkBox_magn_raw.setChecked(True)
        self.checkBox_magn_raw.setObjectName(_fromUtf8("checkBox_magn_raw"))
        self.horizontalLayout_38.addWidget(self.checkBox_magn_raw)
        self.checkBox_pha_raw = QtGui.QCheckBox(self.tab_7)
        self.checkBox_pha_raw.setObjectName(_fromUtf8("checkBox_pha_raw"))
        self.horizontalLayout_38.addWidget(self.checkBox_pha_raw)
        self.gridLayout_2.addLayout(self.horizontalLayout_38, 2, 0, 1, 1)
        self.label_36 = QtGui.QLabel(self.tab_7)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_2.addWidget(self.label_36, 4, 0, 1, 1)
        self.label_38 = QtGui.QLabel(self.tab_7)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_2.addWidget(self.label_38, 1, 0, 1, 1)
        self.verticalLayout_22.addLayout(self.gridLayout_2)
        self.tabWidget_3.addTab(self.tab_7, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.gridLayout_13 = QtGui.QGridLayout()
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_29.setObjectName(
            _fromUtf8("horizontalLayout_29"))
        self.gridLayout_13.addLayout(self.horizontalLayout_29, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox_kspgaussian = QtGui.QCheckBox(self.tab_2)
        self.checkBox_kspgaussian.setObjectName(
            _fromUtf8("checkBox_kspgaussian"))
        self.horizontalLayout_4.addWidget(self.checkBox_kspgaussian)
        self.checkBox_kspgaussshift = QtGui.QCheckBox(self.tab_2)
        self.checkBox_kspgaussshift.setObjectName(
            _fromUtf8("checkBox_kspgaussshift"))
        self.horizontalLayout_4.addWidget(self.checkBox_kspgaussshift)
        self.checkBox_kspgauss_super = QtGui.QCheckBox(self.tab_2)
        self.checkBox_kspgauss_super.setObjectName(
            _fromUtf8("checkBox_kspgauss_super"))
        self.horizontalLayout_4.addWidget(self.checkBox_kspgauss_super)
        self.gridLayout_13.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_40.setObjectName(
            _fromUtf8("horizontalLayout_40"))
        self.label_39 = QtGui.QLabel(self.tab_2)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.horizontalLayout_40.addWidget(self.label_39)
        spacerItem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem)
        self.lineEdit_gfsigma = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_gfsigma.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_gfsigma.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_gfsigma.setObjectName(_fromUtf8("lineEdit_gfsigma"))
        self.horizontalLayout_40.addWidget(self.lineEdit_gfsigma)
        self.comboBox_kspgauss_sigunit = QtGui.QComboBox(self.tab_2)
        self.comboBox_kspgauss_sigunit.setObjectName(
            _fromUtf8("comboBox_kspgauss_sigunit"))
        self.comboBox_kspgauss_sigunit.addItem(_fromUtf8(""))
        self.comboBox_kspgauss_sigunit.addItem(_fromUtf8(""))
        self.comboBox_kspgauss_sigunit.addItem(_fromUtf8(""))
        self.horizontalLayout_40.addWidget(self.comboBox_kspgauss_sigunit)
        self.gridLayout_13.addLayout(self.horizontalLayout_40, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.gridLayout_13.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem2, 3, 0, 1, 1)
        self.verticalLayout_16.addLayout(self.gridLayout_13)
        self.tabWidget_3.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.checkBox_kspepa = QtGui.QCheckBox(self.tab)
        self.checkBox_kspepa.setObjectName(_fromUtf8("checkBox_kspepa"))
        self.horizontalLayout_9.addWidget(self.checkBox_kspepa)
        self.checkBox_kspepashift = QtGui.QCheckBox(self.tab)
        self.checkBox_kspepashift.setObjectName(
            _fromUtf8("checkBox_kspepashift"))
        self.horizontalLayout_9.addWidget(self.checkBox_kspepashift)
        self.checkBox_kspepa_super = QtGui.QCheckBox(self.tab)
        self.checkBox_kspepa_super.setObjectName(
            _fromUtf8("checkBox_kspepa_super"))
        self.horizontalLayout_9.addWidget(self.checkBox_kspepa_super)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.lineEdit_kspepa_band = QtGui.QLineEdit(self.tab)
        self.lineEdit_kspepa_band.setObjectName(
            _fromUtf8("lineEdit_kspepa_band"))
        self.horizontalLayout_7.addWidget(self.lineEdit_kspepa_band)
        self.comboBox_kspepa_scaleunit = QtGui.QComboBox(self.tab)
        self.comboBox_kspepa_scaleunit.setObjectName(
            _fromUtf8("comboBox_kspepa_scaleunit"))
        self.comboBox_kspepa_scaleunit.addItem(_fromUtf8(""))
        self.comboBox_kspepa_scaleunit.addItem(_fromUtf8(""))
        self.comboBox_kspepa_scaleunit.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.comboBox_kspepa_scaleunit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem4 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.verticalLayout_12.addLayout(self.verticalLayout_6)
        self.tabWidget_3.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_28.setObjectName(
            _fromUtf8("horizontalLayout_28"))
        self.gridLayout_12.addLayout(self.horizontalLayout_28, 2, 1, 1, 1)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_32.setObjectName(
            _fromUtf8("horizontalLayout_32"))
        self.label_30 = QtGui.QLabel(self.tab_3)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_32.addWidget(self.label_30)
        spacerItem5 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem5)
        self.lineEdit_gorder = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_gorder.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_gorder.setObjectName(_fromUtf8("lineEdit_gorder"))
        self.horizontalLayout_32.addWidget(self.lineEdit_gorder)
        self.gridLayout_12.addLayout(self.horizontalLayout_32, 3, 0, 1, 1)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_33.setObjectName(
            _fromUtf8("horizontalLayout_33"))
        self.label_31 = QtGui.QLabel(self.tab_3)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_33.addWidget(self.label_31)
        spacerItem6 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem6)
        self.lineEdit_gsigma = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_gsigma.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_gsigma.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_gsigma.setObjectName(_fromUtf8("lineEdit_gsigma"))
        self.horizontalLayout_33.addWidget(self.lineEdit_gsigma)
        self.comboBox_gauss_sigmascale = QtGui.QComboBox(self.tab_3)
        self.comboBox_gauss_sigmascale.setObjectName(
            _fromUtf8("comboBox_gauss_sigmascale"))
        self.comboBox_gauss_sigmascale.addItem(_fromUtf8(""))
        self.comboBox_gauss_sigmascale.addItem(_fromUtf8(""))
        self.comboBox_gauss_sigmascale.addItem(_fromUtf8(""))
        self.horizontalLayout_33.addWidget(self.comboBox_gauss_sigmascale)
        self.gridLayout_12.addLayout(self.horizontalLayout_33, 2, 0, 1, 1)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_34.setObjectName(
            _fromUtf8("horizontalLayout_34"))
        self.label_32 = QtGui.QLabel(self.tab_3)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_34.addWidget(self.label_32)
        self.reflect = QtGui.QRadioButton(self.tab_3)
        self.reflect.setChecked(True)
        self.reflect.setObjectName(_fromUtf8("reflect"))
        self.horizontalLayout_34.addWidget(self.reflect)
        self.nearest = QtGui.QRadioButton(self.tab_3)
        self.nearest.setChecked(False)
        self.nearest.setObjectName(_fromUtf8("nearest"))
        self.horizontalLayout_34.addWidget(self.nearest)
        self.wrap = QtGui.QRadioButton(self.tab_3)
        self.wrap.setObjectName(_fromUtf8("wrap"))
        self.horizontalLayout_34.addWidget(self.wrap)
        self.mirror = QtGui.QRadioButton(self.tab_3)
        self.mirror.setObjectName(_fromUtf8("mirror"))
        self.horizontalLayout_34.addWidget(self.mirror)
        spacerItem7 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem7)
        self.gridLayout_12.addLayout(self.horizontalLayout_34, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_gaussian3D = QtGui.QCheckBox(self.tab_3)
        self.checkBox_gaussian3D.setObjectName(
            _fromUtf8("checkBox_gaussian3D"))
        self.horizontalLayout.addWidget(self.checkBox_gaussian3D)
        self.checkBox_gaussian2D = QtGui.QCheckBox(self.tab_3)
        self.checkBox_gaussian2D.setObjectName(
            _fromUtf8("checkBox_gaussian2D"))
        self.horizontalLayout.addWidget(self.checkBox_gaussian2D)
        self.gridLayout_12.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem8, 5, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_12)
        self.tabWidget_3.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.checkBox_median = QtGui.QCheckBox(self.tab_4)
        self.checkBox_median.setObjectName(_fromUtf8("checkBox_median"))
        self.verticalLayout_9.addWidget(self.checkBox_median)
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName(
            _fromUtf8("horizontalLayout_41"))
        self.label_33 = QtGui.QLabel(self.tab_4)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_41.addWidget(self.label_33)
        spacerItem9 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem9)
        self.lineEdit_median_size = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_median_size.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_median_size.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_median_size.setObjectName(
            _fromUtf8("lineEdit_median_size"))
        self.horizontalLayout_41.addWidget(self.lineEdit_median_size)
        self.verticalLayout_9.addLayout(self.horizontalLayout_41)
        spacerItem10 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.verticalLayout_14.addLayout(self.verticalLayout_9)
        self.tabWidget_3.addTab(self.tab_4, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setEnabled(True)
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.checkBox_wiener = QtGui.QCheckBox(self.tab_8)
        self.checkBox_wiener.setEnabled(True)
        self.checkBox_wiener.setObjectName(_fromUtf8("checkBox_wiener"))
        self.verticalLayout_10.addWidget(self.checkBox_wiener)
        self.horizontalLayout_42 = QtGui.QHBoxLayout()
        self.horizontalLayout_42.setObjectName(
            _fromUtf8("horizontalLayout_42"))
        self.label_34 = QtGui.QLabel(self.tab_8)
        self.label_34.setEnabled(True)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout_42.addWidget(self.label_34)
        spacerItem11 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_42.addItem(spacerItem11)
        self.lineEdit_wiener_size = QtGui.QLineEdit(self.tab_8)
        self.lineEdit_wiener_size.setEnabled(True)
        self.lineEdit_wiener_size.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_wiener_size.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_wiener_size.setObjectName(
            _fromUtf8("lineEdit_wiener_size"))
        self.horizontalLayout_42.addWidget(self.lineEdit_wiener_size)
        self.verticalLayout_10.addLayout(self.horizontalLayout_42)
        self.horizontalLayout_43 = QtGui.QHBoxLayout()
        self.horizontalLayout_43.setObjectName(
            _fromUtf8("horizontalLayout_43"))
        self.label_35 = QtGui.QLabel(self.tab_8)
        self.label_35.setEnabled(True)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalLayout_43.addWidget(self.label_35)
        spacerItem12 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem12)
        self.lineEdit_wiener_noise = QtGui.QLineEdit(self.tab_8)
        self.lineEdit_wiener_noise.setEnabled(True)
        self.lineEdit_wiener_noise.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_wiener_noise.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_wiener_noise.setObjectName(
            _fromUtf8("lineEdit_wiener_noise"))
        self.horizontalLayout_43.addWidget(self.lineEdit_wiener_noise)
        self.verticalLayout_10.addLayout(self.horizontalLayout_43)
        spacerItem13 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem13)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.tabWidget_3.addTab(self.tab_8, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_30.setObjectName(
            _fromUtf8("horizontalLayout_30"))
        self.gridLayout_14.addLayout(self.horizontalLayout_30, 2, 1, 1, 1)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_39.setObjectName(
            _fromUtf8("horizontalLayout_39"))
        self.label_37 = QtGui.QLabel(self.tab_5)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.horizontalLayout_39.addWidget(self.label_37)
        spacerItem14 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem14)
        self.gridLayout_14.addLayout(self.horizontalLayout_39, 3, 0, 1, 1)
        self.horizontalLayout_45 = QtGui.QHBoxLayout()
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_45.setObjectName(
            _fromUtf8("horizontalLayout_45"))
        self.label_41 = QtGui.QLabel(self.tab_5)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.horizontalLayout_45.addWidget(self.label_41)
        spacerItem15 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem15)
        self.lineEdit_epaband = QtGui.QLineEdit(self.tab_5)
        self.lineEdit_epaband.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_epaband.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_epaband.setObjectName(_fromUtf8("lineEdit_epaband"))
        self.horizontalLayout_45.addWidget(self.lineEdit_epaband)
        self.comboBox_epabandwidth = QtGui.QComboBox(self.tab_5)
        self.comboBox_epabandwidth.setObjectName(
            _fromUtf8("comboBox_epabandwidth"))
        self.comboBox_epabandwidth.addItem(_fromUtf8(""))
        self.comboBox_epabandwidth.addItem(_fromUtf8(""))
        self.comboBox_epabandwidth.addItem(_fromUtf8(""))
        self.horizontalLayout_45.addWidget(self.comboBox_epabandwidth)
        self.gridLayout_14.addLayout(self.horizontalLayout_45, 2, 0, 1, 1)
        self.horizontalLayout_46 = QtGui.QHBoxLayout()
        self.horizontalLayout_46.setSpacing(5)
        self.horizontalLayout_46.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_46.setObjectName(
            _fromUtf8("horizontalLayout_46"))
        self.label_42 = QtGui.QLabel(self.tab_5)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.horizontalLayout_46.addWidget(self.label_42)
        self.reflect_epa = QtGui.QRadioButton(self.tab_5)
        self.reflect_epa.setChecked(True)
        self.reflect_epa.setObjectName(_fromUtf8("reflect_epa"))
        self.horizontalLayout_46.addWidget(self.reflect_epa)
        self.nearest_epa = QtGui.QRadioButton(self.tab_5)
        self.nearest_epa.setChecked(False)
        self.nearest_epa.setObjectName(_fromUtf8("nearest_epa"))
        self.horizontalLayout_46.addWidget(self.nearest_epa)
        self.wrap_epa = QtGui.QRadioButton(self.tab_5)
        self.wrap_epa.setObjectName(_fromUtf8("wrap_epa"))
        self.horizontalLayout_46.addWidget(self.wrap_epa)
        self.mirror_epa = QtGui.QRadioButton(self.tab_5)
        self.mirror_epa.setObjectName(_fromUtf8("mirror_epa"))
        self.horizontalLayout_46.addWidget(self.mirror_epa)
        spacerItem16 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem16)
        self.gridLayout_14.addLayout(self.horizontalLayout_46, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.checkBox_epanechnikov3D = QtGui.QCheckBox(self.tab_5)
        self.checkBox_epanechnikov3D.setObjectName(
            _fromUtf8("checkBox_epanechnikov3D"))
        self.horizontalLayout_5.addWidget(self.checkBox_epanechnikov3D)
        self.checkBox_epanechnikov2D = QtGui.QCheckBox(self.tab_5)
        self.checkBox_epanechnikov2D.setEnabled(True)
        self.checkBox_epanechnikov2D.setObjectName(
            _fromUtf8("checkBox_epanechnikov2D"))
        self.horizontalLayout_5.addWidget(self.checkBox_epanechnikov2D)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem17, 5, 0, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_14)
        self.tabWidget_3.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(
            _fromUtf8("horizontalLayout_10"))
        self.checkBox_stdev_cplx = QtGui.QCheckBox(self.tab_6)
        self.checkBox_stdev_cplx.setObjectName(
            _fromUtf8("checkBox_stdev_cplx"))
        self.horizontalLayout_10.addWidget(self.checkBox_stdev_cplx)
        self.checkBox_stdev_magn = QtGui.QCheckBox(self.tab_6)
        self.checkBox_stdev_magn.setObjectName(
            _fromUtf8("checkBox_stdev_magn"))
        self.horizontalLayout_10.addWidget(self.checkBox_stdev_magn)
        self.checkBox_stdev_phase = QtGui.QCheckBox(self.tab_6)
        self.checkBox_stdev_phase.setObjectName(
            _fromUtf8("checkBox_stdev_phase"))
        self.horizontalLayout_10.addWidget(self.checkBox_stdev_phase)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(
            _fromUtf8("horizontalLayout_11"))
        self.stdev_window_size_label = QtGui.QLabel(self.tab_6)
        self.stdev_window_size_label.setObjectName(
            _fromUtf8("stdev_window_size_label"))
        self.horizontalLayout_11.addWidget(self.stdev_window_size_label)
        spacerItem18 = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem18)
        self.stdev_window_size = QtGui.QLineEdit(self.tab_6)
        self.stdev_window_size.setObjectName(_fromUtf8("stdev_window_size"))
        self.horizontalLayout_11.addWidget(self.stdev_window_size)
        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 2, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        self.tabWidget_3.addTab(self.tab_6, _fromUtf8(""))
        self.verticalLayout_8.addWidget(self.tabWidget_3)
        self.gridLayout_11.addLayout(self.verticalLayout_8, 4, 2, 1, 1)
        self.scrollArea_4 = QtGui.QScrollArea(self.tab_fid_2)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName(_fromUtf8("scrollArea_4"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(
            QtCore.QRect(0, 0, 917, 112))
        self.scrollAreaWidgetContents_4.setObjectName(
            _fromUtf8("scrollAreaWidgetContents_4"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(
            self.scrollAreaWidgetContents_4)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.FIDprocparInfo = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.FIDprocparInfo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.FIDprocparInfo.setObjectName(_fromUtf8("FIDprocparInfo"))
        self.verticalLayout_21.addWidget(self.FIDprocparInfo)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_11.addWidget(self.scrollArea_4, 3, 2, 1, 1)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        spacerItem20 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem20)
        self.pushButton_CleanUpDicoms = QtGui.QPushButton(self.tab_fid_2)
        self.pushButton_CleanUpDicoms.setObjectName(
            _fromUtf8("pushButton_CleanUpDicoms"))
        self.verticalLayout_18.addWidget(self.pushButton_CleanUpDicoms)
        self.gridLayout_11.addLayout(self.verticalLayout_18, 3, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_11)
        self.tabWidget.addTab(self.tab_fid_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Version_tag = QtGui.QLabel(self.centralwidget)
        self.Version_tag.setFrameShadow(QtGui.QFrame.Sunken)
        self.Version_tag.setObjectName(_fromUtf8("Version_tag"))
        self.horizontalLayout_3.addWidget(self.Version_tag)
        self.bottom_tag = QtGui.QLabel(self.centralwidget)
        self.bottom_tag.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bottom_tag.setFrameShape(QtGui.QFrame.NoFrame)
        self.bottom_tag.setFrameShadow(QtGui.QFrame.Sunken)
        self.bottom_tag.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bottom_tag.setOpenExternalLinks(True)
        self.bottom_tag.setObjectName(_fromUtf8("bottom_tag"))
        self.horizontalLayout_3.addWidget(self.bottom_tag)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbort = QtGui.QAction(MainWindow)
        self.actionAbort.setObjectName(_fromUtf8("actionAbort"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionOpen_FDF_Directory = QtGui.QAction(MainWindow)
        self.actionOpen_FDF_Directory.setObjectName(
            _fromUtf8("actionOpen_FDF_Directory"))
        self.actionOpen_FID_Directory = QtGui.QAction(MainWindow)
        self.actionOpen_FID_Directory.setObjectName(
            _fromUtf8("actionOpen_FID_Directory"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionChange_DICOM_path = QtGui.QAction(MainWindow)
        self.actionChange_DICOM_path.setObjectName(
            _fromUtf8("actionChange_DICOM_path"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionConvert_FDF = QtGui.QAction(MainWindow)
        self.actionConvert_FDF.setObjectName(_fromUtf8("actionConvert_FDF"))
        self.actionConvert_FID = QtGui.QAction(MainWindow)
        self.actionConvert_FID.setObjectName(_fromUtf8("actionConvert_FID"))
        self.actionCheck_Dicom = QtGui.QAction(MainWindow)
        self.actionCheck_Dicom.setObjectName(_fromUtf8("actionCheck_Dicom"))
        self.actionView_Dicom = QtGui.QAction(MainWindow)
        self.actionView_Dicom.setObjectName(_fromUtf8("actionView_Dicom"))
        self.actionSend_to_DaRIS = QtGui.QAction(MainWindow)
        self.actionSend_to_DaRIS.setObjectName(
            _fromUtf8("actionSend_to_DaRIS"))
        self.actionSave_Filter_Outputs_to_Nifti = QtGui.QAction(MainWindow)
        self.actionSave_Filter_Outputs_to_Nifti.setObjectName(
            _fromUtf8("actionSave_Filter_Outputs_to_Nifti"))
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
        self.tabWidget.setCurrentIndex(1)
        self.Multiecho_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(3)
        QtCore.QObject.connect(self.actionOpen_FDF_Directory, QtCore.SIGNAL(
            _fromUtf8("triggered()")), self.pushButton_changefdf.click)
        QtCore.QObject.connect(
            self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionConvert_FDF, QtCore.SIGNAL(
            _fromUtf8("triggered()")), self.pushButton_convert.click)
        QtCore.QObject.connect(self.actionView_Dicom, QtCore.SIGNAL(
            _fromUtf8("triggered()")), self.pushButton_view.click)
        QtCore.QObject.connect(self.actionSend_to_DaRIS, QtCore.SIGNAL(
            _fromUtf8("triggered()")), self.pushButton_send2daris.click)
        QtCore.QObject.connect(self.actionOpen_FID_Directory, QtCore.SIGNAL(
            _fromUtf8("triggered()")), self.pushButton_changefid.click)
        QtCore.QObject.connect(self.actionConvert_FID, QtCore.SIGNAL(
            _fromUtf8("triggered()")), self.pushButton_convertfid.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Agilent2Dicom: MBI\'s Agilent 9.4T MR Image Analysis and Dicom Converter Application (1.8.2)", None))
        self.pushButton_changefdf.setToolTip(
            _translate("MainWindow", "Change the FDF input directory", None))
        self.pushButton_changefdf.setText(
            _translate("MainWindow", "Change Dir", None))
        self.label_13.setText(_translate("MainWindow", "FDF folder", None))
        self.label_16.setText(_translate("MainWindow", "Dicom folder", None))
        self.label_17.setText(_translate("MainWindow", "DaRIS ID", None))
        self.pushButton_changedicom.setToolTip(_translate(
            "MainWindow", "Change the output DICOM directory.  Only do this if the automatic folder name is already taken.", None))
        self.pushButton_changedicom.setText(
            _translate("MainWindow", "Change Dir", None))
        self.lineEdit_darisid.setToolTip(_translate(
            "MainWindow", "DaRIS ID string should automatically update with new FDF folder", None))
        self.checkBox_debugging.setToolTip(
            _translate("MainWindow", "Display more verbose debugging", None))
        self.checkBox_debugging.setText(
            _translate("MainWindow", "Show debugging", None))
        self.checkBox_nodcmulti.setToolTip(_translate(
            "MainWindow", "Do not convert 2D slices to enhance DICOM format", None))
        self.checkBox_nodcmulti.setText(
            _translate("MainWindow", "Keep 2D DICOM slices", None))
        self.Multiecho_2.setTabText(self.Multiecho_2.indexOf(
            self.tab_generic_2), _translate("MainWindow", "Options", None))
        self.FDFprocparInfo.setText(
            _translate("MainWindow", "Metatdata information: ", None))
        self.pushButton_convert.setToolTip(
            _translate("MainWindow", "Convert FDF folder to DICOM using fdf2dcm.sh", None))
        self.pushButton_convert.setText(
            _translate("MainWindow", "Convert", None))
        self.pushButton_check.setToolTip(_translate(
            "MainWindow", "Check dicom output using Dicom3Tool\'s DCIODVFY", None))
        self.pushButton_check.setText(_translate("MainWindow", "Check", None))
        self.pushButton_view.setToolTip(
            _translate("MainWindow", "View dicom output using MRtrix\'s MRVIEW", None))
        self.pushButton_view.setText(_translate("MainWindow", "View", None))
        self.pushButton_send2daris.setToolTip(
            _translate("MainWindow", "Send Dicom folder to DaRIS ", None))
        self.pushButton_send2daris.setText(
            _translate("MainWindow", "Send to DaRIS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_fdf_2), _translate("MainWindow", "FDF converter", None))
        self.label_22.setText(_translate("MainWindow", "DaRIS ID", None))
        self.pushButton_changefid.setToolTip(
            _translate("MainWindow", "Change the input FID directory", None))
        self.pushButton_changefid.setText(
            _translate("MainWindow", "Change Dir", None))
        self.label_24.setText(_translate("MainWindow", "FID folder", None))
        self.label_27.setText(_translate("MainWindow", "Dicom folder", None))
        self.pushButton_changedicom2.setToolTip(
            _translate("MainWindow", "Change the output DICOM directory.", None))
        self.pushButton_changedicom2.setText(
            _translate("MainWindow", "Change Dir", None))
        self.lineEdit_darisid2.setToolTip(_translate(
            "MainWindow", "DaRIS ID generated from header information in FID procpar.  Do not edit unless you know what you are doing!", None))
        self.pushButton_convertfid.setToolTip(
            _translate("MainWindow", "Process FID folder using the fid2dcm.sh script", None))
        self.pushButton_convertfid.setText(
            _translate("MainWindow", "Convert", None))
        self.pushButton_check2.setToolTip(_translate(
            "MainWindow", "Check the dicom outputs using Dicom3Tool\'s DCIODVFY", None))
        self.pushButton_check2.setText(_translate("MainWindow", "Check", None))
        self.pushButton_view2.setToolTip(_translate(
            "MainWindow", "View the filtered and unfiltered images in MRVIEW", None))
        self.pushButton_view2.setText(_translate("MainWindow", "View", None))
        self.pushButton_send2daris2.setToolTip(
            _translate("MainWindow", "Send DICOMs to DaRIS", None))
        self.pushButton_send2daris2.setText(
            _translate("MainWindow", "Send to DaRIS", None))
        self.tabWidget_3.setToolTip(_translate("MainWindow", "Multidimensional Gaussian, Epanechnikov, Median, StDev or Wiener filters.  \n"
                                               "Warning: use identical sigma values on isotropic images only. Non-isotropic values should be based on image size in comma-serarated list", None))
        self.checkBox_magn.setText(
            _translate("MainWindow", "Save Magnitude", None))
        self.checkBox_pha.setText(_translate("MainWindow", "Save Phase", None))
        self.checkBox_reimag.setText(
            _translate("MainWindow", "Save REAL and IMAG", None))
        self.checkBox_ksp.setText(
            _translate("MainWindow", "Save K space data", None))
        self.checkBox_nifti.setText(
            _translate("MainWindow", "Save magnitude as NIFTI (limited header info)", None))
        self.checkBox_reimag_raw.setText(
            _translate("MainWindow", "Save REAL and IMAG", None))
        self.checkBox_ksp_raw.setText(
            _translate("MainWindow", "Save K space data", None))
        self.checkBox_magn_raw.setText(
            _translate("MainWindow", "Save Magnitude", None))
        self.checkBox_pha_raw.setText(
            _translate("MainWindow", "Save Phase", None))
        self.label_36.setToolTip(_translate(
            "MainWindow", "Outputs saved as \"<dicom folder>-<filter type>-<magn or pha or real or imag>.dcm\".  K-space data is saved to MATLAB mat file \"<dicom folder>-<ksp>.mat\"", None))
        self.label_36.setText(
            _translate("MainWindow", "Outputs of filtered image(s)", None))
        self.label_38.setToolTip(_translate(
            "MainWindow", "Outputs saved as \"<dicom folder>-<filter type>-<magn or pha or real or imag>.dcm\".  K-space data is saved to MATLAB mat file \"<dicom folder>-<ksp>.mat\"", None))
        self.label_38.setText(
            _translate("MainWindow", "Outputs of original reconstructed image:", None))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_7), _translate("MainWindow", "Options", None))
        self.checkBox_kspgaussian.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p> KSPACEFILTER gaussian filter of complex 3D image</p><p><br/></p><p>    filtered_magnitude = kspacefilter(realimg, imagimg)</p><p><br/></p><p><br/></p><p>    scipy.ndimage.fourier.fourier_gaussian</p><p><br/></p><p>    scipy.ndimage.fourier.fourier_gaussian(input, sigma, n=-1, axis=-1,</p><p>    output=None)[source]</p><p><br/></p><p>    Multi-dimensional Gaussian fourier filter.</p><p><br/></p><p>    The array is multiplied with the fourier transform of a Gaussian kernel.</p><p><br/></p><p>    Parameters:</p><p>    input : array_like</p><p>    The input array.</p><p>    sigma : float or sequence</p><p><br/></p><p>    The sigma of the Gaussian kernel. If a float, sigma is the same</p><p>    for all axes. If a sequence, sigma has to contain one value for</p><p>    each axis.</p><p><br/></p><p>    n : int, optional</p><p><br/></p><p>    If n is negative (default), then the input is assumed to be the</p><p>    result of a complex fft. If n is larger than or equal to zero, the</p><p>    input is assumed to be the result of a real fft, and n gives the</p><p>    length of the array before transformation along the real transform</p><p>    direction.</p><p><br/></p><p>    axis : int, optional</p><p>    The axis of the real transform.</p><p>    output : ndarray, optional</p><p><br/></p><p>    If given, the result of filtering the input is placed in this array. None</p><p>    is returned in this case.</p><p><br/></p><p>    Returns:</p><p>    fourier_gaussian : ndarray or None</p><p>    The filtered input. If output is given as a parameter, None is returned.</p><p><br/></p></body></html>", None))
        self.checkBox_kspgaussian.setText(_translate("MainWindow", "Use K-space Gaussian filter\n"
                                                     "(Fourier domain)", None))
        self.checkBox_kspgaussshift.setToolTip(
            _translate("MainWindow", "Disable centre-shifting in k-space", None))
        self.checkBox_kspgaussshift.setText(
            _translate("MainWindow", "Disable centre shift ", None))
        self.checkBox_kspgauss_super.setToolTip(_translate("MainWindow", "Use zero padding in k-space to double image resolution. \n"
                                                           "\n"
                                                           "WARNING this will increase 3D volume sizes by a factor of 8.\n"
                                                           "\n"
                                                           "Double-resolution uses zero-filled k-space data to double the resolution of the image. \n"
                                                           "The super-resolution image is saved to NIFTI while the standard is saved to dicom. ", None))
        self.checkBox_kspgauss_super.setText(_translate("MainWindow", "Double-resolution\n"
                                                        "(Saved to NIFTI only)", None))
        self.label_39.setToolTip(_translate("MainWindow", "scalar or sequence of scalars\n"
                                            "\n"
                                            "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.\n"
                                            "\n"
                                            "Effective Fourier domain sigma is calculated as the image size divided by image domain sigma. sigma.", None))
        self.label_39.setText(
            _translate("MainWindow", "Effective Image Domain Sigma", None))
        self.lineEdit_gfsigma.setToolTip(_translate("MainWindow", "scalar or sequence of scalars\n"
                                                    "\n"
                                                    "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.  Default value for isotropic GRE scans is 1/sqrt(2)=0.707.", None))
        self.lineEdit_gfsigma.setText(
            _translate("MainWindow", "0.707,0.707,0.707", None))
        self.comboBox_kspgauss_sigunit.setItemText(
            0, _translate("MainWindow", "unit voxel", None))
        self.comboBox_kspgauss_sigunit.setItemText(
            1, _translate("MainWindow", "in mm", None))
        self.comboBox_kspgauss_sigunit.setItemText(
            2, _translate("MainWindow", "in um", None))
        self.label.setText(_translate("MainWindow", "Actual FT Gaussian sigma\n"
                                      "(matrix size/sigma)", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(
            self.tab_2), _translate("MainWindow", "K-space Gaussian", None))
        self.checkBox_kspepa.setToolTip(_translate(
            "MainWindow", "3D Epanechnikov filter in k-space (Fourier domain).   FFT of image filter used instead of calculated filter.", None))
        self.checkBox_kspepa.setText(_translate("MainWindow", "Use Kspace Epanechnikov filter\n"
                                                "(Fourier domain)", None))
        self.checkBox_kspepashift.setToolTip(
            _translate("MainWindow", "Disable k-space frequency shift", None))
        self.checkBox_kspepashift.setText(
            _translate("MainWindow", "No Shift", None))
        self.checkBox_kspepa_super.setToolTip(_translate("MainWindow", "Use zero padding in k-space to double image resolution. \n"
                                                         "\n"
                                                         "!!!WARNING this will increase 3D volume sizes by a factor of 8.!!!\n"
                                                         "\n"
                                                         "Double-resolution uses zero-filled k-space data to double the resolution of the image. \n"
                                                         "The super-resolution image is saved to NIFTI while the standard is saved to dicom. ", None))
        self.checkBox_kspepa_super.setText(_translate("MainWindow", "Double-resolution\n"
                                                      "(Saved to NIFTI only)", None))
        self.label_2.setText(_translate("MainWindow", "Effective Filter Bandwidth\n"
                                        "(Use Gaussian sigma\n"
                                        " times sqrt(dimension + 4), \n"
                                        "eg. sqrt(7)*sqrt(0.5)=1.8707 )", None))
        self.lineEdit_kspepa_band.setToolTip(_translate(
            "MainWindow", "Bandwidth equivalent in image space.  Comma separated values (no spaces) accepted for non-isotropic slices.", None))
        self.lineEdit_kspepa_band.setText(
            _translate("MainWindow", "1.8708,1.8708,1.8708", None))
        self.comboBox_kspepa_scaleunit.setItemText(
            0, _translate("MainWindow", "unit voxel", None))
        self.comboBox_kspepa_scaleunit.setItemText(
            1, _translate("MainWindow", "mm", None))
        self.comboBox_kspepa_scaleunit.setItemText(
            2, _translate("MainWindow", "um", None))
        self.label_4.setText(_translate("MainWindow", " Note: Complex Fourier domain Epanechnikov filter is generated from complex image domain kernel. \n"
                                        "\n"
                                        "Pseudo super-resolution does not give additional subvoxel information to the image.  It is a complex interpolation for assisting contrast in rendering \n"
                                        "", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(
            self.tab), _translate("MainWindow", "K-space Epanechnikov", None))
        self.label_30.setToolTip(_translate("MainWindow", "order : {0, 1, 2, 3} or sequence from same set, optional\n"
                                            "\n"
                                            "    The order of the filter along each axis is given as a sequence of integers, or as a single number. An order of 0 corresponds to convolution with a Gaussian kernel. An order of 1, 2, or 3 corresponds to convolution with the first, second or third derivatives of a Gaussian. Higher order derivatives are not implemented\n"
                                            "", None))
        self.label_30.setText(_translate("MainWindow", "Order", None))
        self.lineEdit_gorder.setToolTip(_translate("MainWindow", "order : {0, 1, 2, 3} or sequence from same set, optional\n"
                                                   "\n"
                                                   "    The order of the filter along each axis is given as a sequence of integers, \n"
                                                   "or as a single number. An order of 0 corresponds to convolution with a Gaussian \n"
                                                   "kernel. An order of 1, 2, or 3 corresponds to convolution with the first, \n"
                                                   "second or third derivatives of a Gaussian. \n"
                                                   "Higher order derivatives are not implemented\n"
                                                   "", None))
        self.lineEdit_gorder.setText(_translate("MainWindow", "0", None))
        self.label_31.setToolTip(_translate("MainWindow", "scalar or sequence of scalars\n"
                                            "\n"
                                            "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.", None))
        self.label_31.setText(_translate("MainWindow", "Sigma", None))
        self.lineEdit_gsigma.setToolTip(_translate("MainWindow", "scalar or sequence of scalars\n"
                                                   "\n"
                                                   "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.  Default value for isotropic GRE scans is 1/sqrt(2)=0.707.", None))
        self.lineEdit_gsigma.setText(
            _translate("MainWindow", "0.707,0.707,0.707", None))
        self.comboBox_gauss_sigmascale.setItemText(
            0, _translate("MainWindow", "unit voxel", None))
        self.comboBox_gauss_sigmascale.setItemText(
            1, _translate("MainWindow", "in mm", None))
        self.comboBox_gauss_sigmascale.setItemText(
            2, _translate("MainWindow", "in um", None))
        self.label_32.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                            "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.label_32.setText(_translate("MainWindow", "Mode:", None))
        self.reflect.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                           "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to constant.", None))
        self.reflect.setText(_translate("MainWindow", "Reflect", None))
        self.nearest.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                           "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.nearest.setText(_translate("MainWindow", "Nearest", None))
        self.wrap.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                        "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.wrap.setText(_translate("MainWindow", "Wrap", None))
        self.mirror.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                          "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.mirror.setText(_translate("MainWindow", "Mirror", None))
        self.checkBox_gaussian3D.setToolTip(_translate("MainWindow", " scipy.ndimage.filters.gaussian_filter(input, sigma, order=0, output=None, mode=\'reflect\', cval=0.0, truncate=4.0)[source]\n"
                                                       "\n"
                                                       "    Multidimensional Gaussian filter.", None))
        self.checkBox_gaussian3D.setText(
            _translate("MainWindow", "Use 3D Gaussian filter", None))
        self.checkBox_gaussian2D.setToolTip(_translate("MainWindow", "Use Guassian filter on 2D slices. \n"
                                                       "Use the order of the sizes in the information box above to set the sigma values below.", None))
        self.checkBox_gaussian2D.setText(
            _translate("MainWindow", "Use 2D Gaussian filter", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(
            self.tab_3), _translate("MainWindow", "Gaussian", None))
        self.checkBox_median.setToolTip(_translate("MainWindow", "scipy.ndimage.filters.median_filter¶\n"
                                                   "\n"
                                                   "scipy.ndimage.filters.median_filter(input, size=None, footprint=None, output=None, mode=\'reflect\', cval=0.0, origin=0)[source]\n"
                                                   "\n"
                                                   "    Calculates a multidimensional median filter.", None))
        self.checkBox_median.setText(
            _translate("MainWindow", "Use Median Filter", None))
        self.label_33.setToolTip(_translate("MainWindow", "     \n"
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
                                            "", None))
        self.label_33.setText(_translate("MainWindow", "Window Size(s)", None))
        self.lineEdit_median_size.setToolTip(_translate("MainWindow", "     \n"
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
                                                        "", None))
        self.lineEdit_median_size.setText(
            _translate("MainWindow", "5,5,5", None))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Median", None))
        self.checkBox_wiener.setToolTip(_translate("MainWindow", "NOT ENABLED - Speak to MBI Imaging Team\n"
                                                   "\n"
                                                   "scipy.signal.wiener(im, mysize=None, noise=None)\n"
                                                   "\n"
                                                   "    Perform a Wiener filter on an N-dimensional array.\n"
                                                   "\n"
                                                   "    Apply a Wiener filter to the N-dimensional array im.", None))
        self.checkBox_wiener.setText(
            _translate("MainWindow", "Use Wiener Filter", None))
        self.label_34.setToolTip(_translate("MainWindow", "mysize : int or arraylike, optional\n"
                                            "\n"
                                            "    A scalar or an N-length list giving the size of the Wiener filter window in each dimension. Elements of mysize should be odd. If mysize is a scalar, then this scalar is used as the size in each dimension.\n"
                                            "", None))
        self.label_34.setText(
            _translate("MainWindow", " Window Size(s)", None))
        self.lineEdit_wiener_size.setToolTip(_translate("MainWindow", "mysize : int or arraylike, optional\n"
                                                        "\n"
                                                        "    A scalar or an N-length list giving the size of the Wiener filter window in each dimension. Elements of mysize should be odd. If mysize is a scalar, then this scalar is used as the size in each dimension.\n"
                                                        "", None))
        self.lineEdit_wiener_size.setText(
            _translate("MainWindow", "5,5,5", None))
        self.label_35.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>noise: Estimation of noise, Set to 0 for local variance to be used.</p></body></html>", None))
        self.label_35.setText(_translate(
            "MainWindow", "Noise (Est. variance, 0 uses localised variance) ", None))
        self.lineEdit_wiener_noise.setToolTip(_translate("MainWindow", "mysize : int or arraylike, optional\n"
                                                         "\n"
                                                         "    A scalar or an N-length list giving the size of the Wiener filter window in each dimension. Elements of mysize should be odd. If mysize is a scalar, then this scalar is used as the size in each dimension.\n"
                                                         "", None))
        self.lineEdit_wiener_noise.setText(_translate("MainWindow", "0", None))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "Wiener", None))
        self.label_37.setToolTip(_translate("MainWindow", "order : {0, 1, 2, 3} or sequence from same set, optional\n"
                                            "\n"
                                            "    The order of the filter along each axis is given as a sequence of integers, or as a single number. An order of 0 corresponds to convolution with a Gaussian kernel. An order of 1, 2, or 3 corresponds to convolution with the first, second or third derivatives of a Gaussian. Higher order derivatives are not implemented\n"
                                            "", None))
        self.label_37.setText(
            _translate("MainWindow", "bandwidth = gaussian sigma * sqrt(dim + 4) ", None))
        self.label_41.setToolTip(_translate("MainWindow", "scalar or sequence of scalars\n"
                                            "\n"
                                            "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.", None))
        self.label_41.setText(_translate("MainWindow", "Bandwidth", None))
        self.lineEdit_epaband.setToolTip(_translate("MainWindow", "scalar or sequence of scalars\n"
                                                    "\n"
                                                    "    Standard deviation for Gaussian kernel. The standard deviations of the Gaussian filter are given for each axis as a sequence, or as a single number, in which case it is equal for all axes.  Default value for isotropic GRE scans is 1/sqrt(2)=0.707.", None))
        self.lineEdit_epaband.setText(
            _translate("MainWindow", "1.8708,1.8708,1.8708", None))
        self.comboBox_epabandwidth.setItemText(
            0, _translate("MainWindow", "unit voxel", None))
        self.comboBox_epabandwidth.setItemText(
            1, _translate("MainWindow", "in mm", None))
        self.comboBox_epabandwidth.setItemText(
            2, _translate("MainWindow", "in um", None))
        self.label_42.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                            "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.label_42.setText(_translate("MainWindow", "Mode:", None))
        self.reflect_epa.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                               "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.reflect_epa.setText(_translate("MainWindow", "Reflect", None))
        self.nearest_epa.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                               "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.nearest_epa.setText(_translate("MainWindow", "Nearest", None))
        self.wrap_epa.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                            "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.wrap_epa.setText(_translate("MainWindow", "Wrap", None))
        self.mirror_epa.setToolTip(_translate("MainWindow", "mode : {\'reflect\', \'constant\', \'nearest\', \'mirror\', \'wrap\'}, optional\n"
                                              "The mode parameter determines how the array borders are handled, where cval is the value when mode is equal to âconstantâ", None))
        self.mirror_epa.setText(_translate("MainWindow", "Mirror", None))
        self.checkBox_epanechnikov3D.setToolTip(_translate("MainWindow", "Bespoke epanechnikov_filter(input, sigma)\n"
                                                           "\n"
                                                           "    Fast multidimensional Epanechnikov filter.", None))
        self.checkBox_epanechnikov3D.setText(
            _translate("MainWindow", "Use 3D Epanechnikov filter", None))
        self.checkBox_epanechnikov2D.setText(
            _translate("MainWindow", "Use 2D Epanechnikov filter", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(
            self.tab_5), _translate("MainWindow", "Epanechnikov", None))
        self.checkBox_stdev_cplx.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Don\'t use this - use the phase</p></body></html>", None))
        self.checkBox_stdev_cplx.setText(
            _translate("MainWindow", "Use CPLX Std dev filter", None))
        self.checkBox_stdev_magn.setText(
            _translate("MainWindow", "Use Magnitude", None))
        self.checkBox_stdev_phase.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>Localised standard deviation of the image phase</p><p><br/></p></body></html>", None))
        self.checkBox_stdev_phase.setText(
            _translate("MainWindow", "Use Phase", None))
        self.stdev_window_size_label.setText(
            _translate("MainWindow", "Window size (default 5)  ", None))
        self.stdev_window_size.setText(_translate("MainWindow", "5", None))
        self.tabWidget_3.setTabText(
            self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Stdev", None))
        self.FIDprocparInfo.setText(
            _translate("MainWindow", "Metadata display:", None))
        self.pushButton_CleanUpDicoms.setText(
            _translate("MainWindow", "Clean up", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_fid_2), _translate("MainWindow", "FID converter", None))
        self.Version_tag.setText(
            _translate("MainWindow", "Agilent2Dicom v1.8.2", None))
        self.bottom_tag.setText(_translate("MainWindow", "--o--", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.actionAbort.setText(_translate("MainWindow", "Abort", None))
        self.actionAbort.setShortcut(
            _translate("MainWindow", "Ctrl+Space", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.actionOpen_FDF_Directory.setText(
            _translate("MainWindow", "Open FDF Directory", None))
        self.actionOpen_FDF_Directory.setShortcut(
            _translate("MainWindow", "F2, Alt+2", None))
        self.actionOpen_FID_Directory.setText(
            _translate("MainWindow", "Open FID Directory", None))
        self.actionOpen_FID_Directory.setShortcut(
            _translate("MainWindow", "F3, Alt+3", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1", None))
        self.actionChange_DICOM_path.setText(
            _translate("MainWindow", "Change DICOM path", None))
        self.actionChange_DICOM_path.setShortcut(
            _translate("MainWindow", "Ctrl+D", None))
        self.actionPreferences.setText(
            _translate("MainWindow", "Preferences", None))
        self.actionConvert_FDF.setText(
            _translate("MainWindow", "Convert FDF", None))
        self.actionConvert_FDF.setShortcut(
            _translate("MainWindow", "F4, Alt+4", None))
        self.actionConvert_FID.setText(
            _translate("MainWindow", "Convert FID", None))
        self.actionConvert_FID.setShortcut(
            _translate("MainWindow", "F5, Alt+5", None))
        self.actionCheck_Dicom.setText(
            _translate("MainWindow", "Check Dicom", None))
        self.actionCheck_Dicom.setShortcut(
            _translate("MainWindow", "F6, Alt+6", None))
        self.actionView_Dicom.setText(
            _translate("MainWindow", "View Dicom", None))
        self.actionView_Dicom.setShortcut(
            _translate("MainWindow", "F7, Alt+7", None))
        self.actionSend_to_DaRIS.setText(
            _translate("MainWindow", "Send to DaRIS", None))
        self.actionSend_to_DaRIS.setShortcut(
            _translate("MainWindow", "F8, Ctrl+8", None))
        self.actionSave_Filter_Outputs_to_Nifti.setText(
            _translate("MainWindow", "Save Filter Outputs to Nifti", None))
        self.actionSave_Filter_Outputs_to_Nifti.setToolTip(_translate(
            "MainWindow", "Save Filter Outputs to skeleton Nifti.  Nifti will not have pixel dimensions or correct orientation.  Only filter magnitude is saved.", None))
