from UI.revisionPage_ui import Ui_revision
from PyQt5.QtWidgets import QFrame


class RevisionPage(QFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ui = Ui_revision()
        self.ui.setupUi(self)
        

        pass
