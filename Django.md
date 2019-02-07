# Django - 20190124

Web app을 만드는 것 = cafe를 만드는 것

Framework 와 프랜차이즈와 비슷

### Django - WHY? (Dynamic App)

```django
Model : 데이터를 관리

View: 사용자가 보는 화면

Template : 중간 관리자   or   Controller
```

![django MTVì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://4.bp.blogspot.com/-NEcYwo9PBC4/V8MrvCyN_bI/AAAAAAAAKWA/UXlkbAFd4gwgWmfWBeTFur7W9TtN39KWQCLcB/s1600/MTV.png)



## View & Template

```django
django-admin startproject intro . 
python manage.py runserver $IP:$PORT		// 서버 실행 명령어.
```

```
views -> urls -> html 순으로 정리!!
```

```python
[views]

def dinner(request):
    menu = ["족발","햄버거","치킨","초밥"]
    pick = random.choice(menu)
    return render(request,'dinner.html',{"Dinner":pick})
				// 딕셔너리 형태로 넘겨줘야 함
```

```python
[urls]

urlpatterns = [
    path("dinner/",views.dinner),
    path('index/',views.index),
    path('admin/', admin.site.urls),
]
```

#### [프로젝트 및 앱 생성]

```django
mkdir workshop									// workshop 폴더 생성 
cd workshop										// workshop 폴더로 이동
pyenv virtualenv 3.6.7 first_workshop			// 가상환경 만들기
pyenv local first_workshop						// 가상환경 설정
pip install django								// django 설치
django-admin startproject first_workshopp .		// 프로젝트 생성
python manage.py startapp pages					// 앱 생성
python manage.py runserver $IP:$PORT			// 서버 실행 명령
```

#### [Settings]

```django
ALLOWED_HOSTS = ["playground-genie13.c9users.io"] 	// IP HOST 추가

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "pages.apps.PagesConfig"						// pages 앱 설정
]
```

#### [Views]

```django
def info(request):
    return render(request, "classmate.html")
    
def student(request,name):
    return render(request,"student.html",{"name":name})	// 딕셔너리 형태로 받아와야 함.
```

#### [urls]

```django
from pages import views								// import 해오기

urlpatterns = [
    path("student/<str:name>", views.student),
    path("info/", views.info),
    path('admin/', admin.site.urls),
]
```

#### [가상환경 설정]

* 가상환경 설정

  ```django
  pyenv virtualenv 3.6.7 [가상환경 이름]
  ```

* 가상환경 삭제

  ```django
  pyenv uninstall [가상환경 이름]
  ```

* 가상환경 목록

  ```django
  pyenv versions
  ```

* 현재 폴더에 가상 환경 활성화

  ```django
  pyenv local [가상환경 이름]
  ```

* 현재 폴더에 활성화된 가상 환경 비활성화

  ```django
  .python-version 파일을 찾아 삭제
  ```

  

## [20190128]

#### [models.py]

```django
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
```

```django
python manage.py makemigrations
python manage.py migrate
python manage.py shell	// django 전용 shell

>>> from posts.models import Post
>>> post = Post(title="Hello",content="world!")
```

#### [기본 기능]

```django
# 1. Create
# post = Post(title="Hello", content="world!")
# post.save()

# 2. Read
# 2.1 All
# posts = Post.objects.all()
# 2.2 Get one
# post = Post.objectcs.get(pk=1) // django는 일반적으로 id 대신 pk를 사용
# 2.3 filter(WHERE)
# posts = Post.objects.filter(title="Hello").all()
# post = Post.objects.filter(title="Hello").first()
# 2.4 LIKE
# posts = Post.objects.filter(title__contains="He").all()
# 2.5 order_by
# posts = Post.objects.order_by('title').all() #오름차순
# posts = Post.objects.order_by('-title').all() #내림차순
# 2.6 limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.title = "hi"
# post.save()
```

```html
post 요청 사용시 사용해야함!!
1. html에 {% csrf_token %}
2. views에 return redirect(f"/posts/{post.pk}")사용하여 어디로 돌려줄 것인지 적어줌.
+) from django.shortcuts import render, redirect 내장함수가 아니므로

3. def github(request, username):
   		return redirect(f"https://github.com/{username}")
```

