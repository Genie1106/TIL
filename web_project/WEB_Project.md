# WEB_Project

1. #### 영화 추천 사이트를 위한 레이아웃 구성

   ###### [Navigation Bar]

   ​	 -Bootstrp의 Navbar 가져와서 사용.

   * 상단에 고정하기 위해 sticky-top을 class에 추가

   ```html
   <nav class="navbar navbar-expand-lg navbar-light navbar sticky-top " style="background-color:#330066">
   ```

   ###### [Header]

   * Text를 가운데 정렬 명령어 class에 추가

   ```html
   <header class="d-flex align-items-center justify-content-center">
   	<h2 class="font text-white">당신에게 어울리는 영화를<br>추천해드립니다</h2>
   </header>
   ```

   * CSS를 이용해 header의 배경을 사진으로 지정

   ```css
   header{
       height: 350px;
       background-image:url(Background-Narrow.jpg);
       background-size:cover;							// 너비가 화면만큼 되도록
       background-position: center 480px;				// 화면에 나오는 사진의 위치를 지정
   }
   ```

   ###### [Footer]

   * a태그를 사용하여 누르면 원하는 위치로 이동

   ```html
   <footer class="d-flex align-items-center justify-content-between px-3 
                  sticky-bottom">							// sticky 함수로 밑에 고정
   	<a class="font2 text-white">Genie</a>
       <a href="#body" class="top">						// id가 body인 곳으로 이동
               <i class="fas fa-arrow-circle-up arrow fa-2x"></i>
       </a>
   </footer>
   ```

   ###### [Font]

   * CSS에서 Font를 지정하여 사용

   ```html
   <link href="https://fonts.googleapis.com/css?family=Nanum+Pen+Script" rel="stylesheet">
   // html에 링크를 추가하여 사용
   ```

   ```css
   .font {
       font-size: 60px;
       font-weight: 300; /* bold */
       font-family: 'Nanum Pen Script', cursive;
       line-height: 2;
       letter-spacing: 4px;
       text-align: center;
   }
   ```

   

2. #### 영화 추천 사이트를 위한 영화 리스트 구성

   ###### [Subtitle]

   ```html
   <h3 class="font my-3 d-flex justify-content-center">Movie List</h3>
   <hr class="underline">						// css를 사용해 underline을 가져와 사용
   ```

   ```css
   .underline {
       border-color: #330066;
       width: 70px;							// 70px의 굵기로 밑줄 만들기
       border-width: 3px;
   }
   ```

   ###### [Card view]

   ```html
   <div class="container mt-5">
       <div class="row">
           <div class="col-12 col-sm-6 col-md-4 col-lg-3">
               <div class="card my-1">
                   <img src="movie_poster/내안의 그놈.jpg" class="card-img-top" alt="...">
                   <div class="card-body align-items-center">
                       <h4 class="card-title">내안의 그놈 <button type="button" class="btn btn-secondary font-weight-bold">8.69</button></h4>
                           <hr>
                           <p class="card-text">판타지<br>개봉일: 2019.01.09</p>
                           <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=164172" target="_blank" class="btn btn-success d-flex justify-content-center ">Watch Movie</a>
                   </div>
               </div>
           </div>
       </div>
   </div>
   ```

   

3. #### 영화 상세보기

   ###### [Modal]

```html
<div class="modal fade" id="movie-5" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">아쿠아맨, AQUAMAN</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <img src="movie_poster/side_아쿠아맨.jpg" alt="..." height="300">
            <div class="modal-body">
                <p>12세이상관람가</p>
                <p>누적 관객수: 5,019,236</p>
                <hr>
                <p class="tell">땅의 아들이자 바다의 왕, 심해의 수호자인 슈퍼히어로 아쿠아맨의 탄생을 그린 액션 블록버스터</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
```

