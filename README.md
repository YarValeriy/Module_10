1. Project Overview
   Сайт з цитатами різних авторів, з можливістю додавання авторів і цитат для зареєстрованих коритувачів.
   Основа сайту створена в результаті скрапінгу http://quotes.toscrape.com.
2. Installation Instructions
   Сайт реалізовано на Django, база даних - на Postgres.
3. Usage Guide.
   Перегляд цитат і інформації про авторів не вимагає авторизації. Додавання авторів і цитат вимагає реєстрації і авторизації.
   Для запуску серверу необхідно:
   - перейти в робочий каталоg: cd hw_project
   - запустити сервер: python manage.py runserver
   - перейти на сайт за посиланням http://127.0.0.1:8000/ 
5. Configuration.
Для встановлення пакету і роботи з БД Postgres необхідно:
   - скопіювати hw_project на локальний диск
   - запустити БД postgres на локальній машині
   - в файлі hw_project/hw_project/settings.py встановити параметри підключення до БД postgresза замінивши поточні параметри:
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '567234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
   - перейти в робочий каталоg: cd hw_project
   - ініцюювати міграцію даних з MongoDB в Postgres командою:
     python utils/migration.py
   - запустити сервер: python manage.py runserver

   7. Contributing Guidelines
Код може вільно копіюватися і використатися.

8. License
Проєкт створений в межах навчального курсу школи GoIt, якій і належать права на продукт.
