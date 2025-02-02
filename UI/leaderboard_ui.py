# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'leaderboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from pathlib import Path, PureWindowsPath
from PyQt5 import QtCore, QtGui, QtWidgets

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


class Ui_leaderboard(object):
    def setupUi(self, leaderboard):
        leaderboard.setObjectName("leaderboard")
        leaderboard.resize(1600, 900)
        leaderboard.setMaximumSize(QtCore.QSize(1600, 900))
        leaderboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        leaderboard.setFrameShadow(QtWidgets.QFrame.Raised)
        '''
        self.verticalLayout = QtWidgets.QVBoxLayout(leaderboard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leaderboard_2 = QtWidgets.QLabel(leaderboard)
        self.leaderboard_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.leaderboard_2.setObjectName("leaderboard_2")
        self.verticalLayout.addWidget(self.leaderboard_2)
        self.label = QtWidgets.QLabel(leaderboard)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(leaderboard)
        self.pushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        '''
        self.retryButton = QtWidgets.QPushButton(leaderboard)
        buttonWidth = 380
        self.retryButton.setGeometry(QtCore.QRect(1600 - buttonWidth, 800, buttonWidth - 100, 90))
        self.retryButton.setText("")
        self.retryButton.setObjectName("retryButton")
        self.retryButton.setAutoFillBackground(False)
        self.retryButton.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "retry.png) 0 0 0 0 stretch stretch;")

        self.label_5 = QtWidgets.QLabel(leaderboard)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(str(imagesPath) + "Background.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        
        self.reviseButton = QtWidgets.QPushButton(leaderboard)
        buttonWidth = 380
        self.reviseButton.setGeometry(QtCore.QRect(100, 800, buttonWidth - 100, 90))
        self.reviseButton.setText("")
        self.reviseButton.setObjectName("reviseButton")
        self.reviseButton.setAutoFillBackground(False)
        self.reviseButton.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "revise.png) 0 0 0 0 stretch stretch;")

        
        self.leaderboardTitle = QtWidgets.QLabel(leaderboard)
        widthOfTitle = 500
        self.leaderboardTitle.setGeometry(QtCore.QRect(800 - widthOfTitle//2, 50, widthOfTitle, 100))
        self.leaderboardTitle.setText("")
        self.leaderboardTitle.setPixmap(QtGui.QPixmap(str(imagesPath) + "leaderboard.png"))
        self.leaderboardTitle.setScaledContents(True)
        self.leaderboardTitle.setObjectName("leaderboardTitle")

        self.userHeader = QtWidgets.QLabel(leaderboard)
        self.userHeader.setGeometry(QtCore.QRect(150, 200, 200, 50))
        self.userHeader.setText("")
        self.userHeader.setPixmap(QtGui.QPixmap(str(imagesPath) + "user.png"))
        self.userHeader.setScaledContents(True)
        self.userHeader.setObjectName("userHeader")
        
        self.label_17 = QtWidgets.QLabel(leaderboard)
        self.label_17.setGeometry(QtCore.QRect(251, 131, 109, 31))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(str(imagesPath) + "hard.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")

        boxWidth = 200
        boxHeight = 40
        userX = 150
        boxY = 300
        percentageX = 700
        dateX = 1220

        #1st in user col
        self.user1Label = QtWidgets.QLabel(leaderboard)
        self.user1Label.setGeometry(QtCore.QRect(userX, boxY, boxWidth, boxHeight))
        self.user1Label.setAutoFillBackground(False)
        self.user1Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.user1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.user1Label.setObjectName("user1Label")

        #1st in percentage col        
        self.percentage1Label = QtWidgets.QLabel(leaderboard)
        self.percentage1Label.setGeometry(QtCore.QRect(percentageX, boxY, boxWidth, boxHeight))
        self.percentage1Label.setAutoFillBackground(False)
        self.percentage1Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.percentage1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage1Label.setObjectName("percentage1Label")

        #1st in date col
        self.date1Label = QtWidgets.QLabel(leaderboard)
        self.date1Label.setGeometry(QtCore.QRect(1220, boxY, boxWidth, boxHeight))
        self.date1Label.setAutoFillBackground(False)
        self.date1Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.date1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.date1Label.setObjectName("date1Label")

        #2nd in user col
        self.user2Label = QtWidgets.QLabel(leaderboard)
        self.user2Label.setGeometry(QtCore.QRect(userX, boxY + 100, boxWidth, boxHeight))
        self.user2Label.setAutoFillBackground(False)
        self.user2Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.user2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.user2Label.setObjectName("user2Label")

        #2nd in percentage col
        self.percentage2Label = QtWidgets.QLabel(leaderboard)
        self.percentage2Label.setGeometry(QtCore.QRect(percentageX, boxY + 100, boxWidth, boxHeight))
        self.percentage2Label.setAutoFillBackground(False)
        self.percentage2Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.percentage2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage2Label.setObjectName("percentage2Label")

        self.percentageHeader = QtWidgets.QLabel(leaderboard)
        self.percentageHeader.setGeometry(QtCore.QRect(650, 200, 300, 50))
        self.percentageHeader.setText("")
        self.percentageHeader.setPixmap(QtGui.QPixmap(str(imagesPath) + "percentage.png"))
        self.percentageHeader.setScaledContents(True)
        self.percentageHeader.setObjectName("percentageHeader")


        #2nd in date col
        self.date2Label = QtWidgets.QLabel(leaderboard)
        self.date2Label.setGeometry(QtCore.QRect(dateX, boxY + 100, boxWidth, boxHeight))
        self.date2Label.setAutoFillBackground(False)
        self.date2Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.date2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.date2Label.setObjectName("date2Label")

        #3rd in user col
        self.user3Label = QtWidgets.QLabel(leaderboard)
        self.user3Label.setGeometry(QtCore.QRect(userX, boxY + 200, boxWidth, boxHeight))
        self.user3Label.setAutoFillBackground(False)
        self.user3Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.user3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.user3Label.setObjectName("user3Label")

        #3rd in percentage col
        self.percentage3Label = QtWidgets.QLabel(leaderboard)
        self.percentage3Label.setGeometry(QtCore.QRect(percentageX, boxY + 200, boxWidth, boxHeight))
        self.percentage3Label.setAutoFillBackground(False)
        self.percentage3Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.percentage3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage3Label.setObjectName("percentage3Label")

        #3rd in date col
        self.date3Label = QtWidgets.QLabel(leaderboard)
        self.date3Label.setGeometry(QtCore.QRect(dateX, boxY + 200, boxWidth, boxHeight))
        self.date3Label.setAutoFillBackground(False)
        self.date3Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.date3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.date3Label.setObjectName("date3Label")

        #4th in user col
        self.user4Label = QtWidgets.QLabel(leaderboard)
        self.user4Label.setGeometry(QtCore.QRect(userX, boxY + 300, boxWidth, boxHeight))
        self.user4Label.setAutoFillBackground(False)
        self.user4Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.user4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.user4Label.setObjectName("user4Label")

        #4th in percentage col
        self.percentage4Label = QtWidgets.QLabel(leaderboard)
        self.percentage4Label.setGeometry(QtCore.QRect(percentageX, boxY + 300, boxWidth, boxHeight))
        self.percentage4Label.setAutoFillBackground(False)
        self.percentage4Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.percentage4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage4Label.setObjectName("percentage4Label")

        #4th in date col
        self.date4Label = QtWidgets.QLabel(leaderboard)
        self.date4Label.setGeometry(QtCore.QRect(dateX, boxY + 300, boxWidth, boxHeight))
        self.date4Label.setAutoFillBackground(False)
        self.date4Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.date4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.date4Label.setObjectName("date4Label")

        #5th in user col
        self.user5Label = QtWidgets.QLabel(leaderboard)
        self.user5Label.setGeometry(QtCore.QRect(userX, boxY + 400, boxWidth, boxHeight))
        self.user5Label.setAutoFillBackground(False)
        self.user5Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.user5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.user5Label.setObjectName("user5Label")

        #5th in percentage col
        self.percentage5Label = QtWidgets.QLabel(leaderboard)
        self.percentage5Label.setGeometry(QtCore.QRect(percentageX, boxY + 400, boxWidth, boxHeight))
        self.percentage5Label.setAutoFillBackground(False)
        self.percentage5Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.percentage5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage5Label.setObjectName("percentage5Label")

        #5th in date col
        self.date5Label = QtWidgets.QLabel(leaderboard)
        self.date5Label.setGeometry(QtCore.QRect(dateX, boxY + 400, boxWidth, boxHeight))
        self.date5Label.setAutoFillBackground(False)
        self.date5Label.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
        self.date5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.date5Label.setObjectName("date5Label")

        self.dateHeader = QtWidgets.QLabel(leaderboard)
        self.dateHeader.setGeometry(QtCore.QRect(1200, 200, 250, 50))
        self.dateHeader.setText("")
        self.dateHeader.setPixmap(QtGui.QPixmap(str(imagesPath) + "date.png"))
        self.dateHeader.setScaledContents(True)
        self.dateHeader.setObjectName("dateHeader")

        self.label_17.raise_()
        self.label_5.raise_()
        self.retryButton.raise_()
        self.reviseButton.raise_()
        self.leaderboardTitle.raise_()
        self.userHeader.raise_()
        self.user1Label.raise_()
        self.percentage1Label.raise_()
        self.date1Label.raise_()
        self.user2Label.raise_()
        self.percentage2Label.raise_()
        self.date2Label.raise_()
        self.percentage3Label.raise_()
        self.user3Label.raise_()
        self.date3Label.raise_()
        self.user4Label.raise_()
        self.percentage4Label.raise_()
        self.date4Label.raise_()
        self.user5Label.raise_()
        self.percentage5Label.raise_()
        self.date5Label.raise_()
        self.percentageHeader.raise_()
        self.dateHeader.raise_()

        self.retranslateUi(leaderboard)
        QtCore.QMetaObject.connectSlotsByName(leaderboard)

    def retranslateUi(self, leaderboard):
        _translate = QtCore.QCoreApplication.translate
        leaderboard.setWindowTitle(_translate("leaderboard", "Frame"))
        #self.leaderboard_2.setText(_translate("leaderboard", "Leaderboard:"))
        #self.label.setText(_translate("leaderboard", "Add output Data here"))
        #self.pushButton.setText(_translate("leaderboard", "Back to Homepage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    leaderboard = QtWidgets.QFrame()
    ui = Ui_leaderboard()
    ui.setupUi(leaderboard)
    leaderboard.show()
    sys.exit(app.exec_())
