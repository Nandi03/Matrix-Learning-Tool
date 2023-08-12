from UI.quizSettings_ui import Ui_Frame
from PyQt5.QtWidgets import QFrame


class QuizSettings(QFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        

        pass
