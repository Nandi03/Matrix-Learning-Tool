from UI.resultsPage_ui import Ui_results
from PyQt5.QtWidgets import QFrame


class ResultsPage(QFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ui = Ui_results()
        self.ui.setupUi(self)
        

        pass
