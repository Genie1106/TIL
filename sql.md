# 190121

가상환경 활성화  => 가상환경 안에서만 프로그램이 설치됨. 

```python
pyenv local [가상환경 이름 "first-venv"] // 가상환경 설정
pip --version // version 확인
pip freeze // 설치된 정보를 알려줌
```



<Flask 사용 함수 외우기!>

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host=os.getenv("IP"), port=os.getenv("PORT"), debug=True) 
	// python app.py를 이용해 시작하기.
```

```python
FLASK_APP=app.py flask run --host=$IP --port=$PORT 
// C9서버의 주소를 써야하므로 IP주소를 찾아주어야 한다.
```

```python
@app.route("/greeting/<string:name>")
def greeting(name):
    return f"반갑습니다! {name}님!"
```

```python
flask에서 return 줘야 하는 값은 무조건 문자열!!
```

```python
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
// 저장된 html file 가져와서 띄우기.
```

```python
@app.route("/hi/<name>")
def hi(name):
    return render_template("hi.html",name_in_html=name)
// 인자를 넘겨줘 나타나게 함.

In hi.html file
<h1>Hi! {{name_in_html}}!</h1>  "{{}}"를 사용함.
```

```python
{% for f in fruits %} // 반복문이나 조건문을 사용할 경우, {%  %}로 사용
	<li>{{ f }}</li>  // app.py에서 만든 list를 찾아 f에 넣어준 것을 프린트 함 
{% endfor %}      	  // 이를 통해 반복이 끝났다는 것을 알려줌.
```



# 190122

1. send.html에서 값 넘겨주기

```python
<form action="/receive" method="get">  			//action : receive로 넘겨주기 위해 사용.
	<input type="text" name="name"/>
    <input type="text" name="message"/>
    <input type="submit" value="Submit"/>
</form>
```

2. app.py에서 send에서 넘어온 name과 message 받기

```python
@app.route("/receive")
def receive():
    name = request.args.get("name")				//요청받은 것은 dictionary 형태이므로 get을 
    message = request.args.get("message")		//통해 받아옴.
    return render_template("receive.html")
```



## DB(Data Base)

데이터 베이스 : 체계화된 데이터의 모임. (By. 위키피디아)

RDBMS(관계형데이터베이스관리시스템) - MySQL, SQLite, MS SQL 등

* SQLite : 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스. 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터 베이스.

기본 용어 정리

- 스키마(scheme) : 데이터베이스에서 자료이 구조, 표현방법, 관계등을 정의한 구조.

  |    column    | database |
  | :----------: | :------: |
  |   id, age    |   INT    |
  | phone, email |   TEXT   |

  column(열) : 각 열에는 고유한 데이터 형식이 지정. ex) INTEGER TEXT NULL etc...

  row(행) : 레코드. 테이블의 데이터는 행에 저장.

  PK(기본키) : 각 행의 고유값(Primary Key). 반드시 설정!!  데이터베이스 관리 및 관계 설정시 주요하게 활용.

  id 값에는 PRIMARY KEY를 무조건 주어야함!!!

### SQL

Structured Query Language. 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어.

문법 3가지

* DDL - 데이터 정의 언어(definition) : 데이터와 데이터 베이스 구조를 정의하기 위한 명령어
* DML - 데이터 조작 언어(Manipulation) : 데이터를 저장, 수정, 삭제, 조회를 위한 언어
* DCL - 데이터 제어 언어(Control) : 데이터베이스 사용자의 권한 제어를 위해 사용하는 언어



```sqlite
.mode csv 						// csv 모드로 하겠다.
.import hellodb.csv examples  	// hellodb csv를 examples 테이블에 넣겠다.
.headers on
.mode column					// 스프레드 시트처럼 나옴
.exit							// SQL 모드에서 빠져나옴
```

DB, Table  생성

```sqlite
sqlite3 tutorial.sqlite3  			// sqlite3의 확장자를 연다.
.databases			

CREATE TABLE table(					// Table 생성
	column1 datatype PRIMARY KEY,
	column2 datatype ...
)
.tables 							// 어떤 table이 있는지 확인
.schema table						// table이 어떠한 특성이나 구조를 가졌는지 확인

DROP TABLE table					// table 삭제

INSERT INTO table (coulmn1)			// 특정 table에 새로운 행을 추가해 데이터 추가
		VALUES (value1)
INSERT INTO classmates VALUES(2,"홍길동",50,"서울"); //모든 값을 추가할 때는 column 생략가능

SELECT * FROM examples; 		// select는 특정한 테이블을 반환. *은 모든 column을 불러와라.
SELECT column FROM examples LIMIT num	// 원하는 개수만큼 가져올 때 사용
SELECT column FROM examples LIMIT num OFFSET num// 원하는 개수만큼 offset한 만큼 가져옴

SELECT column FROM examples WHERE column=value				// 특정한 값만 가져옴

DELETE FROM classmates					// WHERE에 속한 값을 지우기
   ...> WHERE id=3;

UPDATE table							// data 수정(Update)
SET column1=value1
WHERE condition
```

SQLite는 동적 데이터 타입으로 기본적으로  affinity에 맞게 들어간다.

```sqlite
CREATE TABLE classmates (	
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
); .


CREATE TABLE users (
id INT PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INT NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INT NOT NULL
);
```

```sqlite
[ WHERE, expression ]
SELECT * FROM users WHERE age>=30;				// 30이상인 사람만 가져오기.
COUNT(column)									// 레코드의 갯수를 반환
SELECT COUNT(*) FROM users;						// users의 갯수를 반환
AVG(column), SUM(),MIN(),MAX()

[정렬]
ORDER BY column1,column2 [ASC/DESC]				// 정렬. ASC - 오름차순
```

```sqlite
[ LIKE ]
WHERE column LIKE

2%		|	2로 시작하는 값
%2 		|	2로 끝나는 값
%2% 	|	2가 들어가는 값
_2% 	|	아무값이나 들어가고 두번째가 2로 시작하는 값
1___ 	|	1로 시작하고 4자리인 값
2_%_% 	|	2로 시작하고 적어도 3자리인 값
```



# 190123

CRUD 

​	Create / Read /​ Update / Delete

ORD

​	Object - Relational Database (객체 관계 데이터베이스) 



[가상환경 설정]

```sqlite
pyenv virtualenv 3.6.7 orm-venv
pyenv local orm-venv

<pip upgrade>
pip install -U pip

# 명령어
flask db init
flask db migrate
flask db upgrade
```

```sqlite
from app import db, User
user = User(username="mijin", email="mijin5122@naver.com")
db.session.add(user) // user를 db에 등록
db.session.commit()

User.query.all()	// User에 등록된 모든 것을 보여줌
```

```sqlite
# [Read]
# SELECT * FROM users;
# users = User.query.all() # 복수

# SELECT * FROM users WHERE username="mijin";
# users = User.query.filter_by(username="mijin").all()

# SELECT * FROM users WHERE username="mijin" LIMIT 1;
# user = User.query.filter_by(username="mijin").first()

# SELECT * FROM users WHERE id=2 LIMIT 1;
# user = User.query.get(2)
# primary key만 get으로 가져올 수 있음.

# SELECT * FROM users LIKE "%jin%";
# users = User.query.filter(User.email.like("%jin%")).all()
```

