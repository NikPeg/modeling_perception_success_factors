Выпускная квалификационная работа **"Программа для моделирования восприятия факторов успеха IТ-проекта с использованием нечетких когнитивных карт"**.

Дизайн программы в Figma: https://www.figma.com/file/PL5iRCOK6h7RpPK1ZqKQgE/modeling_perception_success_factors?type=design&node-id=0%3A1&mode=design&t=wcwHkAdhHbGRcdGC-1

# Запуск программы
1. Активируйте виртуальную среду: `source succenv/bin/activate` в Linux или `succenv\Scripts\activate` в Windows
2. Перейдите в папку django-проекта: `cd success`
3. Установите зависимости: `pip3 install -r requirements.txt`
4. Примените миграции: `python manage.py migrate`
5. Создайте суперпользователя: `python manage.py createsuperuser`
6. Запустите сервер: `python manage.py runserver`. Он будет доступен по адресу: http://127.0.0.1:8000/.

# Структура проекта
1. В основной директории проекта лежат документы в формате LaTex, а также презентации
2. В папке out находятся скомпилированные документы в формате pdf
3. В папке pictures находятся картинки, используемые в документах
4. Код программы находится в папке success. В ней находятся файл с базой данных, список требований, необходимых для работы программы, а также управляющий файл manage.py
5. Внутри папки success находится python-пакет, являющийся django-приложением (django app)
6. В нем находятся классические файлы django: 
- admin для управления админ-панелью, 
- models для описания моделей программы, 
- settings, где описаны настройки программы,
- urls со списком соответствия между url и представлениями,
- views, в котором описаны представления (views),
- wsgi для настройки и запуска веб-приложения в производственной среде
7. Фронтенд проекта находится в папках templates и static, где лежат html-документы страниц и js-скрипты для их работы.