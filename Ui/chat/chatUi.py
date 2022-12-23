# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.sign_up = QtWidgets.QPushButton(Dialog)
        self.sign_up.setGeometry(QtCore.QRect(0, 0, 71, 28))
        self.sign_up.setObjectName("sign_up")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 160, 111, 562))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_chat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_chat.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_chat.setObjectName("btn_chat")
        self.verticalLayout_2.addWidget(self.btn_chat)
        self.btn_contact = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_contact.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_contact.setObjectName("btn_contact")
        self.verticalLayout_2.addWidget(self.btn_contact)
        self.btn_addC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addC.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_addC.setObjectName("btn_addC")
        self.verticalLayout_2.addWidget(self.btn_addC)
        self.btn_add_group = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add_group.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_add_group.setObjectName("btn_add_group")
        self.verticalLayout_2.addWidget(self.btn_add_group)
        self.btn_update_myinfo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_update_myinfo.setMinimumSize(QtCore.QSize(100, 80))
        self.btn_update_myinfo.setObjectName("btn_update_myinfo")
        self.verticalLayout_2.addWidget(self.btn_update_myinfo)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.myavatar = QtWidgets.QLabel(Dialog)
        self.myavatar.setGeometry(QtCore.QRect(10, 30, 100, 100))
        self.myavatar.setObjectName("myavatar")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(160, 0, 1120, 720))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1120, 720))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 326, 680))
        self.scrollArea.setMaximumSize(QtCore.QSize(400, 150000))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 12000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 300, 80))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(321, 0, 801, 720))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.message = QtWidgets.QTextBrowser(self.frame)
        self.message.setGeometry(QtCore.QRect(9, 39, 801, 541))
        self.message.setObjectName("message")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(9, 579, 821, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setTabStopWidth(80)
        self.textEdit.setCursorWidth(1)
        self.textEdit.setObjectName("textEdit")
        self.btn_sendMsg = QtWidgets.QPushButton(self.frame)
        self.btn_sendMsg.setGeometry(QtCore.QRect(680, 670, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_sendMsg.setFont(font)
        self.btn_sendMsg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_sendMsg.setMouseTracking(False)
        self.btn_sendMsg.setAutoFillBackground(False)
        self.btn_sendMsg.setStyleSheet("QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    \n"
"    padding: 10px;\n"
"    color:rgb(5,180,104);\n"
"}")
        self.btn_sendMsg.setIconSize(QtCore.QSize(40, 40))
        self.btn_sendMsg.setCheckable(False)
        self.btn_sendMsg.setAutoDefault(True)
        self.btn_sendMsg.setObjectName("btn_sendMsg")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(760, 0, 47, 41))
        self.toolButton.setObjectName("toolButton")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(2, 0, 3, 720))
        self.line_3.setLineWidth(6)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(9, 30, 831, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_remark = QtWidgets.QLabel(self.frame)
        self.label_remark.setGeometry(QtCore.QRect(30, 0, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_remark.setFont(font)
        self.label_remark.setText("")
        self.label_remark.setObjectName("label_remark")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 580, 800, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_destroy = QtWidgets.QPushButton(Dialog)
        self.btn_destroy.setGeometry(QtCore.QRect(80, 0, 71, 28))
        self.btn_destroy.setObjectName("btn_destroy")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sign_up.setText(_translate("Dialog", "退出登录"))
        self.btn_chat.setText(_translate("Dialog", "聊天"))
        self.btn_contact.setText(_translate("Dialog", "联系人"))
        self.btn_addC.setText(_translate("Dialog", "添加联系人"))
        self.btn_add_group.setText(_translate("Dialog", "群聊"))
        self.btn_update_myinfo.setText(_translate("Dialog", "修改资料"))
        self.myavatar.setText(_translate("Dialog", "avatar"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_sendMsg.setText(_translate("Dialog", "发送"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.btn_destroy.setText(_translate("Dialog", "注销账户"))
