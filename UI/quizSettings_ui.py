# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quizSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#CHANGE!!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox

from pathlib import Path, PureWindowsPath
from os.path import dirname, abspath


imagesPath = dirname(dirname(abspath(__file__))) + "/images/"
realImagesPath = []
for i in imagesPath:
    realImagesPath.append(i)

del(realImagesPath[0])
del(realImagesPath[0])

for i in range(len(realImagesPath)):
    if realImagesPath[i] == "\\":
        realImagesPath[i] = "/"

imagesPath = "".join(realImagesPath)


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1600, 900)
        Frame.setMaximumSize(QtCore.QSize(1600, 900))

        buttonWidth = 380
        self.startButton = QtWidgets.QPushButton(Frame)
        self.startButton.setGeometry(QtCore.QRect(1600 - buttonWidth, 800, buttonWidth - 100, 90))
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "start.png) 0 0 0 0 stretch stretch;")

        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(imagesPath + "Background.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        buttonWidth = 380
        self.backButton = QtWidgets.QPushButton(Frame)
        self.backButton.setGeometry(QtCore.QRect(100, 800, buttonWidth - 100, 90))
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "back.png) 0 0 0 0 stretch stretch;")

        widthOfTitle = 500
        self.configurationTitle = QtWidgets.QLabel(Frame)
        self.configurationTitle.setGeometry(QtCore.QRect(800 - widthOfTitle//2, 50, widthOfTitle + 30, 100))
        self.configurationTitle.setText("")
        self.configurationTitle.setPixmap(QtGui.QPixmap(imagesPath + "configuration.png"))
        self.configurationTitle.setScaledContents(True)
        self.configurationTitle.setObjectName("configurationTitle")

        headerX = 900
        headerY = 220
        headerWidth = 200
        headerHeight = 70
        
        #line edit for name
        self.lineEdit_82 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_82.setGeometry(QtCore.QRect(headerX + 400, headerY + 10, 200, 40))
        self.lineEdit_82.setAutoFillBackground(False)
        self.lineEdit_82.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.lineEdit_82.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_82.setObjectName("lineEdit_82")

        self.textBrowser_1 = QtWidgets.QTextBrowser(Frame)
        self.textBrowser_1.setGeometry(QtCore.QRect(200, 300, 560, 400))
        self.textBrowser_1.setAutoFillBackground(False)
        self.textBrowser_1.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.textBrowser_1.setText("hello")
        self.textBrowser_1.setAlignment(QtCore.Qt.AlignLeft)
        self.textBrowser_1.setObjectName("textBrowser_1")
        
        instructionX = 250
        
        self.additionHeader2x2 = QtWidgets.QLabel(Frame)
        self.additionHeader2x2.setGeometry(QtCore.QRect(instructionX, 300, 560, 50))
        self.additionHeader2x2.setText("")
        self.additionHeader2x2.setPixmap(QtGui.QPixmap(imagesPath + "instructions1.png"))
        self.additionHeader2x2.setScaledContents(True)
        self.additionHeader2x2.setObjectName("additionHeader2x2")

        self.additionHeader3x3 = QtWidgets.QLabel(Frame)
        self.additionHeader3x3.setGeometry(QtCore.QRect(instructionX, 300, 560, 50))
        self.additionHeader3x3.setText("")
        self.additionHeader3x3.setPixmap(QtGui.QPixmap(imagesPath + "instructions2.png"))
        self.additionHeader3x3.setScaledContents(True)
        self.additionHeader3x3.setObjectName("additionHeader3x3")

        self.additionHeader4x4 = QtWidgets.QLabel(Frame)
        self.additionHeader4x4.setGeometry(QtCore.QRect(instructionX, 300, 560, 50))
        self.additionHeader4x4.setText("")
        self.additionHeader4x4.setPixmap(QtGui.QPixmap(imagesPath + "instructions3.png"))
        self.additionHeader4x4.setScaledContents(True)
        self.additionHeader4x4.setObjectName("additionHeader4x4")

        self.easyHeader = QtWidgets.QLabel(Frame)
        self.easyHeader.setGeometry(QtCore.QRect(30, 370, 200, 70))
        self.easyHeader.setText("")
        self.easyHeader.setPixmap(QtGui.QPixmap(imagesPath + "easy.png"))
        self.easyHeader.setScaledContents(True)
        self.easyHeader.setObjectName("easyHeader")

        self.mediumHeader = QtWidgets.QLabel(Frame)
        self.mediumHeader.setGeometry(QtCore.QRect(30, 370, 200, 70))
        self.mediumHeader.setText("")
        self.mediumHeader.setPixmap(QtGui.QPixmap(imagesPath + "medium.png"))
        self.mediumHeader.setScaledContents(True)
        self.mediumHeader.setObjectName("mediumHeader")

        self.hardHeader = QtWidgets.QLabel(Frame)
        self.hardHeader.setGeometry(QtCore.QRect(30, 370, 200, 70))
        self.hardHeader.setText("")
        self.hardHeader.setPixmap(QtGui.QPixmap(imagesPath + "hard.png"))
        self.hardHeader.setScaledContents(True)
        self.hardHeader.setObjectName("hardHeader")

        self.multiplicationHeader2x2 = QtWidgets.QLabel(Frame)
        self.multiplicationHeader2x2.setGeometry(QtCore.QRect(instructionX, 350, 560, 50))
        self.multiplicationHeader2x2.setText("")
        self.multiplicationHeader2x2.setPixmap(QtGui.QPixmap(imagesPath + "instructions12.png"))
        self.multiplicationHeader2x2.setScaledContents(True)
        self.multiplicationHeader2x2.setObjectName("multiplicationHeader2x2")

        self.multiplicationHeader3x3 = QtWidgets.QLabel(Frame)
        self.multiplicationHeader3x3.setGeometry(QtCore.QRect(instructionX, 350, 560, 50))
        self.multiplicationHeader3x3.setText("")
        self.multiplicationHeader3x3.setPixmap(QtGui.QPixmap(imagesPath + "instructions21.png"))
        self.multiplicationHeader3x3.setScaledContents(True)
        self.multiplicationHeader3x3.setObjectName("multiplicationHeader3x3")

        self.multiplicationHeader4x4 = QtWidgets.QLabel(Frame)
        self.multiplicationHeader4x4.setGeometry(QtCore.QRect(instructionX, 350, 560, 50))
        self.multiplicationHeader4x4.setText("")
        self.multiplicationHeader4x4.setPixmap(QtGui.QPixmap(imagesPath + "instructions31.png"))
        self.multiplicationHeader4x4.setScaledContents(True)
        self.multiplicationHeader4x4.setObjectName("multiplicationHeader4x4")

        self.determinantHeader2x2 = QtWidgets.QLabel(Frame)
        self.determinantHeader2x2.setGeometry(QtCore.QRect(instructionX, 400, 560, 50))
        self.determinantHeader2x2.setText("")
        self.determinantHeader2x2.setPixmap(QtGui.QPixmap(imagesPath + "instructions13.png"))
        self.determinantHeader2x2.setScaledContents(True)
        self.determinantHeader2x2.setObjectName("determinantHeader2x2")

        self.determinantHeader3x3 = QtWidgets.QLabel(Frame)
        self.determinantHeader3x3.setGeometry(QtCore.QRect(instructionX, 400, 560, 50))
        self.determinantHeader3x3.setText("")
        self.determinantHeader3x3.setPixmap(QtGui.QPixmap(imagesPath + "instructions22.png"))
        self.determinantHeader3x3.setScaledContents(True)
        self.determinantHeader3x3.setObjectName("determinantHeader3x3")

        self.eigenvectorsHeader = QtWidgets.QLabel(Frame)
        self.eigenvectorsHeader.setGeometry(QtCore.QRect(instructionX, 400, 560, 50))
        self.eigenvectorsHeader.setText("")
        self.eigenvectorsHeader.setPixmap(QtGui.QPixmap(imagesPath + "instructions34.png"))
        self.eigenvectorsHeader.setScaledContents(True)
        self.eigenvectorsHeader.setObjectName("eigenvectorsHeader")

        self.inverseHeader2x2 = QtWidgets.QLabel(Frame)
        self.inverseHeader2x2.setGeometry(QtCore.QRect(instructionX, 450, 560, 50))
        self.inverseHeader2x2.setText("")
        self.inverseHeader2x2.setPixmap(QtGui.QPixmap(imagesPath + "instructions14.png"))
        self.inverseHeader2x2.setScaledContents(True)
        self.inverseHeader2x2.setObjectName("inverseHeader2x2")

        self.inverseHeader3x3 = QtWidgets.QLabel(Frame)
        self.inverseHeader3x3.setGeometry(QtCore.QRect(instructionX, 450, 560, 50))
        self.inverseHeader3x3.setText("")
        self.inverseHeader3x3.setPixmap(QtGui.QPixmap(imagesPath + "instructions23.png"))
        self.inverseHeader3x3.setScaledContents(True)
        self.inverseHeader3x3.setObjectName("inverseHeader3x3")

        self.eigenvaluesHeader = QtWidgets.QLabel(Frame)
        self.eigenvaluesHeader.setGeometry(QtCore.QRect(instructionX, 450, 560, 50))
        self.eigenvaluesHeader.setText("")
        self.eigenvaluesHeader.setPixmap(QtGui.QPixmap(imagesPath + "instructions35.png"))
        self.eigenvaluesHeader.setScaledContents(True)
        self.eigenvaluesHeader.setObjectName("eigenvaluesHeader")

        self.nameHeader = QtWidgets.QLabel(Frame)
        self.nameHeader.setGeometry(QtCore.QRect(headerX, headerY, headerWidth, headerHeight))
        self.nameHeader.setText("")
        self.nameHeader.setPixmap(QtGui.QPixmap(imagesPath + "name.png"))
        self.nameHeader.setScaledContents(True)
        self.nameHeader.setObjectName("nameHeader")

        self.difficultyHeader = QtWidgets.QLabel(Frame)
        self.difficultyHeader.setGeometry(QtCore.QRect(headerX, headerY + 100, headerWidth, headerHeight))
        self.difficultyHeader.setText("")
        self.difficultyHeader.setPixmap(QtGui.QPixmap(imagesPath + "difficulty.png"))
        self.difficultyHeader.setScaledContents(True)
        self.difficultyHeader.setObjectName("difficultyHeader")

        self.numberOfQuestionsHeader = QtWidgets.QLabel(Frame)
        self.numberOfQuestionsHeader.setGeometry(QtCore.QRect(headerX, headerY + 200, headerWidth + 150, headerHeight))
        self.numberOfQuestionsHeader.setText("")
        self.numberOfQuestionsHeader.setPixmap(QtGui.QPixmap(imagesPath + "numberOfQuestions.png"))
        self.numberOfQuestionsHeader.setScaledContents(True)
        self.numberOfQuestionsHeader.setObjectName("numberOfQuestionsHeader")

        #combo box for difficulty
        self.difficultyComboBox = QtWidgets.QComboBox(Frame)
        self.difficultyComboBox.addItem("Easy")
        self.difficultyComboBox.addItem("Medium")
        self.difficultyComboBox.addItem("Hard")
        self.difficultyComboBox.setGeometry(QtCore.QRect(headerX + 400, headerY + 100 + 10, 200, 40))
        self.difficultyComboBox.setAutoFillBackground(False)
        self.difficultyComboBox.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.difficultyComboBox.setObjectName("difficultyComboBox")

        self.difficultyComboBox.currentIndexChanged.connect(self.getChoice)

        #combo box for no. of questions
        self.questionsComboBox = QtWidgets.QComboBox(Frame)
        self.questionsComboBox.addItem("5")
        self.questionsComboBox.addItem("10")
        self.questionsComboBox.addItem("20")
        self.questionsComboBox.setGeometry(QtCore.QRect(headerX + 400, headerY + 200 + 10, 200, 40))
        self.questionsComboBox.setAutoFillBackground(False)
        self.questionsComboBox.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.difficultyComboBox.setObjectName("questionsComboBox")

        questionChoice = self.questionsComboBox.currentText()
        self.questionsComboBox.currentIndexChanged.connect(self.getQuestions)

        self.label_5.raise_()
        self.startButton.raise_()
        self.backButton.raise_()
        self.configurationTitle.raise_()
        self.lineEdit_82.raise_()
        self.additionHeader2x2.raise_()
        self.easyHeader.raise_()
        self.multiplicationHeader2x2.raise_()
        self.determinantHeader2x2.raise_()
        self.inverseHeader2x2.raise_()
        self.nameHeader.raise_()
        self.difficultyHeader.raise_()
        self.numberOfQuestionsHeader.raise_()
        self.difficultyComboBox.raise_()
        self.questionsComboBox.raise_()

        '''Frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formLayout = QtWidgets.QFormLayout(Frame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.plainTextEdit = QtWidgets.QLineEdit(Frame)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(120, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.numberOfQs = QtWidgets.QComboBox(Frame)
        self.numberOfQs.setMaximumSize(QtCore.QSize(100, 16777215))
        self.numberOfQs.setObjectName("numberOfQs")
        self.numberOfQs.addItem("")
        self.numberOfQs.addItem("")
        self.numberOfQs.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.numberOfQs)
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.difficulty = QtWidgets.QComboBox(Frame)
        self.difficulty.setMaximumSize(QtCore.QSize(100, 16777215))
        self.difficulty.setObjectName("difficulty")
        self.difficulty.addItem("")
        self.difficulty.addItem("")
        self.difficulty.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.difficulty)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.submit = QtWidgets.QPushButton(Frame)
        self.submit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.submit.setObjectName("submit")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.submit)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)'''
        
    
    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        #self.label_2.setText(_translate("Frame", "Enter Username:"))
        self.label_3.setText(_translate("Frame", "Select No.of Questions:"))
        self.numberOfQs.setItemText(0, _translate("Frame", "5"))
        self.numberOfQs.setItemText(1, _translate("Frame", "10"))
        self.numberOfQs.setItemText(2, _translate("Frame", "20"))
        self.label_4.setText(_translate("Frame", "Select difficulty:"))
        self.difficulty.setItemText(0, _translate("Frame", "Easy"))
        self.difficulty.setItemText(1, _translate("Frame", "Medium"))
        self.difficulty.setItemText(2, _translate("Frame", "Hard"))
        self.label.setText(_translate("Frame", "Quiz Settings"))
        self.submit.setText(_translate("Frame", "Submit"))

    def getQuestions(self):
        questionChoice = self.questionsComboBox.currentText()
        return questionChoice
    
    def getChoice(self):
        difficultyChoice = self.difficultyComboBox.currentText()
        if difficultyChoice == 'Easy':
                self.mediumHeader.setHidden(True)
                self.additionHeader3x3.setHidden(True)
                self.multiplicationHeader3x3.setHidden(True)
                self.determinantHeader3x3.setHidden(True)
                self.inverseHeader3x3.setHidden(True)

                self.hardHeader.setHidden(True)
                self.additionHeader4x4.setHidden(True)
                self.multiplicationHeader4x4.setHidden(True)
                self.eigenvaluesHeader.setHidden(True)
                self.eigenvectorsHeader.setHidden(True)

                self.inverseHeader2x2.setHidden(False)
                self.additionHeader2x2.setHidden(False)
                self.easyHeader.setHidden(False)
                self.multiplicationHeader2x2.setHidden(False)
                self.determinantHeader2x2.setHidden(False)

                self.additionHeader2x2.raise_()
                self.easyHeader.raise_()
                self.multiplicationHeader2x2.raise_()
                self.determinantHeader2x2.raise_()
                self.inverseHeader2x2.raise_()

        elif difficultyChoice == 'Medium':
                self.additionHeader2x2.setHidden(True)
                self.easyHeader.setHidden(True)
                self.multiplicationHeader2x2.setHidden(True)
                self.determinantHeader2x2.setHidden(True)
                self.inverseHeader2x2.setHidden(True)

                self.hardHeader.setHidden(True)
                self.additionHeader4x4.setHidden(True)
                self.multiplicationHeader4x4.setHidden(True)
                self.eigenvaluesHeader.setHidden(True)
                self.eigenvectorsHeader.setHidden(True)

                self.mediumHeader.setHidden(False)
                self.additionHeader3x3.setHidden(False)
                self.multiplicationHeader3x3.setHidden(False)
                self.determinantHeader3x3.setHidden(False)
                self.inverseHeader3x3.setHidden(False)

                self.mediumHeader.raise_()
                self.additionHeader3x3.raise_()
                self.multiplicationHeader3x3.raise_()
                self.determinantHeader3x3.raise_()
                self.inverseHeader3x3.raise_()
        
        elif difficultyChoice == 'Hard':
                self.additionHeader2x2.setHidden(True)
                self.easyHeader.setHidden(True)
                self.multiplicationHeader2x2.setHidden(True)
                self.determinantHeader2x2.setHidden(True)
                self.inverseHeader2x2.setHidden(True)

                self.mediumHeader.setHidden(True)
                self.additionHeader3x3.setHidden(True)
                self.multiplicationHeader3x3.setHidden(True)
                self.determinantHeader3x3.setHidden(True)
                self.inverseHeader3x3.setHidden(True)

                self.hardHeader.setHidden(False)
                self.additionHeader4x4.setHidden(False)
                self.multiplicationHeader4x4.setHidden(False)
                self.eigenvaluesHeader.setHidden(False)
                self.eigenvectorsHeader.setHidden(False)

                self.hardHeader.raise_()
                self.additionHeader4x4.raise_()
                self.multiplicationHeader4x4.raise_()
                self.eigenvaluesHeader.raise_()
                self.eigenvectorsHeader.raise_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
