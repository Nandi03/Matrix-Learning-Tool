import datetime


class Leaderboard:

    def __init__(self, username, score, difficulty):
        self.username = username
        self.score = score
        self.leaderboard_list = []
        self.scores_list = []
        self.difficulty = difficulty

    # open a text file depending on the difficulty selected to append to the file.
    def open(self):
        self.leaderboard_file = open("Leaderboard_" + self.difficulty + ".txt", "a")

    # open a text file depending on the difficulty selected to read from the file.
    def open_read(self):
        self.leaderboard_file = open("Leaderboard_" + self.difficulty + ".txt", "r")

    # Close the text file.
    def close(self):
        self.leaderboard_file.close()

    # Add an entry with the score, username, date and time to the text file.
    def add(self):
        self.open()
        time = datetime.datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
        entry = self.score + " " + self.username + " " + time
        self.leaderboard_file.write(entry + "\n")
        self.close()

    # Reads the first five entries in the text file and stores them in the lists scores_list and leaderboard_list.
    def first_five(self):
        self.open_read()
        
        for i in range(0, 5):
            self.leaderboard_list.append(self.leaderboard_file.readline())
            entry_len = len(self.leaderboard_list[i])
            for n in range(entry_len - 1):
                if n == 0:
                    self.scores_list.append(self.leaderboard_list[i][n])
                elif self.leaderboard_list[i][n] != " ":
                    self.scores_list[i] = self.scores_list[i] + self.leaderboard_list[i][n]
                else:
                    break

        for i in range(len(self.scores_list)):
            self.scores_list[i] = int(self.scores_list[i])
        return self.scores_list, self.leaderboard_list

    # Reads the next line in the text file and returns the entry made and the score.
    def next_entry(self):
        entry_score = ""
        entry = self.leaderboard_file.readline()
        entry_len = len(entry)
        for i in range(entry_len - 1):
            if entry[i] != " ":
                entry_score = entry_score + entry[i]
            else:
                break

        if entry_score != "":
            entry_score = int(entry_score)
            return entry_score, entry
        else:
            return 0, 0

    # Sorts the entries and scores in descending order.
    def bubble_sort(self):
        for i in range(len(self.scores_list)):
            for j in range(len(self.scores_list) - 1):
                if self.scores_list[j] <= self.scores_list[j + 1]:
                    self.scores_list[j], self.scores_list[j + 1] = self.scores_list[j + 1], self.scores_list[j]
                    self.leaderboard_list[j], self.leaderboard_list[j + 1] = self.leaderboard_list[j + 1], self.leaderboard_list[j]

    # insert next entry to the scores_list and leaderboard_list and re-sort the lists.
    def insert(self):
        entry_score, entry = self.next_entry()
        if entry_score == 0 and entry == 0:
            return True
        for t in range(len(self.scores_list)):
            if entry_score >= self.scores_list[t]:
                self.scores_list.append(entry_score)
                self.leaderboard_list.append(entry)
                self.bubble_sort()
                self.remove()
                break
        return False

    # Remove the last element in the leaderboard_list and scores_list.
    def remove(self):
        if len(self.scores_list) != 0 or len(self.leaderboard_list) != 0:
            self.scores_list.pop()
            self.leaderboard_list.pop()

    # Output the leaderboard, line by line.
    def display(self):
        for i in range(len(self.leaderboard_list)):
            print(self.leaderboard_list[i])

    def leaderboard(self):

        Leaderboard.first_five(self)
        end = False

        self.bubble_sort()
        while end is False:
            end = self.insert()
        self.close()
        self.bubble_sort()

        return self.leaderboard_list
