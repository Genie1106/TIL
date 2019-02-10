# 04_CRUD

1. #### DataBase 생성

   ###### [models.py]

   ```python
   class Movies(models.Model):
   	title = models.CharField(max_length=100)
   	title_en = models.CharField(max_length=100)
   	audience = models.IntegerField()
   	open_data = models.DateField()
   	genre = models.TextField()
   	watch_grade = models.TextField()
   	score = models.FloatField()
   	poster_url = models.TextField()
   	description = models.TextField()
   ```

   

2. #### Page

   1. ##### Index - 영화 목록

      ###### [views.py]

      ```python
      def index(request):
          movies = Movie.objects.all()
          return render(request,"index.html",{"movies":movies})
      ```

      `movies`에 `class Movie`에 저장된 data를 불러와 사용

      ###### [index.html]

      ```html
      {% for movie in movies %}
      <li><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>: {{ movie.score }}</li>
      {% endfor %}
      ```

      `for` 문을 사용하여 위의 `movies`에서 data를 하나씩 불러와 사용

      

   2. ##### New - 새로운 영화 정보 생성 FORM

      ###### [new.html]

      ```html
      <form action="{% url 'movies:create' %}" method="post">
          {% csrf_token %}
          <p>title : <input type="text" name="title"/></p>
          <p>title_en : <input type="text" name="title_en"/></p>
          <p>audience : <input type="number" name="audience"/></p>
          <p>open_data : <input type="date" name="open_data"/></p>
          <p>genre : <input type="text" name="genre"/></p>
          <p>watch_grade : <input type="text" name="watch_grade"/></p>
          <p>score : <input type="number" step="0.01" name="score"/></p>
          <p>poster_url : <input type="text" name="poster_url"/></p>
          <p>description : <input type="textarea" name="description"/></p>
          <p><input type="submit" value=Create></p>
      </form>
      ```

      `POST` 요청 방식을 사용해 작성한 내용을 `movies:create(영화정보생성)` 로 보냄

      ex)


          <p>title : <input type="text" name="title"/></p>
          <p>title_en : <input type="text" name="title_en"/></p>
          <p>audience : <input type="number" name="audience"/></p>
          <p>open_data : <input type="date" name="open_data"/></p>
          <p>genre : <input type="text" name="genre"/></p>
          <p>watch_grade : <input type="text" name="watch_grade"/></p>
          <p>score : <input type="number" step="0.01" name="score"/></p>
          <p>poster_url : <input type="text" name="poster_url"/></p>
          <p>description : <input type="textarea" name="description"/></p>
          <p><input type="submit" value=Create></p>
      

   3. ##### Create - 새로운 영화 정보 생성

      ###### [views.py]

      ```python
      def create(request):
          title = request.POST.get("title")
          title_en = request.POST.get("title_en")
          audience = request.POST.get("audience")
          open_data = request.POST.get("open_data")
          genre = request.POST.get("genre")
          watch_grade = request.POST.get("watch_grade")
          score = request.POST.get("score")
          poster_url = request.POST.get("poster_url")
          description = request.POST.get("description")
          movie = Movie(title=title,title_en=title_en,audience=audience,open_data=open_data,genre=genre,watch_grade=watch_grade,score=score,poster_url=poster_url,description=description)
          movie.save()
          return redirect("movies:index")
      ```

      `request.POST.get()`을 통해 원하는 data를 받음

      ` movie.save()`를 통해 새로운 data를 저장

      `redirect()`로 `movies:index` 로 바로 이동

      

   4. ##### Detail - 영화 정보 상세 조회

      ###### [views.py]

      ```python
      def detail(request,movie_id):
          movie = Movie.objects.get(pk=movie_id)
          return render(request,'detail.html',{'movie':movie})
      ```

      `Movie.objects.get(pk=movie_id)`로 원하는 movie_id의 데이터를 가져옴

      `{'movie':movie}`를 통해 `detail.html`에서 movie에 movie를 넣는다고 해줌

      

   5. ##### Edit - 영화 정보 수정 FORM

      ###### [views.py]

      ​	- Detail과 동일하게 사용. (원하는 key를 받아와 수정)

      ###### [edit.html]

      ```html
      <p>title : <input type="text" name="title" value="{{movie.title}}"/></p>
      ```

      `value`를 통해 원래의 값을 불러옴

      

   6. ##### Update - 영화 정보 수정

      ###### [views.py]

      ```python
      def update(request,movie_id):
          movie=Movie.objects.get(pk=movie_id)
          movie.title = request.POST.get("title")
          movie.title_en = request.POST.get("title_en")
          movie.audience = request.POST.get("audience")
          movie.open_data = request.POST.get("open_data")
          movie.genre = request.POST.get("genre")
          movie.watch_grade = request.POST.get("watch_grade")
          movie.score = request.POST.get("score")
          movie.poster_url = request.POST.get("poster_url")
          movie.description = request.POST.get("description")
          movie.save()
          return redirect("movies:detail",movie.pk)
      ```

      `movie.title = request.POST.get("title")`로 기존의 값을 새로운 값으로 덮어씌움

      `movie.save()` 로 새로 덮힌 데이터를 저장 

      

   7. ##### Delete - 영화 삭제

      ###### [views.py]

      ```python
      def delete(request,movie_id):
          movie=Movie.objects.get(pk=movie_id)
          movie.delete()
          return render(request,"delete.html")
      ```

      `movie.delete()` 로 원하는 데이터를 삭제

   ###### 