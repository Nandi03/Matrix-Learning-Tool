from UI.menupage_ui import Ui_startPage
from PyQt5.QtWidgets import QFrame


class MenuPage(QFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ui = Ui_startPage()
        self.ui.setupUi(self)
        

        pass
