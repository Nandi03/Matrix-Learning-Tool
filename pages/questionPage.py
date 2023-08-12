from UI.questionPage_ui import Ui_Question
from PyQt5.QtWidgets import QFrame


class QuestionPage(QFrame):
    def __init__(self, master, questionNumber, totalQuestions, topic, matrix1, matrix2):
        super().__init__(master)

        self.ui = Ui_Question()
        self.ui.setupUi(self, questionNumber, totalQuestions, topic, matrix1, matrix2)
        #self.ui.questionNo.setText("Question "+ str(number))
        

        pass