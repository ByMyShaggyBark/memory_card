from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QButtonGroup, QRadioButton, QHBoxLayout, QGroupBox
from random import shuffle
from random import randint 

app = QApplication([])
lb_Question = QLabel('Загадка от Жака Фреско')
btn_OK = QPushButton('Ответить')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

RadioGroupBox = QGroupBox('Варианты ответов')
var_1 = QRadioButton('Вариант 1')
var_2 = QRadioButton('Вариант 2')
var_3 = QRadioButton('Вариант 3')
var_4 = QRadioButton('Вариант 4')

questions_list = []
questions_list.append(Question('Государственный язык Бразилии','Португальский' ,'Бразильский' ,'Испанский' ,'Мексиканский'))
questions_list.append(Question('Самая северная страна','Канада','Северная Америка','Гренландия','Антарктида'))
questions_list.append(Question('Сколько лет длилась Столетняя война?','116','100','117','17'))
questions_list.append(Question('Какой национальности не существует?','Смурфы','Энцы','Чулымцы','Алеуты'))
questions_list.append(Question('Какая самая многонациональная страна?','Индия','Россия','США','Китай'))
questions_list.append(Question('Какая самая многочисленная раса в мире?','Европеоидная','Негроидная','Американоидная','Монголоидная'))
questions_list.append(Question('Самая старая страна в мире','Япония','Россия','Египет','Китай'))
questions_list.append(Question('Какая самая маленькая страна по площади?','Ватикан','Монако','Люксембург','Германия'))
questions_list.append(Question('Самая малочисленная нация в мире','Питкэрнцы','Монголы','Чулымцы','Англосаксы'))
questions_list.append(Question('Какая самая бедная страна в мире?','Южный Судан','Нигерия','Чад','Африка'))

RadioGroup = QButtonGroup()
RadioGroup.addButton(var_1)
RadioGroup.addButton(var_2)
RadioGroup.addButton(var_3)
RadioGroup.addButton(var_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(var_1)
layout_ans2.addWidget(var_2)
layout_ans3.addWidget(var_3)
layout_ans3.addWidget(var_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('угадай')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    var_1.setChecked(False)
    var_2.setChecked(False)
    var_3.setChecked(False)
    var_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [var_1, var_2, var_3, var_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1
        print('Статистика\nВсего вопросов: ', window.total, '\nПравильных ответов: ', window.score)
        print('Рейтинг: ', window.score/window.total * 100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\nВсего вопросов: ', window.total, '\nПравильных ответов: ', window.score)
            print('Рейтинг: ', window.score/window.total * 100, '%')

def next_question():
    window.total +=1
    cur_question = randint(0, len(questions_list) -1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo card')
window.total = 0
window.score = 0

btn_OK.clicked.connect(click_OK)

next_question()
window.resize(400,300)
window.show()
app.exec_()
#не менее 10 вопросов