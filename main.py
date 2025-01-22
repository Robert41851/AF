from dotenv import load_dotenv
import os
import smtplib
load_dotenv()
my_name = "Роберт"
site_name = "https://dvmn.org/profession-ref-program/rna703535/bXWhk/"
friend_name = "Саша"
send = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace("%website%",site_name).replace("%friend_name%",friend_name).replace("%my_name%",my_name)
mail_from = "robertus.nazaroff@yandex.ru"
mail_to = "robertus.nazaroff@yandex.ru"
letter = f"""\
From: {mail_from}
To: {mail_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{send}
"""
letter = letter.encode("UTF-8")
print(letter)
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
server = smtplib.SMTP_SSL('smtp.yandex.ru',465)
server.login(login, password)
server.sendmail(mail_from, mail_to, letter)
server.quit()
