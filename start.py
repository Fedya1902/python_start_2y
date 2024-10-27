from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
 
app = QApplication([])

app.setStyleSheet("""
    QApplication {
        background: #f3f3f3;  /* Light gray for a Windows 11 background */
    }
    QWidget {
        background: #f3f3f3;
        color: #323232;  /* Darker gray text */
    }
    QPushButton {
        background-color: #0078D4;  /* Windows blue */
        border: none;
        border-radius: 8px;
        color: white;
        font-family: Segoe UI, sans-serif;
        font-size: 18px;
        padding: 10px 20px;
        margin: 8px 0;
    }
    QPushButton:hover {
        background-color: #005a9e;  /* Darker blue on hover */
    }
    QPushButton:pressed {
        background-color: #004578;  /* Even darker blue when pressed */
    }
    QGroupBox {
        background: #ffffff;
        border: 1px solid #e1e1e1;
        border-radius: 10px;
        padding: 10px;
        font-family: Segoe UI, sans-serif;
        font-size: 20px;
        color: #323232;
    }
    QRadioButton {
        font-family: Segoe UI, sans-serif;
        font-size: 18px;
        color: #323232;
        spacing: 5px;
    }
    QLabel {
        color: #323232;
        font-family: Segoe UI, sans-serif;
        font-size: 22px;
        margin: 5px;
    }
""")
 
from main_window import *
from menu_window import *
 
 
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
q3 = Question("Яка планета найближча до Сонця?", "Меркурій", "Венера", "Юпітер", "Марс")
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

def rest():
    window.hide()

    n = sp_rest.value() * 60
    sleep(n)

    window.show()

btn_rest.clicked.connect(rest)
    
def menu_generation():
    if current_question.count_ask == 0:
        c = 0
    else:
        c = (current_question.count_right/current_question.count_ask)*100

    text = f'Разів відповіли: {current_question.count_ask}\n' \
        f'Вірних відповідей: {current_question.count_right}\n' \
        f'Успішність: {round(c, 2)}%'

    lb_statistic.setText(text)


    menu_win.show()

    # Виставити вікно "Меню" по центру екрану ПК
    screen_geometry = app.desktop().screenGeometry()
    x = (screen_geometry.width() - menu_win.width()) // 2
    y = (screen_geometry.height() - menu_win.height()) // 2
    menu_win.move(x, y)

    window.hide()

btn_menu.clicked.connect(menu_generation)    


def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)    

























 
 
# показати вікно
window.show()
# запустити додаток
app.exec_()
 
