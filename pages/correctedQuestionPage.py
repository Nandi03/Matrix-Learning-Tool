from UI.correctedQuestionPage_ui import Ui_Question
from PyQt5.QtWidgets import QFrame


class correctedQuestionPage(QFrame):
    def __init__(self, master, questionNumber, totalQuestions, topic, matrix1, matrix2, matrix3):
        super().__init__(master)

        self.ui = Ui_Question()
        self.ui.setupUi(self, questionNumber, totalQuestions, topic, matrix1, matrix2, matrix3)
        #self.ui.questionNo.setText("Question "+ str(number))
        

        pass