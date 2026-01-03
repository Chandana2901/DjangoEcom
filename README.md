## Django ecommerce 

### 1. to create the project
```python manage.py startproject <project_name> .```

### 2. to start the project
```python manage.py runserver```

### 3. to create migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 4. to install tailwind
#### a. install django-tailwind
```pip install django-tailwind```
#### b. Add to INSTALLED_APPS in settings.py
```INSTALLED_APPS += ['tailwind']```
#### c. create tailwind app
```python manage.py tailwind init```
#### d. add generated app to INSTALLED_APPS in settings.py and create another variable
```
INSTALLED_APPS += ['theme']
TAILWIND_APP_NAME = 'theme'
```
#### e. install tailwind css
```python manage.py tailwind install```
#### f. start dev
```python manage.py tailwind start```
