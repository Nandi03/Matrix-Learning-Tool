'''
        self.operation = QtWidgets.QLabel(Question)
        self.operation.setGeometry(QtCore.QRect(250, 160, 41, 41))
        self.operation.setText("")
        self.operation.setPixmap(QtGui.QPixmap(imagesPath + "Multiply.png"))
        self.operation.setScaledContents(True)
        self.operation.setObjectName("operation")
        
        self.frame_6 = QtWidgets.QFrame(Question)
        self.frame_6.setGeometry(QtCore.QRect(100, 130, 91, 95))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")

        self.lineEdit_55 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_55.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_55.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_55.setObjectName("lineEdit_55")

        self.horizontalLayout_19.addWidget(self.lineEdit_55)

        self.lineEdit_56 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_56.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_56.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_56.setObjectName("lineEdit_56")

        self.horizontalLayout_19.addWidget(self.lineEdit_56)

        self.lineEdit_57 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_57.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_57.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.horizontalLayout_19.addWidget(self.lineEdit_57)
        self.gridLayout_7.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)

        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")

        self.lineEdit_58 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_58.setAutoFillBackground(False)
        self.lineEdit_58.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_58.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.horizontalLayout_20.addWidget(self.lineEdit_58)

        self.lineEdit_59 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_59.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_59.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.horizontalLayout_20.addWidget(self.lineEdit_59)

        self.lineEdit_60 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_60.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_60.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.horizontalLayout_20.addWidget(self.lineEdit_60)

        self.gridLayout_7.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)

        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")

        self.lineEdit_61 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_61.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_61.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.horizontalLayout_21.addWidget(self.lineEdit_61)

        self.lineEdit_62 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_62.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_62.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.horizontalLayout_21.addWidget(self.lineEdit_62)

        self.lineEdit_63 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_63.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_63.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.horizontalLayout_21.addWidget(self.lineEdit_63)

        self.gridLayout_7.addLayout(self.horizontalLayout_21, 2, 0, 1, 1)

        self.matrixOneBracket = QtWidgets.QLabel(Question)
        self.matrixOneBracket.setGeometry(QtCore.QRect(200, 250, 20, 200))
        self.matrixOneBracket.setText("")
        self.matrixOneBracket.setPixmap(QtGui.QPixmap(imagesPath + "bracket.png"))
        self.matrixOneBracket.setScaledContents(True)
        self.matrixOneBracket.setObjectName("matrixOneBracket")

        self.label_17 = QtWidgets.QLabel(Question)
        self.label_17.setGeometry(QtCore.QRect(180, 130, 21, 101))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(imagesPath + "bracket1.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(Question)
        self.label_18.setGeometry(QtCore.QRect(430, 130, 21, 101))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(imagesPath + "bracket1.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")

        self.frame_7 = QtWidgets.QFrame(Question)
        self.frame_7.setGeometry(QtCore.QRect(350, 130, 91, 95))
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")

        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_8.setObjectName("gridLayout_8")

        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")

        self.lineEdit_64 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_64.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_64.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.horizontalLayout_22.addWidget(self.lineEdit_64)

        self.lineEdit_65 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_65.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_65.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.horizontalLayout_22.addWidget(self.lineEdit_65)

        self.lineEdit_66 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_66.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_66.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.horizontalLayout_22.addWidget(self.lineEdit_66)

        self.gridLayout_8.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)

        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")

        self.lineEdit_67 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_67.setAutoFillBackground(False)
        self.lineEdit_67.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_67.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.horizontalLayout_23.addWidget(self.lineEdit_67)

        self.lineEdit_68 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_68.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_68.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.horizontalLayout_23.addWidget(self.lineEdit_68)
        
        self.lineEdit_69 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_69.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_69.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.horizontalLayout_23.addWidget(self.lineEdit_69)

        self.gridLayout_8.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)

        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")

        self.lineEdit_70 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_70.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_70.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.horizontalLayout_24.addWidget(self.lineEdit_70)

        self.lineEdit_71 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_71.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_71.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.horizontalLayout_24.addWidget(self.lineEdit_71)

        self.lineEdit_72 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_72.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_72.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.horizontalLayout_24.addWidget(self.lineEdit_72)

        self.gridLayout_8.addLayout(self.horizontalLayout_24, 2, 0, 1, 1)

        self.label_19 = QtWidgets.QLabel(Question)
        self.label_19.setGeometry(QtCore.QRect(340, 130, 21, 101))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(imagesPath + "bracket.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")

        self.label_20 = QtWidgets.QLabel(Question)
        self.label_20.setGeometry(QtCore.QRect(310, 260, 21, 101))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(imagesPath + "bracket1.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")

        self.frame_8 = QtWidgets.QFrame(Question)
        self.frame_8.setGeometry(QtCore.QRect(230, 260, 91, 95))
        self.frame_8.setAutoFillBackground(False)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")

        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName("gridLayout_9")

        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")

        self.lineEdit_73 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_73.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_73.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.horizontalLayout_25.addWidget(self.lineEdit_73)

        self.lineEdit_74 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_74.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_74.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.horizontalLayout_25.addWidget(self.lineEdit_74)

        self.lineEdit_75 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_75.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_75.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.horizontalLayout_25.addWidget(self.lineEdit_75)

        self.gridLayout_9.addLayout(self.horizontalLayout_25, 1, 0, 1, 1)

        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.lineEdit_76 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_76.setAutoFillBackground(False)
        self.lineEdit_76.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_76.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.horizontalLayout_26.addWidget(self.lineEdit_76)

        self.lineEdit_77 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_77.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_77.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.horizontalLayout_26.addWidget(self.lineEdit_77)

        self.lineEdit_78 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_78.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_78.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.horizontalLayout_26.addWidget(self.lineEdit_78)

        self.gridLayout_9.addLayout(self.horizontalLayout_26, 0, 0, 1, 1)

        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")

        self.lineEdit_79 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_79.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_79.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.horizontalLayout_27.addWidget(self.lineEdit_79)

        self.lineEdit_80 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_80.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_80.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.horizontalLayout_27.addWidget(self.lineEdit_80)

        self.lineEdit_81 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_81.setStyleSheet("border: 1px solid #000000;\n"
"border-image: url(" + imagesPath + "metal.jpg) 0 0 0 0 stretch stretch;")
        self.lineEdit_81.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.horizontalLayout_27.addWidget(self.lineEdit_81)

        self.gridLayout_9.addLayout(self.horizontalLayout_27, 2, 0, 1, 1)

        self.label_21 = QtWidgets.QLabel(Question)
        self.label_21.setGeometry(QtCore.QRect(220, 260, 21, 101))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(imagesPath + "bracket.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")'''
        
        '''Question.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Question.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(Question)
        self.verticalLayout.setObjectName("verticalLayout")
        self.questionNo = QtWidgets.QLabel(Question)
        self.questionNo.setMaximumSize(QtCore.QSize(16777215, 20))
        self.questionNo.setObjectName("questionNo")
        self.verticalLayout.addWidget(self.questionNo)
        self.label_2 = QtWidgets.QLabel(Question)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Question)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.submit = QtWidgets.QPushButton(Question)
        self.submit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.submit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.submit.setObjectName("submit")
        self.verticalLayout.addWidget(self.submit)

        self.retranslateUi(Question)
        QtCore.QMetaObject.connectSlotsByName(Question)
        
        
        
        
        
        def button_click(self):
        if self.currentPage == self.pages["settings"]:
            self.numberOfQuestions = int(self.pages["settings"].ui.numberOfQuestions.currentText())
            self.numberOfQuestionsLeft = self.numberOfQuestions - 2
            self.difficulty = (self.pages["settings"].ui.difficulty.currentText()).lower()
            self.username = (self.pages["settings"]).ui.plainTextEdit.text()
            if self.validate_username() == True:
                self.q = QuizMaster(self.difficulty, self.numberOfQuestions)
                self.q.run_quiz()
                self.get_next_qs()
                self.pages["question"].ui.questionNo.setText("Question "+ str(self.questionNumber))
                self.pages["question"].ui.label_2.setText(self.operation + "\n" + self.matrix1 + "\n" + self.matrix2)
                self.questionNumber = 2
                self.load_page("question")
            else:
                self.load_page("settings")

        elif self.currentPage == self.pages["question"]:
            if self.questionNumber <= self.numberOfQuestions:
                self.get_next_qs()
                self.pages["question"].ui.questionNo.setText("Question "+ str(self.questionNumber))
                self.pages["question"].ui.label_2.setText(self.operation + "\n" + self.matrix1 + "\n" + self.matrix2)
                #input
                self.load_page("question")
                self.questionNumber = self.questionNumber + 1
            else:
                self.results()
                self.pages["results"].ui.label_2.setText(self.results_string)
                self.load_page("results")

        elif self.currentPage == self.pages["results"]:
            self.display_leaderboard()
            self.pages["leaderboard"].ui.label.setText(self.lboard_string)
            self.load_page("leaderboard")

        elif self.currentPage == self.pages["leaderboard"]:
            self.lboard_string = ""
            self.questionNumber = 1
            self.load_page("menu")'''

            '''

            def get_next_qs(self):
                topic = self.q.get_topic(self.questionNumber)
                self.operation = self.operations[topic]
                if self.questionNumber > 0:
                    if (topic == 0 or topic == 1 or topic == 2):
                        self.matrix1, self.matrix2 = self.q.read_questions_file(self.questionNumber)
                        self.matrix1 = str(self.matrix1)
                        self.matrix2 = str(self.matrix2)
                    else:
                        self.matrix1 = str(self.q.read_questions_file(self.questionNumber))
                        self.matrix2 = ""
            '''