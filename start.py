from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])
 
from main_window import *
 
 
# Питання
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1 
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0 

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Який океан найбільший на землі?", "Тихий", "Південний", 'Індійський', 'Атлантичний')
q2 = Question("Який орган у тілі людини найголовніший?", "Мозок", "Кішечник", "Серце", "Легені")
q3 = Question("Яка столиця Франції?", "Париж", "Вашингтон", "Рим", "Берлін")
q3 = Question("Яка планета найближча до Сонця?", "Меркурій", "Венера", "Юпітер", "Венера")
q4 = Question("Яка ріка є найдовшою у світі?", "Ніл", "Амазонка", "Янцзи", "Місісіпі")
q5 = Question("Хто написав «Гаррі Поттера»?", "Джуан Роулінг", "Стівен Кінг", "Толкін", "K. C. Льюїс")
q6 = Question("Яка з цих тварин є ссавцем?", "Дельфін", "Риба", "Птиця ", "Ящірка")
q7 = Question("Яка з цих птахів не може літати?", "Страус", "Орел", "Ластівка", "Синиця")
q8 = Question("Який день святкується 8 березня?", "Жіночий день", "Різдво", "Новий рік", "День незалежності")
q9 = Question("Який основний колір утворює зелений при змішуванні?", "Жовтий і синій", "Червоний і синій", "Червоний і жовтий", "Чорний і білий")
q10 = Question("Який вид спорту грається на льоду?", "Хокей", "Теніс", "Баскетбол", "Футбол")



questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]


 
# Помістили радіо перемикачі в список
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
# перемішали список рандомно
 
 
# підставляємо питання та відповідді до радіо перемикачів
def new_question():

    global current_question
    current_question = choice(questions)
    lb_question.setText(current_question.question)
    lb_right_answer.setText(current_question.answer)

    shuffle(radio_buttons)
 
    radio_buttons[0].setText(current_question.answer)
    radio_buttons[1].setText(current_question.wrong_answer1)
    radio_buttons[2].setText(current_question.wrong_answer2)
    radio_buttons[3].setText(current_question.wrong_answer3)
 
# запускаємо функцію
new_question()
 
# Перевірка правильної відповідді
def check():
    RadioGroup.setExclusive(False)
    # проходимось по всім радіо перемикачам
    for answer in radio_buttons:
        #  перевіряємо які перемикачі обрані користувачем
        if answer.isChecked():
            # прибираємо "галочку" біля відповідді
            answer.setChecked(False)
 
            # перевіряємо текст перемикача з правильною відповіддю
            if answer.text() == lb_right_answer.text():
                current_question.got_right()
                lb_result.setText('Вірно!')
                break
 
    # Конструкція else після циклу працює лише тоді, коли цикл закінчився без переривання
    #  (тобто коли цикл не був зупинений за допомогою break).
    else:
        # якщо в циклі немає істини (true), обрана не вірна відповідь
        lb_result.setText('Не вірно!')
        current_question.got_wrong()
 
    RadioGroup.setExclusive(True)
 
# Клік на кнопку "Відповісти" або "Наступне запитання"
def click_ok():
 
    # Якщо користувач натиснув на кнопку "Відповісти"
    # викликаємо функцію check, щоб перевірити правильну відповідь
    # та приховуємо группу з питаннями
    # показуємо групу з відповіддями
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
 
        # Змінюємо текст кнопки "Відповісти" на "Наступне запитання"
        btn_next.setText('Наступне запитання')
    else:
        # Натиснута кнопка "Наступне запитання" то запитуємо нове запитання
        # приховуємо відповідді 
        # показуємо групу з питаннями
        new_question()
        gb_question.show()
        gb_answer.hide()
 
        # Змінюємо текст кнопки "Наступне запитання" на "Відповісти" 
        btn_next.setText('Відповісти')
 
# Під'єднуємо кнопку до обробника функції click_ok()
btn_next.clicked.connect(click_ok)
 
 
# показати вікно
window.show()
# запустити додаток
app.exec_()
 
