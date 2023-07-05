# Todos Application

### How to install:

```commandline
python -m venv venv
source venv/bin/activate or venv\Scripts\activate
pip install -r requirements
```

##### Run migrations:

```commandline
python manage.py migrate
```

### How to run application:
`python manage.py runserver`

##### Fill database with test data:
```commandline
python manage.py shell
>>>> from todos.fill_db import create_initial_db
>>>> create_initial_db()
```

##### Create superuser:

```python manage.py createsuperuser```

### Available commands:

- `python manage.py show_urls` -  show tab-separated list of (url_pattern, view_function, name) tuples for a project
- `python manage.py shell` - open django application console
- `python manage.py shell_plus --print-sql` - open django shell with sql explanation



# Todos

### Models
- Todo (fk на родительский todo, может быть null)
- Priority (one-to-many)
- Label (many-to-many)

### Templates (можно использовать bootstrap и тд для стилизации)

- ~~Отображение списка дел с иерархией для конкретного пользователя~~
- ~~Возможность удалять задачи (можно при помощи ajax)~~
- ~~Страница с добавлением задачи + возможность выбирать родительскую задачу~~
- ~~Возможность обновлять задачу~~
- ~~Complete задачи~~
- *Пагинация - подгрузка по 10 задач при помощи ajax
- Добавить фильтрацию по label и priority
- ~~Реализовать поиск по title~~
- Реализовать навигацию (navbar)
- Работа с пользователем:
  - форма для входа
  - форма для регистрации
  - кнопка log-out

### REST

- ~~получение задач с подзадачами~~
  - *реализовать пагинацию
  - ~~реализовать поиск по фильтрам~~
- ~~добавление задачи~~
- ~~обновление задачи~~
- ~~удаление задачи~~
  - *soft delete
- ~~получение данных о конкретной задаче~~
  - добавить флаг, чтобы можно было получить все связанные задачи

### DRF

- ~~получение задач с подзадачами~~
  - ~~реализовать пагинацию~~
  - ~~реализовать поиск по фильтрам~~
- ~~добавление задачи~~
- ~~обновление задачи~~
- ~~удаление задачи~~
- ~~получение данных о конкретной задаче~~
- реализовать эндпоинты для работы с priority
- реализовать эндпоинты для работы с label
- ~~работа с пользователем:~~
  - ~~работа с jwt~~
  - ~~регистрация пользователя~~

