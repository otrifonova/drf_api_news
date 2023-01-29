Этот проект - тестовое задание, реализация REST backend новостного приложения с использованием DRF (Django REST Framework).<br>
Проект завернут в Docker.

<h3>Структура проекта:</h3>

        .
        ├──api_news
        │   ├── migrations
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── serializers.py
        │   ├── tests.py
        │   ├── urls.py
        │   └── views.py
        ├── proj
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        ├── db.sqlite3
        ├── docker-compose.yml
        ├── Dockerfile
        ├── manage.py
        └── requirements.txt

Структура соответствует стандартной, автоматически создаваемой, структуре Django-проекта.
В приложении app_news дополнительно созданы модули serializers.py - сериализаторы моделей, urls.py - маршруты приложения api_news.<br>
В базу данных db.sqlite3 уже загружены тестовые данные с текстом-рыбой.<br>
Файлы docker-compose.yml и Dockerfile предназначены для запуска приложения из Docker-контейнера.

<h3>Запуск приложения:</h3>
<ol type="1">
<li>Клонировать репозиторий</li>
</ol>
<p><b>Для запуска из IDE:</b></p>
<ol type="1">
<li value="2">Установить виртуальную среду и библиотеки (pip install -r requirements.txt)</li>
<li>Из директории проекта запустить локальный сервер командой:

    python manage.py runserver 
</li>
</ol>
<p><b>Для запуска через Docker Compose:</b></p>
<ol type="1">
<li value="2">Из директории проекта запустить docker-контейнер командой:

    docker compose up
</li>
</ol>
<p>Приложение будет доступно из браузера на локальном сервере http://localhost:8000/.</p>

<h3>База данных</h3>
В качестве базы данных использована SQLite. В базе данных содержатся следующие таблицы:
<ul type="disc">
<li>News - новости (поля: id (pk), name, summary, text, type (fk Type)</li>
<li>Type - типы новостей (поля: id (pk), name, color)
</ul>

<h3>Функционал:</h3>
<ul type="disk">
 <li> 
  <b>CRUD (Create, Read, Update, Delete) типов новостей</b> посредством POST, GET, PUT, PATCH и DELETE-запросов:<br>
 Маршрут для POST-запросов: <br>

    http://localhost:8000/api/types/

 Маршрут для GET, PUT, PATCH и DELETE-запросов:
 
    http://localhost:8000/api/types/<int:id>/

 POST, PUT и PATCH запросы требуют передачи JSON-формата с ключами - именами полей таблицы:
 
    {
    "name": "",
    "summary": "",
    "text": "",
    "type": ""
    }
 </li>
 <li>
  <b>CRUD новостей</b> посредством POST, GET, PUT, PATCH и DELETE-запросов.
  Маршрут для POST-запросов: <br>

    http://localhost:8000/api/news/

  Маршрут для GET, PUT, PATCH и DELETE-запросов:
 
    http://localhost:8000/api/news/<int:id>/

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
