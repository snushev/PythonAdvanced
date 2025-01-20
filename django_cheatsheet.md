# Django Cheatsheet

## 🚀 Създаване на проект и приложение
```sh
# Инсталиране на Django
pip install django

# Създаване на нов проект
django-admin startproject myproject

# Влизане в проекта
cd myproject

# Създаване на приложение
python manage.py startapp myapp
```

---

## ⚙️ Настройки на проекта (settings.py)
```python
# Добавяне на приложението в settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",  # Добавяме нашето приложение
]

# Настройки за базата данни (по подразбиране SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

---

## 🏗️ Модели (models.py)
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### 🔄 Прилагане на миграции
```sh
# Създаване на миграция
python manage.py makemigrations

# Изпълнение на миграциите
python manage.py migrate
```

---

## 🔗 URL маршрутизация (urls.py)
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

---

## 🎭 Изгледи (views.py)
```python
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})
```

---

## 📄 Шаблони (templates/index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>Публикации</h1>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    {% endfor %}
</body>
</html>
```

---

## 📩 Форми (forms.py)
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
```

---

## 📜 Админ панел (admin.py)
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

```sh
# Създаване на суперпотребител
python manage.py createsuperuser
```

---

## 🔑 Аутентикация на потребители
```python
from django.contrib.auth import authenticate, login, logout

# Вход
user = authenticate(username="admin", password="password")
if user is not None:
    login(request, user)

# Изход
logout(request)
```

---

## 🌍 Стартиране на сървъра
```sh
python manage.py runserver
```

