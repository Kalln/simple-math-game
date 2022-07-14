from PySide6.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QLineEdit
from PySide6.QtCore import Qt, Slot
import sys
import random


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # feedback displays if user guessed correct or incorrect.
        self.feedback = QLabel("")
        self.feedback.setAlignment(Qt.AlignCenter)
        self.feedback.setStyleSheet("""
            color: #FFFFFF;
            font-family: Titillium;
            font-size: 32px;
        """)


        # displays math problem
        self.text = QLabel("Press the button to start")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("""
            color: Black;
            font-family: Titillium;
            font-size: 32px;
        """)

        # To verify user input.
        self.button = QPushButton("Click me")
        self.button.setStyleSheet("""
            font-size: 20px;
        """)


        # User enters answer
        self.form = QLineEdit()
        self.form.setStyleSheet("""
            font-size: 32px;
        """)

        #layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.feedback)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.form)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        #button action
        self.button.clicked.connect(self.onClick)

    def onClick(self):
        # User wont get feedback first time clicking button, since no problem has been displayed
        if (self.text.text() == "Press the button to start"):
            runned = True
            get_new_problem(self) 
            return

        # check result and give feedback to user
        user_input = self.form.text()
        print(user_input)
        result = calculate_correct(self.text.text())

        # check if user input is correct result and generate new math problem
        if (int(user_input) == result[2]):
            user_feedback(self, True)
            get_new_problem(self)
            return
        
        # If user is wrong
        user_feedback(self, False)
        get_new_problem(self)
            
    
def get_new_problem(self):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    self.text.setText(f"{num1} + {num2}")
    self.form.clear()

def user_feedback(self, answer_is: bool):
    if answer_is:
        self.feedback.setText("CORRECT")
        self.feedback.setStyleSheet("""
            color: Green;
            font-family: Titillium;
            font-size: 32px;
        """)
        return
    self.feedback.setText("INCORRECT")
    self.feedback.setStyleSheet("""
            color: Red;
            font-family: Titillium;
            font-size: 32px;
        """)


def calculate_correct(text) -> list:
    tmp = text.split("+")
    results = list(map(int, tmp))
    results.append(results[0] + results[1])
    return results

if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())