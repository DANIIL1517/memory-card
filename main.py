from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, choice

app = QApplication([])
from main_window import *

# Клас для створення запитань
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.correct = 0
        self.attempt = 0
    
    # метод для врахування неправильної відповіді
    def got_wrong(self):
        self.attempt += 1
    
    # метод для врахування правильної відповіді
    def got_right(self):
        self.attempt += 1
        self.correct += 1

# створюємо 4 питання (об'єкти класу Question)
q1 = Question("Яблуко", "apple", "application", "apply", "pinapple")
q2 = Question("Дім", "house", "horse", "hurry", "hour")

# список кнопок та список питань
questions = [q1, q2] 
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 

# Функція, яка вдіображає нове питання та варіанти відповідей до нього
def new_question():
    # обираємо рандомне питання
    global current_question
    current_question = choice(questions) 
    # розставляємо по віджетам формулюваня питання та його правильну відповідь
    lb_Question.setText(current_question.question)
    lb_Correct.setText(current_question.answer)
    # перемішуємо радіокнопки
    shuffle(radio_buttons)
    # розставляємо варіанти відповідей
    radio_buttons[0].setText(current_question.answer)
    radio_buttons[1].setText(current_question.wrong_answer1)
    radio_buttons[2].setText(current_question.wrong_answer2)
    radio_buttons[3].setText(current_question.wrong_answer3)

new_question()

# Функція, яка перевіряє обрану відповідь
def check():
    for button in radio_buttons:
        if button.isChecked():
            if button.text() == lb_Correct.text():
                lb_Result.setText("Правильно")
                current_question.got_right()
            else:
                lb_Result.setText("Неправильно")
                current_question.got_wrong()



# Функція, яка буде спрацьовувати при натисканні на кнопку "Відповісти"
def click_ok():
    if btn_OK.text() == "Відповісти":
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText("Наступне питання")
    else:
        new_question()
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText("Відповісти")

# підключаємо функцію click_ok() до кнопки "Відповісти"
btn_OK.clicked.connect(click_ok)

window.show()
app.exec()