# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatgpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_chatgptform(object):
    def setupUi(self, chatgptform):
        chatgptform.setObjectName("chatgptform")
        chatgptform.setWindowModality(QtCore.Qt.NonModal)
        chatgptform.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chatgptform.sizePolicy().hasHeightForWidth())
        chatgptform.setSizePolicy(sizePolicy)
        chatgptform.setMaximumSize(QtCore.QSize(600, 400))
        self.label_3 = QtWidgets.QLabel(chatgptform)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_3.setObjectName("label_3")
        self.chatgpt_model = QtWidgets.QComboBox(chatgptform)
        self.chatgpt_model.setGeometry(QtCore.QRect(130, 110, 451, 35))
        self.chatgpt_model.setMinimumSize(QtCore.QSize(0, 35))
        self.chatgpt_model.setObjectName("chatgpt_model")
        self.chatgpt_template = QtWidgets.QPlainTextEdit(chatgptform)
        self.chatgpt_template.setGeometry(QtCore.QRect(10, 180, 571, 151))
        self.chatgpt_template.setObjectName("chatgpt_template")
        self.label_4 = QtWidgets.QLabel(chatgptform)
        self.label_4.setGeometry(QtCore.QRect(10, 155, 271, 21))
        # font = QtGui.QFont()
        # font.setFamily("黑体")
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.set_chatgpt = QtWidgets.QPushButton(chatgptform)
        self.set_chatgpt.setGeometry(QtCore.QRect(10, 350, 93, 35))
        self.set_chatgpt.setMinimumSize(QtCore.QSize(0, 35))
        self.set_chatgpt.setObjectName("set_chatgpt")
        self.chatgpt_api = QtWidgets.QLineEdit(chatgptform)
        self.chatgpt_api.setGeometry(QtCore.QRect(150, 10, 431, 35))
        self.chatgpt_api.setMinimumSize(QtCore.QSize(0, 35))
        self.chatgpt_api.setObjectName("chatgpt_api")
        self.label = QtWidgets.QLabel(chatgptform)
        self.label.setGeometry(QtCore.QRect(10, 10, 130, 35))
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.chatgpt_key = QtWidgets.QLineEdit(chatgptform)
        self.chatgpt_key.setGeometry(QtCore.QRect(150, 60, 431, 35))
        self.chatgpt_key.setMinimumSize(QtCore.QSize(0, 35))
        self.chatgpt_key.setObjectName("chatgpt_key")
        self.label_2 = QtWidgets.QLabel(chatgptform)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 130, 35))
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(chatgptform)
        QtCore.QMetaObject.connectSlotsByName(chatgptform)

    def retranslateUi(self, chatgptform):
        _translate = QtCore.QCoreApplication.translate
        chatgptform.setWindowTitle(_translate("chatgptform", "ChatGPT"))
        self.label_3.setText(_translate("chatgptform", "ChatGPT Model"))
        self.chatgpt_template.setPlaceholderText(_translate("chatgptform", "prompt"))
        self.label_4.setText(_translate("chatgptform", "{lang} don\'t remove"))
        self.set_chatgpt.setText(_translate("chatgptform", "OK"))
        self.chatgpt_api.setPlaceholderText(_translate("chatgptform", "api url default  https://chat.openai.com"))
        self.chatgpt_key.setPlaceholderText(_translate("chatgptform", "secret key"))
        self.label.setText(_translate("chatgptform", "ChatGPT API URL"))
        self.label_2.setText(_translate("chatgptform", "ChatGPT  Key "))
