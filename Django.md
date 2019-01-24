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

  