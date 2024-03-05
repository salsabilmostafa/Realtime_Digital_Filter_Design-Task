from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import sys
from function import ApplicationDirector
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from pyqtgraph import ScatterPlotItem
from math import sqrt
import pyqtgraph as pg


class Ui_Application(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(1079, 665)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "Realtime-filter/Assets/WindowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Application.setWindowIcon(icon)
        Application.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "")

        self.centralwidget = QtWidgets.QWidget(Application)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected {\n"
                                     "    background-color: #000000;\n"
                                     "color:white;\n"
                                     " border: none;\n"
                                     "      padding: 5px 10px;\n"
                                     "     border: 1.2px ;\n"
                                     "border-style: outset;\n"
                                     "  \n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:!selected {\n"
                                     "    background-color:  #ffffff;\n"
                                     "color:black;\n"
                                     " border: none;\n"
                                     "      padding: 5px 10px;\n"
                                     "     border: 1.2px ;\n"
                                     "border-style: outset;\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget::pane {\n"
                                     "    border: none;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.tabWidget.setObjectName("tabWidget")
        self.design_tab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.design_tab.setPalette(palette)
        self.design_tab.setStyleSheet("QGroupBox {\n"
                                      "background-color: #ffffff;\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.design_tab.setObjectName("design_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.design_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.design_box = QtWidgets.QGroupBox(self.design_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.design_box.setFont(font)
        self.design_box.setStyleSheet("border: none;\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.design_box.setObjectName("design_box")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.design_box)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Zplane_box = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Zplane_box.sizePolicy().hasHeightForWidth())
        self.Zplane_box.setSizePolicy(sizePolicy)
        self.Zplane_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Zplane_box.setFont(font)
        self.Zplane_box.setStyleSheet("QGroupBox {\n"
                                      "background-color: #ffffff;\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.Zplane_box.setObjectName("Zplane_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Zplane_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.z_plane = PlotWidget1(self.Zplane_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.z_plane.sizePolicy().hasHeightForWidth())
        self.z_plane.setSizePolicy(sizePolicy)
        self.z_plane.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.z_plane.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.z_plane.setObjectName("z_plane")
        self.verticalLayout_4.addWidget(self.z_plane)
        self.magBox = QtWidgets.QGroupBox(self.Zplane_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.magBox.sizePolicy().hasHeightForWidth())
        self.magBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.magBox.setFont(font)
        self.magBox.setStyleSheet("QGroupBox {\n"
                                  "background-color: #ffffff;\n"
                                  ";\n"
                                  "}\n"
                                  "")
        self.magBox.setObjectName("magBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.magBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.Magnitude_graph = PlotWidget(self.magBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Magnitude_graph.sizePolicy().hasHeightForWidth())
        self.Magnitude_graph.setSizePolicy(sizePolicy)
        self.Magnitude_graph.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Magnitude_graph.setObjectName("Magnitude_graph")
        self.verticalLayout.addWidget(self.Magnitude_graph)
        self.verticalLayout_4.addWidget(self.magBox)
        self.horizontalLayout_10.addWidget(self.Zplane_box)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.preferenceBox = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.preferenceBox.sizePolicy().hasHeightForWidth())
        self.preferenceBox.setSizePolicy(sizePolicy)
        self.preferenceBox.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.preferenceBox.setFont(font)
        self.preferenceBox.setStyleSheet("QGroupBox {\n"
                                         "    \n"
                                         "    background-color:#ffffff;\n"
                                         "  padding: 5px 10px;\n"
                                         "    \n"
                                         "}\n"
                                         "")
        self.preferenceBox.setTitle("")
        self.preferenceBox.setObjectName("preferenceBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.preferenceBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zeros_radioButton = QtWidgets.QRadioButton(self.preferenceBox)
        self.zeros_radioButton.setChecked(True)
        self.zeros_radioButton.setStyleSheet("\n"
                                             "      color: black;\n"
                                             "      border: none;\n"
                                             "      padding: 5px 10px;\n"
                                             "     border: 1.2px solid black;\n"
                                             "border-style: outset;\n"
                                             "\n"
                                             "")
        self.zeros_radioButton.setObjectName("zeros_radioButton")
        self.horizontalLayout_5.addWidget(self.zeros_radioButton)
        self.pole_radioButton = QtWidgets.QRadioButton(self.preferenceBox)
        self.pole_radioButton.setStyleSheet("color: black;\n"
                                            "      border: none;\n"
                                            "      padding: 5px 10px;\n"
                                            "     border: 1.2px solid black;\n"
                                            "border-style: outset;\n"
                                            "")
        self.pole_radioButton.setObjectName("pole_radioButton")
        self.horizontalLayout_5.addWidget(self.pole_radioButton)
        self.gridLayout_9.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.preferenceBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("QGroupBox {\n"
                                    "background-color: #ffffff;\n"
                                    "\n"
                                    " padding: 5px 10px;\n"
                                    "     border: 1.2px ;\n"
                                    "border-style: outset;\n"
                                    "}\n"
                                    "")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.add_conjugates = QtWidgets.QCheckBox(self.groupBox)
        self.add_conjugates.setStyleSheet("background-color: #ffffff;\n"
                                          "      color: black;\n"
                                          "      border: none;\n"
                                          "      padding: 5px 10px;\n"
                                          "     border: 1.2px ;\n"
                                          "border-style: outset;")
        self.add_conjugates.setObjectName("add_conjugates")
        self.horizontalLayout_9.addWidget(self.add_conjugates)
        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(self.preferenceBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox1.sizePolicy().hasHeightForWidth())
        self.groupBox1.setSizePolicy(sizePolicy)
        self.groupBox1.setStyleSheet(" padding: 5px 10px;\n"
                                     "     border: 1.2px ;\n"
                                     "border-style: outset;")
        self.groupBox1.setObjectName("groupBox1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Clear_combobox = QtWidgets.QComboBox(self.groupBox1)
        self.Clear_combobox.setStyleSheet("background-color: #ffffff;\n"
                                          "      color: black;\n"
                                          "      border: none;\n"
                                          "      padding: 5px 10px;\n"
                                          "     border: 1.2px ;\n"
                                          "border-style: outset;")
        self.Clear_combobox.setEditable(True)
        self.Clear_combobox.setObjectName("Clear_combobox")
        self.Clear_combobox.addItem("")
        self.Clear_combobox.addItem("")
        self.Clear_combobox.addItem("")
        self.Clear_combobox.addItem("")
        self.horizontalLayout_4.addWidget(self.Clear_combobox)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)
        self.confirm_button = QtWidgets.QPushButton(self.groupBox1)
        self.confirm_button.setMaximumSize(QtCore.QSize(86, 16777215))
        self.confirm_button.setStyleSheet("background-color: #ffffff;\n"
                                          "      color: black;\n"
                                          "      border: none;\n"
                                          "      padding: 5px 10px;\n"
                                          "     border: 1.2px ;\n"
                                          "border-style: outset;")
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout_8.addWidget(self.confirm_button)
        self.gridLayout_9.addWidget(self.groupBox1, 2, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.preferenceBox)
        self.phasebox = QtWidgets.QGroupBox(self.design_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.phasebox.sizePolicy().hasHeightForWidth())
        self.phasebox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phasebox.setFont(font)
        self.phasebox.setStyleSheet("QGroupBox {\n"
                                    "background-color: #ffffff;\n"
                                    "\n"
                                    "}\n"
                                    "")
        self.phasebox.setObjectName("phasebox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.phasebox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.Phase_graph = PlotWidget(self.phasebox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Phase_graph.sizePolicy().hasHeightForWidth())
        self.Phase_graph.setSizePolicy(sizePolicy)
        self.Phase_graph.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Phase_graph.setObjectName("Phase_graph")
        self.verticalLayout_6.addWidget(self.Phase_graph)
        self.verticalLayout_5.addWidget(self.phasebox)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addWidget(self.design_box, 0, 0, 1, 1)
        self.tabWidget.addTab(self.design_tab, "")
        self.correction_tab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.correction_tab.setPalette(palette)
        self.correction_tab.setStyleSheet("QGroupBox {\n"
                                          "background-color: #ffffff;\n"
                                          "\n"
                                          "}\n"
                                          "")
        self.correction_tab.setObjectName("correction_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.correction_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox2 = QtWidgets.QGroupBox(self.correction_tab)
        self.groupBox2.setStyleSheet("border: none;\n"
                                     "")
        self.groupBox2.setObjectName("groupBox2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.Zplane_box_2 = QtWidgets.QGroupBox(self.groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Zplane_box_2.sizePolicy().hasHeightForWidth())
        self.Zplane_box_2.setSizePolicy(sizePolicy)
        self.Zplane_box_2.setStyleSheet("QGroupBox {\n"
                                        "background-color: #ffffff;\n"
                                        "      border: none;\n"
                                        "      padding: 5px 10px;\n"
                                        "     border: 1.2px solid black;\n"
                                        "border-style: outset;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.Zplane_box_2.setObjectName("Zplane_box_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Zplane_box_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_14 = QtWidgets.QLabel(self.Zplane_box_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("\n"
                                    "color: black;\n"
                                    "      border: none;\n"
                                    "      padding: 5px 10px;\n"
                                    "     border: 1.2px solid black;\n"
                                    "border-style: outset;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.z_plane_2 = PlotWidget(self.Zplane_box_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.z_plane_2.sizePolicy().hasHeightForWidth())
        self.z_plane_2.setSizePolicy(sizePolicy)
        self.z_plane_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.z_plane_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.z_plane_2.setObjectName("z_plane_2")
        self.verticalLayout_11.addWidget(self.z_plane_2)
        self.horizontalLayout_21.addWidget(self.Zplane_box_2)
        self.mag_box = QtWidgets.QGroupBox(self.groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mag_box.sizePolicy().hasHeightForWidth())
        self.mag_box.setSizePolicy(sizePolicy)
        self.mag_box.setStyleSheet("QGroupBox {\n"
                                   "background-color: #ffffff;\n"
                                   "      border: none;\n"
                                   "      padding: 2px 10px;\n"
                                   "     border: 1.2px solid black;\n"
                                   "border-style: outset;\n"
                                   "}")
        self.mag_box.setObjectName("mag_box")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mag_box)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.mag_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("\n"
                                    "color: black;\n"
                                    "      border: none;\n"
                                    "      padding: 5px 10px;\n"
                                    "     border: 1.2px solid black;\n"
                                    "border-style: outset;\n"
                                    "")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.Phase_Response_Graph = PlotWidget(self.mag_box)
        self.Phase_Response_Graph.setStyleSheet(
            "background-color: rgb(0, 0, 0);")
        self.Phase_Response_Graph.setObjectName("Phase_Response_Graph")
        self.verticalLayout_10.addWidget(self.Phase_Response_Graph)
        self.horizontalLayout_21.addWidget(self.mag_box)
        self.phase_box = QtWidgets.QGroupBox(self.groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.phase_box.sizePolicy().hasHeightForWidth())
        self.phase_box.setSizePolicy(sizePolicy)
        self.phase_box.setStyleSheet("QGroupBox {\n"
                                     "background-color: #ffffff;\n"
                                     "      border: none;\n"
                                     "      padding: 5px 10px;\n"
                                     "     border: 1.2px solid black;\n"
                                     "border-style: outset;\n"
                                     "}")
        self.phase_box.setObjectName("phase_box")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.phase_box)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QtWidgets.QLabel(self.phase_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("\n"
                                    "color: black;\n"
                                    "      border: none;\n"
                                    "      padding: 5px 10px;\n"
                                    "     border: 1.2px solid black;\n"
                                    "border-style: outset;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.corrected_phase = PlotWidget(self.phase_box)
        self.corrected_phase.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.corrected_phase.setObjectName("corrected_phase")
        self.verticalLayout_12.addWidget(self.corrected_phase)
        self.horizontalLayout_21.addWidget(self.phase_box)
        self.gridLayout_6.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.filterBox = QtWidgets.QGroupBox(self.groupBox2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.filterBox.sizePolicy().hasHeightForWidth())
        self.filterBox.setSizePolicy(sizePolicy)
        self.filterBox.setStyleSheet("QGroupBox {\n"
                                     "background-color: #ffffff;\n"
                                     "      border: none;\n"
                                     "      padding: 5px 10px;\n"
                                     "     border: 1.2px solid black;\n"
                                     "border-style: outset;\n"
                                     "}")
        self.filterBox.setObjectName("filterBox")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.filterBox)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.filter_combobox = QtWidgets.QComboBox(self.filterBox)
        self.filter_combobox.setStyleSheet("\n"
                                           "color: black;\n"
                                           "      border: none;\n"
                                           "      padding: 5px 10px;\n"
                                           "     border: 1.2px solid black;\n"
                                           "border-style: outset;")
        self.filter_combobox.setObjectName("filter_combobox")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")
        self.filter_combobox.addItem("")

        self.horizontalLayout_18.addWidget(self.filter_combobox)
        self.add_filter_button = QtWidgets.QPushButton(
            self.filterBox, clicked=lambda: Director.add_filter())
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add_filter_button.setFont(font)
        self.add_filter_button.setStyleSheet("background-color: #ffffff;\n"
                                             "      color: black;\n"
                                             "      border: none;\n"
                                             "      padding: 5px 10px;\n"
                                             "     border: 1.2px ;\n"
                                             "border-style: outset;")
        self.add_filter_button.setObjectName("add_filter_button")
        self.horizontalLayout_18.addWidget(self.add_filter_button)
        self.delete_filter_button = QtWidgets.QPushButton(
            self.filterBox, clicked=lambda: Director.delete_filter())

        font = QtGui.QFont()
        font.setPointSize(9)
        self.delete_filter_button.setFont(font)
        self.delete_filter_button.setStyleSheet("background-color: #ffffff;\n"
                                                "      color: black;\n"
                                                "      border: none;\n"
                                                "      padding: 5px 10px;\n"
                                                "     border: 1.2px ;\n"
                                                "border-style: outset;")
        self.delete_filter_button.setObjectName("delete_filter_button")
        self.horizontalLayout_18.addWidget(self.delete_filter_button)
        self.customBox = QtWidgets.QGroupBox(self.filterBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.customBox.sizePolicy().hasHeightForWidth())
        self.customBox.setSizePolicy(sizePolicy)
        self.customBox.setStyleSheet("QGroupBox {\n"
                                     "background-color: #ffffff;\n"
                                     "      border: none;\n"
                                     "      padding: 5px 10px;\n"
                                     "     border: 1.2px solid black;\n"
                                     "border-style: outset;\n"
                                     "}")
        self.customBox.setObjectName("customBox")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.customBox)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.custom_filter_text = QtWidgets.QLineEdit(self.customBox)
        self.custom_filter_text.setStyleSheet("color: rgb(0, 0, 0);")
        self.custom_filter_text.setText("")
        self.custom_filter_text.setObjectName("custom_filter_text")
        self.horizontalLayout_20.addWidget(self.custom_filter_text)
        self.apply_custom_filter = QtWidgets.QPushButton(
            self.customBox, clicked=lambda: Director.insert_custom_allpass())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.apply_custom_filter.sizePolicy().hasHeightForWidth())
        self.apply_custom_filter.setSizePolicy(sizePolicy)
        self.apply_custom_filter.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.apply_custom_filter.setFont(font)
        self.apply_custom_filter.setStyleSheet("background-color: #ffffff;\n"
                                               "      color: black;\n"
                                               "      border: none;\n"
                                               "      padding: 5px 10px;\n"
                                               "     border: 1.2px ;\n"
                                               "border-style: outset;")
        self.apply_custom_filter.setObjectName("apply_custom_filter")
        self.horizontalLayout_20.addWidget(self.apply_custom_filter)
        self.horizontalLayout_18.addWidget(self.customBox)
        self.gridLayout_6.addWidget(self.filterBox, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.correction_tab, "")
        self.Results_tab = QtWidgets.QWidget()
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Results_tab.setPalette(palette)
        self.Results_tab.setStyleSheet("border:none;")
        self.Results_tab.setObjectName("Results_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Results_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.resultBox = QtWidgets.QGroupBox(self.Results_tab)
        self.resultBox.setStyleSheet("")
        self.resultBox.setObjectName("resultBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.resultBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.RealBox = QtWidgets.QGroupBox(self.resultBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RealBox.sizePolicy().hasHeightForWidth())
        self.RealBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.RealBox.setFont(font)
        self.RealBox.setStyleSheet("background-color: #ffffff;\n"
                                   "      border: none;\n"
                                   "      padding: 2px 10px;\n"
                                   "     border: 1.2px solid black;\n"
                                   "border-style: outset;")
        self.RealBox.setObjectName("RealBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.RealBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem5 = QtWidgets.QSpacerItem(
            88, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.real_signal = PlotWidget(self.RealBox)
        self.real_signal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.real_signal.setObjectName("real_signal")
        self.verticalLayout_7.addWidget(self.real_signal)
        self.gridLayout_4.addWidget(self.RealBox, 0, 0, 1, 1)
        self.FilteredBox = QtWidgets.QGroupBox(self.resultBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FilteredBox.sizePolicy().hasHeightForWidth())
        self.FilteredBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.FilteredBox.setFont(font)
        self.FilteredBox.setStyleSheet("background-color: #ffffff;\n"
                                       "      border: none;\n"
                                       "      padding: 2px 10px;\n"
                                       "     border: 1.2px solid black;\n"
                                       "border-style: outset;")
        self.FilteredBox.setObjectName("FilteredBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.FilteredBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.filtered_signal = PlotWidget(self.FilteredBox)
        self.filtered_signal.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.filtered_signal.setObjectName("filtered_signal")
        self.gridLayout_3.addWidget(self.filtered_signal, 1, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(
            88, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.FilteredBox, 1, 0, 1, 1)
        self.loadingBox = QtWidgets.QGroupBox(self.resultBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.loadingBox.setFont(font)
        self.loadingBox.setStyleSheet("background-color: #ffffff;\n"
                                      "      border: none;\n"
                                      "      padding: 5px 10px;\n"
                                      "     border: 1.2px solid black;\n"
                                      "border-style: outset;")
        self.loadingBox.setTitle("")
        self.loadingBox.setObjectName("loadingBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.loadingBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(0, -1, 32, -1)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.load_radioButton = QtWidgets.QRadioButton(self.loadingBox)
        self.load_radioButton.setMaximumSize(QtCore.QSize(179, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load_radioButton.setFont(font)
        self.load_radioButton.setStyleSheet("background-color: #ffffff;\n"
                                            "      color: black;\n"
                                            "      border: none;\n"
                                            "      padding: 5px 10px;\n"
                                            "     border: 1.2px ;\n"
                                            "border-style: outset;")
        self.load_radioButton.setObjectName("load_radioButton")
        self.horizontalLayout_15.addWidget(self.load_radioButton)
        self.touch_pad_radioButton = QtWidgets.QRadioButton(self.loadingBox)
        self.touch_pad_radioButton.setMaximumSize(QtCore.QSize(181, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.touch_pad_radioButton.setFont(font)
        self.touch_pad_radioButton.setStyleSheet("background-color: #ffffff;\n"
                                                 "      color: black;\n"
                                                 "      border: none;\n"
                                                 "      padding: 5px 10px;\n"
                                                 "     border: 1.2px ;\n"
                                                 "border-style: outset;")
        self.touch_pad_radioButton.setObjectName("touch_pad_radioButton")
        self.horizontalLayout_15.addWidget(self.touch_pad_radioButton)
        self.load_button = QtWidgets.QPushButton(
            self.loadingBox, clicked=lambda: Director.browse_load_signal())
        self.load_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.load_button.setStyleSheet("background-color: #ffffff;\n"
                                       "      color: black;\n"
                                       "      border: none;\n"
                                       "      padding: 5px 10px;\n"
                                       "     border: 1.2px ;\n"
                                       "border-style: outset;")
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_15.addWidget(self.load_button)
        self.gridLayout_8.addLayout(self.horizontalLayout_15, 0, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.loadingBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)
        self.speed_slider = QtWidgets.QSlider(self.loadingBox)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.speed_slider.setMinimum(100)
        self.speed_slider.setMaximum(500)
        self.gridLayout_8.addWidget(self.speed_slider, 1, 1, 1, 1)
        self.speed_LCD = QtWidgets.QLCDNumber(self.loadingBox)
        self.speed_LCD.setObjectName("speed_LCD")
        self.gridLayout_8.addWidget(self.speed_LCD, 1, 2, 1, 1)
        self.touch_pad = MousePad()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.touch_pad.sizePolicy().hasHeightForWidth())
        self.touch_pad.setSizePolicy(sizePolicy)
        self.touch_pad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.touch_pad.setStyleSheet("border: 1px solid black;\n"
                                     "border-radius: 15px;\n" "background-color:#527a7a;\n")
        self.touch_pad.setObjectName("touch_pad")
        self.gridLayout_8.addWidget(self.touch_pad, 2, 0, 1, 3)
        self.gridLayout_4.addWidget(self.loadingBox, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.resultBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Results_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        Application.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Application)
        self.statusbar.setObjectName("statusbar")
        Application.setStatusBar(self.statusbar)

        self.retranslateUi(Application)
        self.tabWidget.setCurrentIndex(2)
        self.Clear_combobox.setCurrentIndex(0)
        self.speed_slider.valueChanged['int'].connect(
            self.speed_LCD.display)  # type: ignore
        self.filter_combobox.currentIndexChanged.connect(
            lambda index: Director.display_allpass_filter(index))
        self.load_radioButton.setChecked(True)
        self.tabWidget.currentChanged.connect(
            lambda index: Director.display_tab(index))
        self.touch_pad_radioButton.toggled.connect(
            lambda: Director.touchpad_radiobutton_toggle())
        self.speed_slider.valueChanged.connect(
            lambda value: Director.update_temporal_speed(value))
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate(
            "Application", "Realtime Filter Designer"))
        self.label.setText(_translate("Application", "Digital Filters"))
        self.Zplane_box.setTitle(_translate("Application", "Z - Pole"))
        self.magBox.setTitle(_translate("Application", "Magnitude Response"))
        self.zeros_radioButton.setText(_translate("Application", "Zeros"))
        self.pole_radioButton.setText(_translate("Application", "Poles"))
        self.label_9.setText(_translate("Application", "Conjugates:"))
        self.add_conjugates.setText(_translate("Application", "Add"))
        self.Clear_combobox.setCurrentText(
            _translate("Application", "all zeros"))
        self.Clear_combobox.setItemText(
            0, _translate("Application", "all zeros"))
        self.Clear_combobox.setItemText(
            1, _translate("Application", "all poles"))
        self.Clear_combobox.setItemText(2, _translate("Application", "all"))
        self.Clear_combobox.setItemText(
            3, _translate("Application", "current"))
        self.confirm_button.setText(_translate("Application", "Clear"))
        self.phasebox.setTitle(_translate("Application", "Phase Response"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.design_tab), _translate("Application", "Filter"))
        self.label_14.setText(_translate("Application", "Z - Pole"))
        self.label_13.setText(_translate("Application", "Phase Response"))
        self.label_16.setText(_translate("Application", "Corrected Phase"))

        self.filter_combobox.setItemText(
            0, _translate("Application", "(0.5+0.5j)"))
        self.filter_combobox.setItemText(
            1, _translate("Application", "(-0.5+0.5j)"))
        self.filter_combobox.setItemText(
            2, _translate("Application", "(0.5-0.5j)"))
        self.filter_combobox.setItemText(
            3, _translate("Application", "(-0.5-0.5j)"))

        self.add_filter_button.setText(_translate("Application", "Apply"))
        self.delete_filter_button.setText(_translate("Application", "Remove"))
        self.custom_filter_text.setPlaceholderText(
            _translate("Application", "Add your Filter"))
        self.apply_custom_filter.setText(_translate("Application", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.correction_tab), _translate("Application", "All Pass Filter"))
        self.RealBox.setTitle(_translate("Application", "Real Signal"))
        self.FilteredBox.setTitle(_translate("Application", "Filtered Signal"))
        self.load_radioButton.setText(
            _translate("Application", "Load Signal  "))
        self.touch_pad_radioButton.setText(
            _translate("Application", "Touch Pad"))
        self.load_button.setText(_translate("Application", "Load"))
        self.label_12.setText(_translate("Application", "Speed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.Results_tab), _translate("Application", "Output"))


class PlotWidget1(PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.cursor_x_coordinates = 0
        self.cursor_y_coordinates = 0
        self.Director = None
        self.clear_box = None
        self.clicked_points = []
        self.addedPoint = None
        self.dragged_point = None
        self.mouse_dragging = False
        self.last_mouse_pos = None
        self.selected_point = None

    def mousePressEvent(self, event):
        if event.button() == pg.QtCore.Qt.LeftButton:
            mouse_point = self.plotItem.vb.mapSceneToView(event.pos())
            self.cursor_x_coordinates, self.cursor_y_coordinates = round(
                mouse_point.x(), 1), round(mouse_point.y(), 1)

        if not self.Director.is_available(self.cursor_x_coordinates, self.cursor_y_coordinates):
            # Check if the new point is within the area
            is_within_area = self.Director.currentPosition(
                self.cursor_x_coordinates, self.cursor_y_coordinates)
            if is_within_area:
                self.mouse_dragging = True
                self.selected_point = True
                self.last_mouse_pos = mouse_point

            if not is_within_area:
                Director.highlightedX = self.cursor_x_coordinates
                Director.highlightedY = self.cursor_y_coordinates
                self.Director.add_zeros_and_poles(
                    self.cursor_x_coordinates, self.cursor_y_coordinates)
                # Create and add the new clicked point
                self.addedPoint = ScatterPlotItem()
                self.addedPoint.addPoints(x=[self.cursor_x_coordinates], y=[
                                          self.cursor_y_coordinates], brush='r')
                self.addItem(self.addedPoint)

        else:  # check dragging
            self.mouse_dragging = True
            self.removeItem(self.addedPoint)
            if (self.Director.currentPosition(self.cursor_x_coordinates, self.cursor_y_coordinates)):
                self.addedPoint = ScatterPlotItem()
                self.addedPoint.addPoints(x=[self.cursor_x_coordinates], y=[
                                          self.cursor_y_coordinates], brush='r')
                self.addItem(self.addedPoint)
                Director.highlightedX = self.cursor_x_coordinates
                Director.highlightedY = self.cursor_y_coordinates
                self.mouse_dragging = True
                is_within_area = True
                self.selected_point = True
                self.last_mouse_pos = mouse_point

    def mouseMoveEvent(self, event):
        if self.mouse_dragging and self.selected_point:
            # Update the selected point's coordinates
            x_old = round(self.last_mouse_pos.x(), 1)
            y_old = round(self.last_mouse_pos.y(), 1)
            current_position = self.plotItem.vb.mapSceneToView(event.pos())
            self.clicked_points = round(
                current_position.x(), 1), round(current_position.y(), 1)
            self.Director.new_coordinates_pos(
                x_old, y_old, self.clicked_points)
            self.last_mouse_pos = current_position

    def mouseReleaseEvent(self, event):
        if event.button() == pg.QtCore.Qt.LeftButton:
            self.mouse_dragging = False
            self.selected_point = False


class MousePad(QGraphicsView):
    def __init__(self):
        super(MousePad, self).__init__()
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        Director.track_cursor(event)
        # Call the base class implementation
        super().mouseMoveEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QMainWindow()
    ui = Ui_Application()
    ui.setupUi(Application)
    Director = ApplicationDirector(ui)
    Director.highlighted_point = ui.z_plane.addedPoint
    ui.z_plane.Director = Director
    ui.z_plane.clear_box = ui.Clear_combobox
    Director.plot_unit_circle(0)
    ui.add_conjugates.clicked.connect(Director.add_conjugates)
    ui.confirm_button.clicked.connect(Director.clear_current)
    Application.show()
    sys.exit(app.exec_())
