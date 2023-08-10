import telebot
import webbrowser
from telebot import types


bot=telebot.TeleBot('6685756745:AAHrkzK26gwRJMyxLrBtbb9rCr9_q6zSrXY')





@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Страны')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Экзамены')
    btn3 = types.KeyboardButton(' Материалы для подготовке к экзаменам ')
    btn4 = types.KeyboardButton('Сайты университетов')
    markup.row(btn2,btn3)
    markup.row(btn4)
    bot.send_message(message.chat.id,f'Привет ! {message.from_user.first_name}, Выберите страны и я вам скину файл для ознакомления!) ',reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text =='Страны':
        file = open('Mini tour universities.pdf', 'rb')
        bot.send_document(message.chat.id, file)
        bot.register_next_step_handler(message, on_sum)
def on_sum(message):
    if message.text == 'Экзамены':
        bot.send_message(message.chat.id,"IELTS — международная система оценки знания английского языка. IELTS предлагает тестирование в четырех различных областях:\nЧтение (Reading) — оценивает способность понимать и анализировать тексты на английском языке.\nПисьмо — проверяет умение создавать письменные тексты различных жанров, таких как эссе или письмо.\nПрослушивание  — тестирует способность понимать иностранную речь на слух через различные записи.\nГоворение  — оценивает устные коммуникативные навыки, включая способность выражать свои мысли и мнения на английском языке.Стоимость данного экзамена 77тысяч тенге\n\nSAT (Scholastic Assessment Test) — это стандартизированный тест, который часто используется для приема в американские колледжи и университеты. \nОн разрабатывается и администрируется организацией College Board. \nSAT предназначен для оценки способностей абитуриентов и их готовности к обучению в высших учебных заведениях.\nТест состоит из четырех основных разделов:Чтение — проверяет способность понимать тексты различных жанров и анализировать их.Письмо с эссе  — оценивает навыки написания эссе и аргументации, а также знание грамматики и стиля.\nМатематика без калькулятора  — тестирует математические навыки, которые можно выполнить без использования калькулятора.Математика с калькулятором \n — проверяет более сложные математические задачи, для которых можно использовать калькулятор.В зависимости от учебного заведения, куда претендует абитуриент, тест SAT может быть одним из факторов при принятии решения о приеме. Результаты теста SAT помогают колледжам оценить общую успеваемость и готовность абитуриента к высшему образованию. Стоимость экзамена от $120 ")
        bot.register_next_step_handler(message, on_ass)
def on_ass(message):
    if message.text=='Материалы для подготовке к экзаменам':
        file_1=open('Math rustimova.pdf','rb')


        bot.send_document(message.chat.id,file_1)
        bot.register_next_step_handler(message,on_aqq)
def on_aqq(message):
    if message.text=='Сайты университетов':
        file_7=open('LINKS OF every university.docx','rb')
        bot.send_document(message.chat.id, file_7)












@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, ' Чем могу вам помочь?')

















@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}  ')
    elif message.text.lower() =='как дела':
        bot.send_message(message.chat.id,f'У меня все хорошо,у тебя как {message.from_user.first_name} ? ')


bot.polling(none_stop=True)



