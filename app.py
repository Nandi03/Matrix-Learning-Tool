from ast import In, Num
import audioop
from email.mime import audio
import os
import sys
from cProfile import label
import numpy as np

from PyQt5 import QtCore, QtMultimedia

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

import time


from pages.leaderboard import LeaderboardPage
from pages.menupage import MenuPage
from pages.questionPage import QuestionPage
from pages.correctedQuestionPage import correctedQuestionPage
from pages.quizSettings import QuizSettings
from pages.resultsPage import ResultsPage
from pages.revisionPage import RevisionPage
from UI.MainWindow_ui import Ui_MainWindow
from QuizMaster import QuizMaster
from Leaderboard import Leaderboard

from pathlib import Path, PureWindowsPath
from os.path import dirname, abspath

imagesPath = dirname(abspath(__file__)) + "/images/"
realImagesPath = []
for i in imagesPath:
    realImagesPath.append(i)

del(realImagesPath[0])
del(realImagesPath[0])

for i in range(len(realImagesPath)):
    if realImagesPath[i] == "\\":
        realImagesPath[i] = "/"

imagesPath = "".join(realImagesPath)

audioPath = dirname(abspath(__file__)) + "/images/"
realAudioPath = []
for i in audioPath:
    realAudioPath.append(i)

del(realAudioPath[0])
del(realAudioPath[0])

for i in range(len(realAudioPath)):
    if realAudioPath[i] == "\\":
        realAudioPath[i] = "/"

imagesPath = "".join(realAudioPath)

class App:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        
        self.numberOfQuestions = 0
        self.numberOfQuestionsLeft = 0
        self.difficulty = ""
        self.score = "0"
        self.lboard_string = ""
        self.matrix1 = ""
        self.matrix2 = ""
        self.questionNumber = 1
        self.results_string = ""
        self.resultsPageQuestion = 0

        self.operations = {
            0: "Add: ", 
            1: "Subtract: ",
            2: "multiply: ", 
            3: "Find the determinant of: ",
            4: "Find the inverse of: ", 
            5: "Find eigenvectors & eigenvalues of: "
        
        }

        self.operation = 0

        self.window.show()
        self.pages = {
            "menu": MenuPage,
            "settings": QuizSettings, 
            #"question": QuestionPage,
            "results": ResultsPage,
            "leaderboard": LeaderboardPage,
            "revise": RevisionPage
        }
        
        self.pages = self.init_pages()
        self.currentPage = self.pages["menu"]

        #button connections

        self.pages["revise"].ui.menuButton.clicked.connect(lambda x: self.loadPage("menu"))
        
        self.pages["menu"].ui.startButton.clicked.connect(lambda x: self.loadPage("settings"))
        self.pages["menu"].ui.reviseButton.clicked.connect(lambda x: self.loadPage("revise"))
        self.pages["settings"].ui.backButton.clicked.connect(lambda x: self.loadPage("menu"))
        self.pages["settings"].ui.startButton.clicked.connect(lambda x: self.startQuiz())

        self.pages["results"].ui.leaderboardButton.clicked.connect(lambda x: self.display_leaderboard())
        self.pages["results"].ui.leaderboardButton.clicked.connect(lambda x: self.loadPage("leaderboard"))
        self.pages["results"].ui.retryButton.clicked.connect(lambda x: self.loadPage("menu"))

        self.pages["results"].ui.nextButton.clicked.connect(self.resultsNextButton)
        self.pages["results"].ui.backButton.clicked.connect(self.resultsBackButton)
        self.pages["results"].ui.reviseButton.clicked.connect(lambda x: self.loadPage("revise"))
        self.pages["leaderboard"].ui.retryButton.clicked.connect(lambda x: self.loadPage("menu"))
        self.pages["leaderboard"].ui.reviseButton.clicked.connect(lambda x: self.loadPage("revise"))

        self.currentPage.show()

        sys.exit(self.app.exec())

    def resultsBackButton(self):
        if self.resultsPageQuestion > 1:
            self.resultsPageQuestion -= 1
   

            self.pages["results"].ui.currentQuestionDigit.setPixmap(QtGui.QPixmap(\
                imagesPath + str(self.resultsPageQuestion//10)  + ".png"))
            self.pages["results"].ui.currentQuestionDigit1.setPixmap(QtGui.QPixmap(\
                imagesPath + str(self.resultsPageQuestion%10)  + ".png"))
            
            self.pages["results"].ui.totalQuestionsDigit.setPixmap(QtGui.QPixmap(imagesPath + str(self.numberOfQuestions//10) + ".png"))
            self.pages["results"].ui.totalQuestionsDigit1.setPixmap(QtGui.QPixmap(imagesPath + str(self.numberOfQuestions%10) + ".png"))

            solution = self.q.read_answer_file(self.resultsPageQuestion, 'solutions.txt')
            user_ans = self.q.read_answer_file(self.resultsPageQuestion, 'user_ans.txt')
            self.pages["results"].ui.userAns.setText("Your answer: \n " + str(user_ans))
            self.pages["results"].ui.correctAns.setText("Correct answer: \n" + str(solution))

            self.pages["results"].ui.viewQuestion.clicked.connect(lambda x: \
                self.loadPage("correctedQuestion" + str(self.resultsPageQuestion)))

            if np.all(solution == user_ans):
                self.pages["results"].ui.correctnessHeader.setPixmap(QtGui.QPixmap(imagesPath \
                    + "correct.png"))
            else:
                self.pages["results"].ui.correctnessHeader.setPixmap(QtGui.QPixmap(imagesPath \
                    + "incorrect.png"))

            self.loadPage("results")
        else:
            return

    def resultsNextButton(self):
        
        if self.resultsPageQuestion < self.numberOfQuestions:
            #print(self.pages["results"].ui.setupUi.test)
            self.resultsPageQuestion += 1

            self.pages["results"].ui.currentQuestionDigit.clear()
            self.pages["results"].ui.currentQuestionDigit1.clear()

            self.pages["results"].ui.currentQuestionDigit.setPixmap(QtGui.QPixmap(\
            imagesPath + str(self.resultsPageQuestion//10)  + ".png"))
            self.pages["results"].ui.currentQuestionDigit1.setPixmap(QtGui.QPixmap(\
            imagesPath + str(self.resultsPageQuestion%10)  + ".png"))

            self.pages["results"].ui.totalQuestionsDigit.setPixmap(QtGui.QPixmap(imagesPath + str(self.numberOfQuestions//10) + ".png"))
            self.pages["results"].ui.totalQuestionsDigit1.setPixmap(QtGui.QPixmap(imagesPath + str(self.numberOfQuestions%10) + ".png"))


            solution = self.q.read_answer_file(self.resultsPageQuestion, 'solutions.txt')
            user_ans = self.q.read_answer_file(self.resultsPageQuestion, 'user_ans.txt')
            self.pages["results"].ui.userAns.setText("Your answer: \n " + str(user_ans))
            self.pages["results"].ui.correctAns.setText("Correct answer: \n" + str(solution))

            self.pages["results"].ui.viewQuestion.clicked.connect(lambda x: \
                self.loadPage("correctedQuestion" + str(self.resultsPageQuestion)))
            
            
            if np.all(solution == user_ans):
                self.pages["results"].ui.correctnessHeader.setPixmap(QtGui.QPixmap(imagesPath \
                    + "correct.png"))
            else:
                self.pages["results"].ui.correctnessHeader.setPixmap(QtGui.QPixmap(imagesPath \
                    + "incorrect.png"))

            self.loadPage("results")

        else:
            return
                
    def loadPage(self, pageName):
        '''openPosition, openPosition1 = QtCore.QRect(0, -900, 1600, 900), QtCore.QRect(0, 900, 1600, 900)
        closedPosition, closedPosition1 = QtCore.QRect(0, -450, 1600, 900), QtCore.QRect(0, 1350, 1600, 900)
        
        temporaryImage = QtWidgets.QLabel(self.currentPage)
        temporaryImage.setText("")
        temporaryImage.setPixmap(QtGui.QPixmap(imagesPath + "shutter.png"))
        temporaryImage.setScaledContents(True)
        temporaryImage.setObjectName("upperShutter")
        temporaryImage.raise_()

        animation = QtCore.QPropertyAnimation(temporaryImage, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(openPosition)
        animation.setEndValue(closedPosition)

        temporaryImage1 = QtWidgets.QLabel(self.currentPage)
        temporaryImage1.setText("")
        temporaryImage1.setPixmap(QtGui.QPixmap(imagesPath + "shutter.png"))
        temporaryImage1.setScaledContents(True)
        temporaryImage1.setObjectName("lowerShutter")
        temporaryImage.raise_()

        animation1 = QtCore.QPropertyAnimation(temporaryImage1, b"geometry")
        animation1.setDuration(500)
        animation1.setStartValue(openPosition1)
        animation1.setEndValue(closedPosition1)

        animation.start()
        animation1.start()
        time.sleep(500)

        temporaryImage.deleteLater()
        temporaryImage = None
        temporaryImage1.deleteLater()
        temporaryImage1 = None'''

        
        '''
        Url = QtCore.QUrl.fromLocalFile("audioPath" + nextQuestion.mp3")

        content = QtMultimedia.QMediaContent(Url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.setVolume(50)
        player.play()'''

        self.currentPage.hide()
        self.currentPage = self.pages[pageName]
        self.currentPage.show()

        '''temporaryImage = QtWidgets.QLabel(self.currentPage)
        temporaryImage.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        temporaryImage.setText("")
        temporaryImage.setPixmap(QtGui.QPixmap(imagesPath + "shutter.png"))
        temporaryImage.setScaledContents(True)
        temporaryImage.setObjectName("upperShutter")
        temporaryImage.raise_()

        animation = QtCore.QPropertyAnimation(temporaryImage, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(openPosition)
        animation.setEndValue(closedPosition)

        temporaryImage1 = QtWidgets.QLabel(self.currentPage)
        temporaryImage1.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        temporaryImage1.setText("")
        temporaryImage1.setPixmap(QtGui.QPixmap(imagesPath + "shutter.png"))
        temporaryImage1.setScaledContents(True)
        temporaryImage1.setObjectName("lowerShutter")
        temporaryImage.raise_()

        animation1 = QtCore.QPropertyAnimation(temporaryImage1, b"geometry")
        animation1.setDuration(500)
        animation1.setStartValue(openPosition1)
        animation1.setEndValue(closedPosition1)

        animation.start()
        animation1.start()
        time.sleep(500)

        temporaryImage.deleteLater()
        temporaryImage = None
        temporaryImage1.deleteLater()
        temporaryImage1 = None'''



    def nextPage(self, currentQuestion, results=False):
        condition = True
        topic = self.q.get_topic(currentQuestion)
        if topic != 3:
            matrixDimension = len(self.q.read_questions_file(currentQuestion)[0])
            for i in range(1,matrixDimension+1):
                for j in range(1,matrixDimension+1):
                    temp = self.validateInput(self.pages["question" + str(currentQuestion)].findChild(\
                        QLineEdit, ("matrixBox" + str(j - 1) + str(i - 1) + "input")).text())
                    
                    if temp == False:
                        condition = False
                    
        else:
            temp = self.validateInput(self.pages["question" + str(currentQuestion)].findChild(\
                        QLineEdit, ("matrixBox" + "11" + "input")).text())
            if temp == False:
                condition = False
        
        if condition:
            if results == False:
                self.loadPage("question" + str(currentQuestion+1))
            else:
                self.results()


    def startQuiz(self):
        self.numberOfQuestions = int(self.pages["settings"].ui.questionsComboBox.currentText())
        #self.numberOfQuestions = 10
        self.numberOfQuestionsLeft = self.numberOfQuestions - 2

        self.difficulty = (self.pages["settings"].ui.difficultyComboBox.currentText()).lower()
        #self.difficulty = "easy"
        self.username = (self.pages["settings"]).ui.lineEdit_82.text()
        if self.validate_username() == True:
            self.q = QuizMaster(self.difficulty, self.numberOfQuestions, self.pages)
            self.q.run_quiz()

            for questionNumber in range(1, self.numberOfQuestions + 1):
                topic = self.q.get_topic(questionNumber)
                matrix1, matrix2 = "", ""
                if topic == 0 or topic == 1 or topic == 2:
                    matrix1, matrix2 = self.q.read_questions_file(questionNumber)
                else:
                    matrix1 = self.q.read_questions_file(questionNumber)
                
                _page = QuestionPage(self.ui.centralwidget, questionNumber, self.numberOfQuestions, \
                     topic, matrix1, matrix2)
                
                self.ui.horizontalLayout.addWidget(_page)
                _page.hide()
                self.pages["question" + str(int(questionNumber))] = _page
            
            for i in range(2, self.numberOfQuestions):
                self.pages["question" + str(i)].ui.backButton.clicked.connect(\
                    lambda x, i=i: self.loadPage("question" + str(i-1)))
                self.pages["question" + str(i)].ui.nextButton.clicked.connect(\
                    lambda x, i=i: self.nextPage(i))

            self.pages["question1"].ui.backButton.clicked.connect(lambda x: self.loadPage("settings"))
            self.pages["question1"].ui.nextButton.clicked.connect(lambda x: self.nextPage(1))
            self.pages["question" + str(self.numberOfQuestions)].ui.backButton.clicked.connect(\
                lambda x: self.loadPage("question" + str(self.numberOfQuestions - 1)))
            self.pages["question" + str(self.numberOfQuestions)].ui.nextButton.clicked.connect(\
                lambda x: self.nextPage(self.numberOfQuestions, results=True))

            self.questionNumber = 1
            self.loadPage("question1")
        
        else:
            #show error with settings
            self.loadPage("settings")

    def init_pages(self):
        _pages = {}

        for page in self.pages:
            _page = self.pages[page](self.ui.centralwidget)
            self.ui.horizontalLayout.addWidget(_page)
            _page.hide()
            _pages[page] = _page

        return _pages            
    
    
    def validate_username(self):
        if len(self.username) == 0: 
            return False
        
        for char in self.username:
            if char != " ":
                pass
            else:
                return False        
        else:
            return True
        
    def validateInput(self, input):
        validation_rule = QtGui.QDoubleValidator(-999999, 999999, 2)
        if validation_rule.validate(input, 4)[0] == QtGui.QValidator.Acceptable:
            return True
        else:
            return False
    def display_leaderboard(self):
        entry = Leaderboard(self.username, str(self.score), self.difficulty)
        Leaderboard.add(entry)
        lboard_list = Leaderboard.leaderboard(entry)
        n = 0
        for entry1 in lboard_list:
            score = ""
            username = ""
            date = ""
            components = {1:score, 2: username, 3: date, 4:date}
            i = 1
            for char in entry1:
                if char == " ":
                    i += 1
                else:
                    components[i] = components[i] + char
            
            if n == 0:
                self.pages["leaderboard"].ui.user1Label.setText(components[2])
                self.pages["leaderboard"].ui.percentage1Label.setText(components[1])
                self.pages["leaderboard"].ui.date1Label.setText(components[3] + " " + components[4])
            elif n == 1:
                self.pages["leaderboard"].ui.user2Label.setText(components[2])
                self.pages["leaderboard"].ui.percentage2Label.setText(components[1])
                self.pages["leaderboard"].ui.date2Label.setText(components[3] + " " + components[4])
            elif n == 2:
                self.pages["leaderboard"].ui.user3Label.setText(components[2])
                self.pages["leaderboard"].ui.percentage3Label.setText(components[1])
                self.pages["leaderboard"].ui.date3Label.setText(components[3] + " " + components[4])

            elif n == 3:
                self.pages["leaderboard"].ui.user4Label.setText(components[2])
                self.pages["leaderboard"].ui.percentage4Label.setText(components[1])
                self.pages["leaderboard"].ui.date4Label.setText(components[3] + " " + components[4])
  
            elif n == 4:
                self.pages["leaderboard"].ui.user5Label.setText(components[2])
                self.pages["leaderboard"].ui.percentage5Label.setText(components[1])
                self.pages["leaderboard"].ui.date5Label.setText(components[3] + components[4])
    
            n += 1

        
    def results(self):
        self.resultsPageQuestion = 0
        self.q.save_all_user_ans()
        results_list = self.q.mark_all_questions()
        self.score = self.q.find_percentage() 
        #"                                 " + 
        self.pages["results"].ui.percentageLabel.setText(str(self.score) + "%")
        self.pages["results"].ui.percentageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pages["results"].ui.percentageLabel.setFont(QtGui.QFont('Arial', 20))

        self.pages["results"].ui.currentQuestionDigit.clear()
        self.pages["results"].ui.currentQuestionDigit1.clear()

        self.pages["results"].ui.viewQuestion.clicked.connect(lambda x: \
                self.loadPage("correctedQuestion" + "1"))

        for questionNumber in range(1, self.numberOfQuestions + 1):
                topic = self.q.get_topic(questionNumber)
                matrix1, matrix2, matrix3 = "", "", ""
                if topic == 0 or topic == 1 or topic == 2:
                    matrix1, matrix2 = self.q.read_questions_file(questionNumber)
                else:
                    matrix1 = self.q.read_questions_file(questionNumber)

                matrix3 = self.q.read_answer_file(questionNumber, 'solutions.txt')
                
                _page = correctedQuestionPage(self.ui.centralwidget, questionNumber, self.numberOfQuestions, \
                     topic, matrix1, matrix2, matrix3)

                self.ui.horizontalLayout.addWidget(_page)
                _page.hide()
                self.pages["correctedQuestion" + str(int(questionNumber))] = _page

                _page.ui.resultsButton.clicked.connect(lambda x: self.loadPage("results"))
                

        self.resultsNextButton()
        
        self.loadPage("results")

if __name__ == "__main__":
    app = App()
