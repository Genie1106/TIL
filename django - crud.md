# Workshop 19

[환경설정]

```django
pyenv virtualenv 3.6.7 ad_19
pyenv local ad_19
pip install django
django-admin startproject d19 .
python manage.py startapp students

settings 설정 (프로젝트와 앱 설정)

python manage.py migrations
python manage.py migrate
```

```python
[urls.py]
from django,urls import include

```

```python
[urls.py]
from django.urls import path
from . import views

urlpattenrs = [
    path("new/",views.new),
    path("",views.index),
    path("create/",views.create),
    path("<int:student_id>/",views.detail),
    path("<int:student_id>/delete",views.delete),
    path("<int:student_id>/edit",views.edit),
    path("<int:student_id>/update",views.update),
]
```

```python
[views.py]
from django.shortcuts import render,redirect
from .modles import Student

def index(request):
    students = Student.objects.all()
    return render(request,"index,html",{"students":students})

def new(request):
    return render(request, "new.html")

def create(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    birthday=request.POST.get('birthday')
    age=request.POST.get('age')
    
    s=Student(name=name,email=email,birthday=birthday,age=age)
    s.save()
    return redirect(f"/students/{s.pk}")

def detail(request,student_id):
    s= Student.objects.get(pk=student_id)
    return render(request,"detail.html",{"student":s})

def delete(request.student_id):
    s= Student.objects.get(pk=student_id)
    s.delete()
    return redirect('/studnets/')

def edit(request,student_id):
    s=Student.objects.get(pk=student_id)
    return render(request,'edit.html',{'student':s}) 

def update(request,student_id):
    s=Student.objects.get(pk=student_id)
    s.name=request.POST.get("name")
    s.email=request.POST.get("email")
    s.birthday=request.POST.get("birthday")
    s.age=request.POST.get("age")
    s.save()
    return redirect(f"/students/{s.pk}")
    
```



# 190130

[]

```python
[urls.py]

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # path("github/<str:username>/",views.github),
    # path("naver/<str:q>/",views.naver),
    path("",views.index, name="list"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:post_id>/",views.detail, name="detail"),
    path("<int:post_id>/delete/",views.delete, name="delete"),
    path("<int:post_id>/edit/",views.edit, name="edit"),
    path("<int:post_id>/update/",views.update, name="update"),
]
```

```python
[views.py]

def delete(request,post_id):
    # 삭제하는 코드
    post=Post.objects.get(pk=post_id)
    post.delete()
    return redirect("posts:list")

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    # DB
    post = Post(title=title,content=content)
    post.save()
    return redirect("posts:detail", post.pk)			// 동적으로 요구할 때
```

```html
[index.html]
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Index</h1>
    <a href="{% url 'posts:new' %}">New</a>
    <ul>
    {% for post in posts %}
  		<li><a href="{% url 'posts:detail' post.pk %}">{{ post.title }}</a></li>
    {% endfor %}
    {% endfor %}
    </ul>
</body>
</html>
```

[댓글 추가하기]

```python
[models.py]

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	content = models.TextField()
```

```shell
python manage.py shell
from posts.models import Post,Comment
Post.objects.all()
 c = Comment(post=post, content='도깨비정주행'		
 c.save()
 post.comment_set.all() 	//모든 comment(table이름) 들을 가져오는 명령어
  post.comment_set.first() 	//모든 comment(table이름) 중 첫번째를 가져오는 명령어
```

[CSS 적용]

```html
[index.html]
{% load static %}
```

