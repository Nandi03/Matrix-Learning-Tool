# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questionPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#CHANGE!!

from PyQt5 import QtCore, QtGui, QtWidgets

from pathlib import Path, PureWindowsPath
from os.path import dirname, abspath

from numpy import equal, matrix

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

class Ui_Question(object):
    
    def setupUi(self, Question, questionNumber, totalQuestions, topic, matrix1, matrix2, matrix3):
        Question.setObjectName("Question")
        Question.resize(1600, 900)
        Question.setMaximumSize(QtCore.QSize(1600, 900))

        self.background = QtWidgets.QLabel(Question)
        self.background.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(imagesPath + "Background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        buttonWidth = 380
        self.resultsButton = QtWidgets.QPushButton(Question)
        self.resultsButton.setGeometry(QtCore.QRect(100, 800, buttonWidth - 100, 90))
        self.resultsButton.setText("")
        self.resultsButton.setObjectName("resultsButton")
        self.resultsButton.setAutoFillBackground(False)
        self.resultsButton.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + str(imagesPath) + "results.png) 0 0 0 0 stretch stretch;")
        self.resultsButton.raise_()

        widthOfTitle = 500
        self.questionTitle = QtWidgets.QLabel(Question)
        self.questionTitle.setGeometry(QtCore.QRect(800 - widthOfTitle//2, 50, widthOfTitle + 30, 100))
        self.questionTitle.setText("")
        self.questionTitle.setPixmap(QtGui.QPixmap(imagesPath + "question.png"))
        self.questionTitle.setScaledContents(True)
        self.questionTitle.setObjectName("questionTitle")        

        self.currentQuestionDigit = QtWidgets.QLabel(Question)
        self.currentQuestionDigit.setGeometry(QtCore.QRect(1100, 50, 70, 100)) 
        self.currentQuestionDigit.setText("")
        self.currentQuestionDigit.setPixmap(QtGui.QPixmap(imagesPath + str(questionNumber//10)  + ".png"))
        self.currentQuestionDigit.setScaledContents(True)
        self.currentQuestionDigit.setObjectName("currentQuestionDigit")

        self.currentQuestionDigit1 = QtWidgets.QLabel(Question)
        self.currentQuestionDigit1.setGeometry(QtCore.QRect(1160, 50, 70, 100)) 
        self.currentQuestionDigit1.setText("")
        self.currentQuestionDigit1.setPixmap(QtGui.QPixmap(imagesPath + str(questionNumber%10)  + ".png"))
        self.currentQuestionDigit1.setScaledContents(True)
        self.currentQuestionDigit1.setObjectName("currentQuestionDigit1")

        self.totalQuestionsDigit = QtWidgets.QLabel(Question)
        self.totalQuestionsDigit.setGeometry(QtCore.QRect(1270, 50, 70, 100))
        self.totalQuestionsDigit.setText("")
        self.totalQuestionsDigit.setPixmap(QtGui.QPixmap(imagesPath + str(totalQuestions//10) + ".png"))
        self.totalQuestionsDigit.setScaledContents(True)
        self.totalQuestionsDigit.setObjectName("totalQuestionsDigit")

        self.totalQuestionsDigit1 = QtWidgets.QLabel(Question)
        self.totalQuestionsDigit1.setGeometry(QtCore.QRect(1320, 50, 70, 100))
        self.totalQuestionsDigit1.setText("")
        self.totalQuestionsDigit1.setPixmap(QtGui.QPixmap(imagesPath + str(totalQuestions%10) + ".png"))
        self.totalQuestionsDigit1.setScaledContents(True)
        self.totalQuestionsDigit1.setObjectName("totalQuestionsDigit1")

        self.slashTitle = QtWidgets.QLabel(Question)
        self.slashTitle.setGeometry(QtCore.QRect(1225, 50, 50, 100))
        self.slashTitle.setText("")
        self.slashTitle.setPixmap(QtGui.QPixmap(imagesPath + "slash.png"))
        self.slashTitle.setScaledContents(True)
        self.slashTitle.setObjectName("slashTitle")
        
        def createMatrix(matrixCenterX, matrixCenterY, matrixSize, matrix, lineEdit=False, reverse=False):
                realBoxWidth = 50
                realGapWidth = 20
                matrixCells = len(matrix[0])
                scaleCoefficient = (matrixSize/matrixCells)/(realBoxWidth + realGapWidth)
                boxWidth, gapWidth = realBoxWidth*scaleCoefficient, realGapWidth*scaleCoefficient
                
                returnMatrix = {}
                offset = (matrixCells/2)*boxWidth + (matrixCells - 1)*gapWidth/2
                topLeftPositionX, topLeftPositionY = matrixCenterX - offset, matrixCenterY - offset

                extraString = ""
                if lineEdit == True:
                        extraString = "input"
                if reverse == False:
                        for i in range(matrixCells):
                                for j in range(matrixCells):
                                        if lineEdit == True:
                                                returnMatrix[str(i) + str(j)] = QtWidgets.QLineEdit(Question)
                                        else:
                                                returnMatrix[str(i) + str(j)] = QtWidgets.QLabel(Question)
                                                returnMatrix[str(i) + str(j)].setText(str(matrix[i][j]))
                                        returnMatrix[str(i) + str(j)].setGeometry(QtCore.QRect(int(topLeftPositionX + i*(boxWidth+gapWidth)), int(topLeftPositionY + j*(boxWidth+gapWidth)) \
                                                , int(boxWidth), int(boxWidth)))
                                        returnMatrix[str(i) + str(j)].setStyleSheet("border: 1px solid #000000;\n"
                "border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
                                        returnMatrix[str(i) + str(j)].setAlignment(QtCore.Qt.AlignCenter)
                                        returnMatrix[str(i) + str(j)].setObjectName("matrixBox" + str(i) + str(j) + extraString)
                                        returnMatrix[str(i) + str(j)].raise_()
                else:
                        for i in range(matrixCells):
                                for j in range(matrixCells):
                                        if lineEdit == True:
                                                returnMatrix[str(i) + str(j)] = QtWidgets.QLineEdit(Question)
                                        else:
                                                returnMatrix[str(i) + str(j)] = QtWidgets.QLabel(Question)
                                                returnMatrix[str(i) + str(j)].setText(str(matrix[j][i]))
                                        returnMatrix[str(i) + str(j)].setGeometry(QtCore.QRect(int(topLeftPositionX + i*(boxWidth+gapWidth)), int(topLeftPositionY + j*(boxWidth+gapWidth)) \
                                                , int(boxWidth), int(boxWidth)))
                                        returnMatrix[str(i) + str(j)].setStyleSheet("border: 1px solid #000000;\n"
                "border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
                                        returnMatrix[str(i) + str(j)].setAlignment(QtCore.Qt.AlignCenter)
                                        returnMatrix[str(i) + str(j)].setObjectName("matrixBox" + str(i) + str(j) + extraString)
                                        returnMatrix[str(i) + str(j)].raise_()

                bracketRealWidth, bracketRealHeight = 30, 200
                scaleCoefficient = (matrixCells*(boxWidth + gapWidth) + 50)/bracketRealHeight

                bracketPositionX = topLeftPositionX - bracketRealWidth*scaleCoefficient - 20
                bracketPositionY =  topLeftPositionY + (matrixCells/2)*boxWidth + (matrixCells - 1)*gapWidth/2\
                        - bracketRealHeight*scaleCoefficient//2

                self.matrixOneBracket = QtWidgets.QLabel(Question)
                self.matrixOneBracket.setGeometry(QtCore.QRect(int(bracketPositionX), int(bracketPositionY), \
                        int(bracketRealWidth*scaleCoefficient), int(bracketRealHeight*scaleCoefficient)))
                #print(scaleCoefficient)
                self.matrixOneBracket.setText("")
                self.matrixOneBracket.setPixmap(QtGui.QPixmap(imagesPath + "bracket.png"))
                self.matrixOneBracket.setScaledContents(True)
                self.matrixOneBracket.setObjectName("matrixOneBracket")

                bracket1PositionX = topLeftPositionX + matrixCells*boxWidth + (matrixCells-1)*gapWidth + 20
                bracket1PositionY =  topLeftPositionY + (matrixCells/2)*boxWidth + (matrixCells - 1)*gapWidth/2\
                        - bracketRealHeight*scaleCoefficient//2

                self.matrixOneBracket1 = QtWidgets.QLabel(Question)
                self.matrixOneBracket1.setGeometry(QtCore.QRect(int(bracket1PositionX), int(bracket1PositionY), \
                        int(bracketRealWidth*scaleCoefficient), int(bracketRealHeight*scaleCoefficient)))
                #print(scaleCoefficient)
                self.matrixOneBracket1.setText("")
                self.matrixOneBracket1.setPixmap(QtGui.QPixmap(imagesPath + "bracket1.png"))
                self.matrixOneBracket1.setScaledContents(True)
                self.matrixOneBracket1.setObjectName("matrixOneBracket1")

                self.matrixOneBracket.raise_()
                self.matrixOneBracket1.raise_()

                return returnMatrix, topLeftPositionX, topLeftPositionX + offset*2\
                        , topLeftPositionY
        
        self.operation = QtWidgets.QLabel(Question)
        self.operation.setText("")

        if topic == 0 or topic == 1 or topic == 2:
                createMatrix(350, 375, 200, matrix1)
                createMatrix(1600-350, 375, 200, matrix2)
                operationWidth = 100    
                self.operation.setGeometry(QtCore.QRect(int(1600/2 - operationWidth//2), 300, \
                        int(operationWidth), int(operationWidth)))

                if topic == 0:
                        self.operation.setPixmap(QtGui.QPixmap(imagesPath + "add.png"))
                elif topic == 1:
                        self.operation.setPixmap(QtGui.QPixmap(imagesPath + "subtract.png"))
                elif topic == 2:
                        self.operation.setPixmap(QtGui.QPixmap(imagesPath + "Multiply.png"))

                self.evaluateHeader = QtWidgets.QLabel(Question)
                self.evaluateHeader.setGeometry(QtCore.QRect(200, 150, 300, 70))
                self.evaluateHeader.setText("")
                self.evaluateHeader.setPixmap(QtGui.QPixmap(imagesPath + "evaluate.png"))
                self.evaluateHeader.setScaledContents(True)
                self.evaluateHeader.setObjectName("evaluateHeader")
                self.evaluateHeader.raise_()

                createMatrix(800, 700, 200, matrix3, lineEdit=False, reverse=True)

        else:
                matrixDict, topLeftPositionX, topRightPositionX, topLeftPositionY \
                        = createMatrix(800, 375, 200, matrix1)  

                if topic == 3:
                        operationWidth = 150  
                        self.operation.setPixmap(QtGui.QPixmap(imagesPath + "determinantOperation.png"))
                        self.operation.setGeometry(QtCore.QRect(int(topLeftPositionX - operationWidth - 50),\
                                 300, int(operationWidth), 100))

                        self.evaluateHeader = QtWidgets.QLabel(Question)
                        self.evaluateHeader.setGeometry(QtCore.QRect(200, 150, 600, 70))
                        self.evaluateHeader.setText("")
                        self.evaluateHeader.setPixmap(QtGui.QPixmap(imagesPath + "determinant.png"))
                        self.evaluateHeader.setScaledContents(True)
                        self.evaluateHeader.setObjectName("evaluateHeader")
                        self.evaluateHeader.raise_()

                        self.inputBox = QtWidgets.QLabel(Question)
                        self.inputBox.setGeometry(QtCore.QRect(800 - 50, 600, 100,100))
                        self.inputBox.setAutoFillBackground(False)
                        self.inputBox.setStyleSheet("border: 1px solid #000000;\n"
                "border-image: url(" + str(imagesPath) + "metal.png) 0 0 0 0 stretch stretch;")
                        self.inputBox.setAlignment(QtCore.Qt.AlignCenter)
                        self.inputBox.setObjectName("inputBox")
                        self.inputBox.setText(str(matrix3))
                        
                elif topic == 4:
                        operationWidth = 100  
                        self.operation.setPixmap(QtGui.QPixmap(imagesPath + "inverseOperation.png"))
                        self.operation.setGeometry(QtCore.QRect(int(topRightPositionX + operationWidth//2 + 20), int(topLeftPositionY - 20 - operationWidth//2), \
                                int(operationWidth), int(operationWidth)))

                        self.evaluateHeader = QtWidgets.QLabel(Question)
                        self.evaluateHeader.setGeometry(QtCore.QRect(200, 150, 500, 70))
                        self.evaluateHeader.setText("")
                        self.evaluateHeader.setPixmap(QtGui.QPixmap(imagesPath + "inverse.png"))
                        self.evaluateHeader.setScaledContents(True)
                        self.evaluateHeader.setObjectName("evaluateHeader")
                        self.evaluateHeader.raise_()

                        createMatrix(800, 700, 200, matrix3, lineEdit=False, reverse=True)

                

        self.operation.setScaledContents(True)
        self.operation.setObjectName("operation")

        

        equalsWidth = 100
        self.label_3 = QtWidgets.QLabel(Question)
        self.label_3.setGeometry(QtCore.QRect(int(350 - equalsWidth//2), 600, 100, 100))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(imagesPath + "equals.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        #self.background.raise_()
        self.operation.raise_()
        self.questionTitle.raise_()
        self.currentQuestionDigit.raise_()
        self.currentQuestionDigit1.raise_()
        self.totalQuestionsDigit.raise_()
        self.totalQuestionsDigit1.raise_()
        self.slashTitle.raise_()

    def retranslateUi(self, Question):
        _translate = QtCore.QCoreApplication.translate
        Question.setWindowTitle(_translate("Question", "Frame"))
        self.questionNo.setText(_translate("Question", "Question 1:"))
        self.label_2.setText(_translate("Question", "Matrix 1, Matrix 2"))
        self.submit.setText(_translate("Question", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Question = QtWidgets.QFrame()
    ui = Ui_Question()
    
    ui.setupUi(Question, 2, 10, 3, [[1,2],[3,4]], [[7,5],[2,6]], 5)
    
    Question.show()
    sys.exit(app.exec_())
