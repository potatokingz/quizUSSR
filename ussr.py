import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class USSRQuiz(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("USSR Loyality Test")
        self.setFixedSize(400, 600)
        self.setStyleSheet("background-color: #CC0000;")  # Soviet red

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        self.title = QLabel("☭ USSR Loyality Quiz ☭")
        self.title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.title.setStyleSheet("color: #FFD700;")  # Gold text
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)

        self.flag = QLabel("☭")
        self.flag.setFont(QFont("Arial", 64))
        self.flag.setStyleSheet("color: #FFD700;")
        self.flag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.flag)

        self.prompt = QLabel("Do you want to be part of the USSR? (yes/no)")
        self.prompt.setFont(QFont("Arial", 12))
        self.prompt.setStyleSheet("color: #FFD700;")
        self.layout.addWidget(self.prompt)

        self.answer_input = QLineEdit()
        self.answer_input.setFont(QFont("Arial", 12))
        self.answer_input.setStyleSheet("background-color: #8B0000; color: #FFD700;")
        self.layout.addWidget(self.answer_input)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.submit_btn.setStyleSheet(
            "background-color: #FFD700; color: #CC0000; padding: 8px;")
        self.submit_btn.clicked.connect(self.handle_join_response)
        self.layout.addWidget(self.submit_btn)

        self.stage = "join"
        self.comrade_name = ""
        self.comrade_age = 0
        self.quiz_index = 0
        self.score = 0

        self.q_and_a = [
            ("Who lead the Communist Party of the Soviet Union?\n(a) Vladimir Lenin\n(b) Joseph Stalin\n(c) Mikhail Gorbachev", ["b", "joseph stalin", "stalin"]),
            ("What is the simbol of the Soviet Union?\n(a) Hammer and Sickle\n(b) Red Star\n(c) Bear", ["a", "hammer and sickle"]),
            ("Has the Soviet Union sent a man into space? (yes/no)", ["yes"]),
            ("What is the capital of the USSR?\n(a) Kiev\n(b) Moscow\n(c) Leningrad", ["b", "moscow"]),
            ("Which body of goverment hold supreme power in USSR?\n(a) The Supreme Soviet\n(b) The Politburo\n(c) The KGB", ["a", "the supreme soviet"]),
            ("The Soviet economy is primarly based on:\n(a) Capitalism\n(b) Socialism\n(c) Feudalism", ["b", "socialism"]),
            ("The national anthem of USSR was composed by:\n(a) Dmitri Shostakovich\n(b) Alexander Alexandrov\n(c) Sergei Prokofiev", ["b", "alexander alexandrov"]),
            ("What year did the October Revolution take place?\n(a) 1917\n(b) 1945\n(c) 1939", ["a", "1917"]),
            ("Which city was rename to Leningrad in honour of Lenin?\n(a) St. Petersburg\n(b) Moscow\n(c) Novosibirsk", ["a", "st. petersburg", "st petersburg"]),
            ("What is official language of the USSR?\n(a) Russian\n(b) Ukrainian\n(c) Belarusian", ["a", "russian"]),
            ("Who was the first cosmonaut to orbit Earth?\n(a) Yuri Gagarin\n(b) Neil Armstrong\n(c) Valentina Tereshkova", ["a", "yuri gagarin"])
        ]

        self.setLayout(self.layout)

    def handle_join_response(self):
        answer = self.answer_input.text().strip().lower()
        if self.stage == "join":
            if answer == "yes":
                self.show_message("Great lil bro!!! You are now part of the USSR!")
                self.stage = "info_name"
                self.prompt.setText("Whats your name Comradez?:")
                self.answer_input.clear()
            elif answer == "no":
                self.show_message("Verry well Comradez! Your exsexution is tomorow!Prepare")
                self.close()
            else:
                self.show_message("whats that use 'yes' or 'no' ")
                self.answer_input.clear()

        elif self.stage == "info_name":
            if answer:
                self.comrade_name = answer.title()
                self.show_message(f"{self.comrade_name}: Hello my name is {self.comrade_name}")
                self.stage = "info_age"
                self.prompt.setText(f"USSR Agent: How old are you {self.comrade_name}?:")
                self.answer_input.clear()
            else:
                self.show_message("Type your name Comradez!")

        elif self.stage == "info_age":
            if answer.isdigit():
                self.comrade_age = int(answer)
                if self.comrade_age < 17:
                    self.show_message(f"{self.comrade_name}, your too young for the USSR")
                    self.close()
                else:
                    self.show_message(f"{self.comrade_name}, great comeradez, your USSR IQ will be revealed shortly with this Quiz...")
                    self.stage = "quiz"
                    self.quiz_index = 0
                    self.score = 0
                    self.show_next_question()
            else:
                self.show_message("Type your age number only Comradez!")

        elif self.stage == "quiz":
            self.check_answer(answer)

    def show_next_question(self):
        if self.quiz_index < len(self.q_and_a):
            question, _ = self.q_and_a[self.quiz_index]
            self.prompt.setText(f"Question {self.quiz_index + 1}:\n{question}")
            self.answer_input.clear()
        else:
            self.finish_quiz()

    def check_answer(self, answer):
        _, correct_answers = self.q_and_a[self.quiz_index]
        if answer in correct_answers:
            self.score += 1
            self.show_message("Good job comrade! Correct!")
        else:
            self.show_message("Nope, wrong answer!")
        self.quiz_index += 1
        self.show_next_question()

    def finish_quiz(self):
        min_pass = 6
        self.answer_input.setDisabled(True)
        self.submit_btn.setDisabled(True)
        self.prompt.setText(f"{self.comrade_name}, you scored {self.score} out of {len(self.q_and_a)}.")

        if self.score >= min_pass:
            self.show_message("You are worthy to serve the USSR! The Party salutes you!")
        else:
            self.show_message("You fail the Party's test. Study hard and try again.")

    def show_message(self, text):
        msg = QMessageBox(self)
        msg.setWindowTitle("USSR Loyality Test")
        msg.setText(text)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = USSRQuiz()
    window.show()
    sys.exit(app.exec())
