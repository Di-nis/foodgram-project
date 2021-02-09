# Foodgram

## Описание
Foodgram - сервис для хранения рецептов

## Развертывание
* IP-адрес сервера:
    - 130.193.43.93
* Вход в контейнер web:
    - docker exec -it <CONTAINER ID> bash, где <CONTAINER ID> - id контейнера web;
* Выполнение миграций:
    - python manage.py migrate
* Создание суперпользователя:
    - python manage.py createsuperuser;
* Заполнение базы данных начальными данными:
    - python3 manage.py shell;
    - from django.contrib.contenttypes.models import ContentType;
    - ContentType.objects.all().delete()
    - quit()
    - python manage.py loaddata fixtures.json
* Сбор статических файлов:
    - python manage.py collectstatic

## Workflow-статус
![Foodgram_workflow](https://github.com/Di-nis/foodgram-project/workflows/Foodgram_workflow/badge.svg)


## Создано с помощью
* [Python](https://www.python.org/)
* [Django](https://docs.djangoproject.com/en/3.1/) - Python веб фреймворк
* [Django REST framework](https://www.django-rest-framework.org/) - 
Библиотека для создания REST-сервисов на основе Django
* [JavaScript](https://www.javascript.com/)

## Авторы, контактная информация
* **Денис Смирнов** - *разработчик* - (https://github.com/Di-nis)
Электронная почта - di-nis@yandex.ru

## Благодарности
Спасибо всей команде Яндекс.Практикум за терпение, помощь и трепетное отношение в реализации этого учебного задания.
