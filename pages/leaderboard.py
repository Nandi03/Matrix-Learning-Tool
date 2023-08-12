from UI.leaderboard_ui import Ui_leaderboard
from PyQt5.QtWidgets import QFrame


class LeaderboardPage(QFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ui = Ui_leaderboard()
        self.ui.setupUi(self)


        pass
