import numpy as np
import random
from MatrixCalculator import MatrixCalculator
from Question import Question
import PyQt5.QtWidgets as QtWidgets


class QuizMaster():
    # change matrices_per_topic and calculator dictionary to class attributes?

    def __init__(self, level, no_of_questions, pages):
        self.level = level
        self.no_of_questions = no_of_questions
        self.pages = pages

        # topics are represented by integers 0-4: addition, subtraction, multiplication,
        # determinant, inverse

        # no. of matrices needed to make Q
        self.matrices_per_topic = (2, 2, 2, 1, 1, 1, 1)

        # topic and size of matrix/matrices randomly generated for each Q
        self.topics = []
        self.matrix_sizes = []

        self.user_answers = [None] * self.no_of_questions
        self.score = 0
        self.user_results = []

        self.calculator = {0: MatrixCalculator.addition, 1: MatrixCalculator.subtraction,
                           2: MatrixCalculator.multiplication, 3: MatrixCalculator.determinant,
                           4: MatrixCalculator.inverse}

    def get_topic(self, q_no):
        return self.topics[q_no - 1]

    def get_matrix_size(self, q_no):
        return self.matrix_sizes[q_no - 1]

    def set_matrix_size_and_topic(self):
        matrix_size = 0
        topic = 0
        if (self.level == "easy"):
            matrix_size = 2
            topic = random.randint(0, 4)

        if (self.level == "medium"):
            matrix_size = 3
            topic = random.randint(0, 4)

            # for level hard, have 4x4 matrices for topics 0-3?
        if (self.level == "hard"):
            matrix_size = 4
            topic = random.randint(0, 4)

        self.matrix_sizes.append(matrix_size)
        self.topics.append(topic)

    def make_question(self, q_no):
        self.set_matrix_size_and_topic()

        topic = self.get_topic(q_no)
        matrix_size = self.get_matrix_size(q_no)
        no_of_matrices = self.matrices_per_topic[topic]

        Question(matrix_size, no_of_matrices, topic).make_matrices_for_q()

    def make_all_questions(self):
        q_no = 0
        while (q_no != self.no_of_questions):
            q_no += 1
            self.make_question(q_no)

    def create_file(self, file_name):
        f = open(file_name, 'wb')
        f.close()

        # determines how many lines to skip and read from questions.txt for each Q

    def read_matrix_slices(self, q_no):
        skip_lines = 0
        for i in range(q_no - 1):
            skip_lines += self.matrix_sizes[i] * self.matrices_per_topic[self.topics[i]]
        row_length = self.get_matrix_size(q_no)

        return skip_lines, row_length

    # returns matrix/ matrices used in given question
    def read_questions_file(self, q_no):
        topic = self.get_topic(q_no)
        skip_lines, row_length = self.read_matrix_slices(q_no)

        matrix1 = np.genfromtxt("questions.txt", dtype=int, skip_header=skip_lines, max_rows=row_length)

        if (topic == 0 or topic == 1 or topic == 2):
            matrix2 = np.genfromtxt("questions.txt", dtype=int, skip_header=skip_lines + row_length,
                                    max_rows=row_length)
            return matrix1, matrix2

        return matrix1

    # temp. method for testing - make new method for UI
    def display_question(self, q_no):
        topic = self.get_topic(q_no)

        print("Topic: ", topic)

        matrix1 = self.read_questions_file(q_no)
        if (topic == 0 or topic == 1 or topic == 2):
            matrix1, matrix2 = self.read_questions_file(q_no)
            print(matrix1, matrix2)
            return

        return matrix1

    def calc_solution(self, q_no):
        topic = self.get_topic(q_no)

        matrix1 = self.read_questions_file(q_no)
        if (topic == 0 or topic == 1 or topic == 2):
            matrix1, matrix2 = self.read_questions_file(q_no)

        calc = MatrixCalculator()

        if (topic == 0 or topic == 1 or topic == 2):
            return self.calculator[topic](calc, matrix1, matrix2)
        elif (topic == 3):
            det = self.calculator[topic](calc, matrix1)
            return np.matrix(det)
        elif (topic == 4):
            return self.calculator[topic](calc, matrix1)
        elif (topic == 5):
            eig_vals, eig_vects = self.calculator[topic](calc, matrix1)
            return eig_vals
        # uses same method as topic 5
        elif (topic == 6):
            eig_vals, eig_vects = self.calculator[topic - 1](calc, matrix1)
            return eig_vects

    # save solution to file
    def save_solution(self, q_no):
        solution = self.calc_solution(q_no)
        file_name = 'solutions.txt'
        f = open(file_name, 'a')
        self.save_formatted_ans(q_no, solution, f)
        f.close()

    # helper: formats answers to save into solutions.txt and user_ans.txt
    def save_formatted_ans(self, q_no, answer, file):
        topic = self.get_topic(q_no)
        if (topic == 0 or topic == 1 or topic == 2 or topic == 3):
            np.savetxt(file, answer, fmt='%i')
        elif (topic == 4):
            np.savetxt(file, answer, fmt='%.2f')
        else:
            np.savetxt(file, answer, fmt='%s')

    # calculates and saves all solutions
    def calc_all_solutions(self):
        q_no = 0
        while (q_no != self.no_of_questions):
            q_no += 1
            self.save_solution(q_no)

    # temp. method for testing - adapt to fit UI
    def display_solution(self, q_no):
        solution = self.read_answer_file(q_no, 'solutions.txt')
        return solution

    # reads and formats matrices from solutions.txt and user_ans.txt
    def read_answer_file(self, q_no, file_name):
        skip_lines, row_length = self.read_answer_slice(q_no)
        dtype = self.set_matrix_dtype(q_no)
        matrix = np.genfromtxt(file_name, dtype, skip_header=skip_lines, max_rows=row_length)
        return matrix

    def set_matrix_dtype(self, q_no):
        topic = self.get_topic(q_no)
        if (topic == 4):
            dtype = float
        elif (topic == 5 or topic == 6):
            dtype = str
        else:
            dtype = int
        return dtype

    # determines no. of lines to skip and then read
    # for given a Q from solutions and user_ans files
    def read_answer_slice(self, q_no):
        skip_lines = 0
        for i in range(q_no - 1):
            topic = self.topics[i]
            if (topic == 3):
                skip_lines += 1
            else:
                skip_lines += self.matrix_sizes[i]

        topic = self.get_topic(q_no)
        if (topic == 3):
            row_length = 1
        else:
            row_length = self.get_matrix_size(q_no)

        return skip_lines, row_length

    # UI: adapt method
    def get_user_ans(self, q_no):
        dtype = self.set_matrix_dtype(q_no)
        #print("Enter the entries in a single line (separated by space): ")
        user_input = []
        topic = self.get_topic(q_no)
        if topic != 3:
            matrixDimension = len(self.read_questions_file(q_no)[0])
            for i in range(1,matrixDimension+1):
                newRow = []
                for j in range(1,matrixDimension+1):
                    newRow.append(float(self.pages["question" + str(q_no)].findChild(\
                        QtWidgets.QLineEdit, ("matrixBox" + str(i - 1) + str(j - 1) + "input")).text()))
                user_input.append(newRow)
        else:
            user_input.append([float(self.pages["question" + str(q_no)].findChild(\
                        QtWidgets.QLineEdit, ("matrixBox" + "11" + "input")).text())])
            
        return user_input

    # saves user's answer in user_answers[]
    def save_user_ans(self, q_no):
        self.user_answers[q_no - 1] = self.get_user_ans(q_no)

    # turns each answer in user_answers[] from a list
    # to a matrix. Saves all answers to user_ans.txt
    def save_all_user_ans(self):
        q_no = 0
        while (q_no != self.no_of_questions):
            q_no += 1
            #user_ans = self.user_answers[q_no - 1]
            user_ans = self.get_user_ans(q_no)
            self.save_user_ans_to_file(np.matrix(user_ans), 'user_ans.txt', q_no)

            # helper: reshapes user_ans matrix to match solutions.txt

    # and saves it to user_ans.txt
    def save_user_ans_to_file(self, user_ans, file_name, q_no):
        f = open(file_name, 'a')
        matrix_size = self.get_matrix_size(q_no)
        topic = self.get_topic(q_no)

        if (topic == 3):
            user_ans = np.matrix(user_ans)
        elif (topic == 5):
            user_ans = np.matrix(user_ans).reshape(matrix_size, 1)
        else:
            user_ans = np.matrix(user_ans).reshape(matrix_size, matrix_size)

        self.save_formatted_ans(q_no, user_ans, f)
        f.close()

    # temp. method for testing - adapt to fit UI
    def display_user_ans(self, q_no):
        user_ans = self.read_answer_file(q_no, 'user_ans.txt')
        return user_ans

    def mark_question(self, solution, user_ans):
        if (np.array_equal(solution, user_ans)):
            self.score += 1
            self.user_results.append(1)
            return True
        else:
            self.user_results.append(0)
            return False

    def mark_all_questions(self):
        q_no = 0
        while (q_no != self.no_of_questions):
            q_no += 1
            solution = self.read_answer_file(q_no, 'solutions.txt')
            user_ans = self.read_answer_file(q_no, 'user_ans.txt')
            self.mark_question(solution, user_ans)
        return self.user_results

    def find_percentage(self):
        return int((self.score / self.no_of_questions) * 100)

    # temp. method used for testing
    def question(self, q_no):
        #print("Question ", q_no, ":\n")
        self.display_question(q_no)
        self.save_user_ans(q_no)

    # service method - adapt to fit UI...currently an
    # organised mess used for simulating quiz movement
    def run_quiz(self):
        self.create_file('questions.txt')
        self.create_file('user_ans.txt')

        self.make_all_questions()

        self.create_file('solutions.txt')
        self.calc_all_solutions()

        # display Q1
    #    q_no = 1
    #    self.question(q_no)
        # print(self.user_answers)

    #    quiz_movement = str(input("next? "))

        # display Q2
    #    if (quiz_movement == "next"):
    #        q_no += 1
    #        self.question(q_no)
        # print(self.user_answers)

    #    while (q_no != self.no_of_questions):
    #        quiz_movement = str(input("next or back? "))
    #        if quiz_movement == "next":
    #            q_no += 1
    #            self.question(q_no)

    #        elif quiz_movement == "back":
    #            q_no -= 1
    #            self.question(q_no)
            # print(self.user_answers)

    #    submit = str(input("submit quiz? "))

    #    if (submit == "submit"):
    #        self.save_all_user_ans()
    #        self.mark_all_questions()
    #
    #        final_score = self.find_percentage()
    #        print("Score: ", final_score)
    #        # UI: use to show results page
    #        print("Results: ", self.user_results)

    #    review = str(input("review quiz? "))
    #    if (review == "review"):
    #        # ask user to select a question_no to review...
             # or just review the whole quiz?

            # currently reviewing whole quiz in one go (i.e., one frame) -
            # can change to display each Q on a diff. page
    #        q_no = 0
    #        while (q_no != self.no_of_questions):
    #            q_no += 1
    #            print("Question ", q_no, ":\n")
    #            self.display_question(q_no)
    #            self.display_solution(q_no)
    #            self.display_user_ans(q_no)

