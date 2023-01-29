Этот проект - тестовое задание, реализация REST backend новостного приложения с использованием DRF (Django Rest Framework).<br>
Проект завернут в Docker.

###Структура проекта:

        ├── proj<br>
        │   ├──api_news<br>
        │   │   ├── migrations<br>
        │   │   ├── __init__.py<br>
        │   │   ├── admin.py<br>
        │   │   ├── apps.py<br>
        │   │   ├── models.py<br>
        │   │   ├── serializers.py<br>
        │   │   ├── tests.py<br>
        │   │   ├── urls.py<br>
        │   │   └── views.py<br>
        │   ├── proj<br>
        │   │   ├── __init__.py<br>
        │   │   ├── asgi.py<br>
        │   │   ├── settings.py<br>
        │   │   ├── urls.py<br>
        │   │   ├── wsgi.py<br>
        │   ├── db.sqlite3<br>
        │   ├── docker-compose.yml<br>
        │   ├── Dockerfile<br>
        │   ├── manage.py<br>
        │   └── requirements.txt<br>

Структура соответствует стандартной, автоматически создаваемой, структуре Django-проекта.
В приложении app_news дополнительно созданы модули serializers.py - сериализаторы моделей, urls.py - маршруты приложения api_news.<br>
В базе данных db.sqlite3 уже загружены тестовые данные с текстом-рыбой.<br>
Файлы docker-compose.yml и Dockerfile предназначены для запуска приложения из Docker-контейнера.

###Запуск приложения:
<ol type="1">
<li>Клонировать репозиторий</li>
<p><b>Для запуска из IDE:</b></p>
<li>Установить виртуальную среду и библиотеки (pip install -r requirements.txt)</li>
<li>Из директории проекта /proj запустить локальный сервер командой:

    python manage.py runserver 
</li>
<p><b>Для запуска через Docker Compose:</b></p>
<li value="2">Из директории проекта /proj запустить docker-контейнер командой:

    docker compose up
</li>
</ol>
Приложение будет доступно из браузера на локальном сервере http://localhost:8000/.

###База данных
В качестве базы данных использована SQLite. В базе данных содержатся следующие таблицы:
<ul type="disc">
<li>News - новости (поля: id (pk), name, summary, text, type_id (fk Type)</li>
<li>Type - типы новостей (поля: id (pk), name, color)
</ul>

###Функционал:
<ul type="disk">
 <li> 
  <b>CRUD (Create, Read, Update, Delete) типов новостей</b> посредством POST, GET, PUT, PATCH и DELETE-запросов:<br>
 Маршрут для POST-запросов: <br>

    http://localhost:8000/api/types/

 Маршрут для GET, PUT, PATCH и DELETE-запросов:
 
    http://localhost:8000/api/types/<int:type_id>/

 POST, PUT и PATCH запросы требуют передачи JSON-формата с ключами - именами полей таблицы:
 
    {
    "name": "",
    "summary": "",
    "text": "",
    "type_id": ""
    }
 </li>
 <li>
  <b>CRUD новостей</b> посредством POST, GET, PUT, PATCH и DELETE-запросов.
  Маршрут для POST-запросов: <br>

    http://localhost:8000/api/news/

  Маршрут для GET, PUT, PATCH и DELETE-запросов:
 
    http://localhost:8000/api/news/<int:type_id>/

  POST, PUT и PATCH запросы требуют передачи JSON-формата с ключами - именами полей таблицы:
 
    {
    "name": "",
    "color": ""
    }
 </li>
 <li>
 <b>Возможность получить список всех типов новостей:</b>

    GET http://localhost:8000/api/types/
 </li>
 <li>
  <b>Возможность получить список всех новостей</b> (имя, краткое описание, имя типа, цвет типа):

    GET http://localhost:8000/api/news/
 </li>
 <li>
 <b>Возможность получить список новостей определенного типа:</b>

    GET http://localhost:8000/api/news/?type_id=<int:type_id>/

 </li>
</ul>
