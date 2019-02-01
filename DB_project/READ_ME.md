# Project_03 DB

1. `01_create_table.sql` 파일 생성

   ###### [pjt.sqlite3 File 생성]

   ```sqlite
   sqlite3 pjt.sqlite3
   ```

   ###### [Table  생성]

   ```sqlite
   CREATE TABLE movies(
       "영화코드" INTEGER PRIMARY KEY,
       "영화이름" TEXT,
       "관람등급" TEXT,
       "감독" TEXT,
       "개봉연도" DATE,
       "누적관객수" INTEGER,
       "상영시간" INTEGER,
       "제작국가" TEXT,
       "장르" TEXT
   );
   ```

   ###### [header와 mode 설정]

   ```sqlite
   .mode csv
   .import boxoffice.csv movies
   .headers on
   .mode column
   ```

   ###### [출력]

   ```sqlite
   SELECT * FROM movies;
   ```

   

2. `02_crud.sql` 파일 생성

   ###### [새로운 데이터 추가]

   ```sqlite
   INSERT INTO movies VALUES (20182530,"극한직업","15세이상관람가","이병헌",20190123,313467,111,"한국","코미디");
   ```

   ###### [조건에 맞는 데이터 삭제 ]

   ```sqlite
   SELECT * FROM movies WHERE "영화코드"=20040521;
   DELETE FROM movies WHERE "영화코드"=20040521;
   ```

   `DELETE` 명렁어로 삭제  &  `WHERE`을 사용하여 어떤 조건인지 설정

   ###### [조건에 맞는 데이터 수정]

   ```sqlite
   SELECT * FROM movies WHERE "영화코드"=20185124;
   UPDATE movies SET "감독"="없음" WHERE "영화코드"=20185124;
   ```

   `UPDATE` `SET`  을 사용해 데이터를 어떻게 수정할지 알려줌

   

3. `03_select_sql` 파일 생성

   ###### [조건에 맞는 데이터 출력]

   ```sqlite
   -- 상영시간이 150분 이상인 영화이름 출력
   SELECT 영화이름 FROM movies WHERE 상영시간>=150;
   ```

   `WHERE`로 조건을 정해줌

   ```sqlite
   -- 누적관객수 백만이 넘고 관람등급이 청소년관람불가인 영화이름과 누적관객수 출력
   SELECT 영화이름,누적관객수 FROM movies WHERE 누적관객수>1000000 and 관람등급="청소년관람불가";
   ```

   `and`를 이용해 조건 2개를 만족하는 것을 출력하도록 함

   ```sqlite
   -- 장르를 중복없이 출력
   SELECT distinct 장르 FROM movies;
   ```

   `SELECT distinct`를 사용하여 중복없이 출력되도록 함

   ###### [조건에 맞는 데이터 삭제 ]

   ```sqlite
   SELECT * FROM movies WHERE "영화코드"=20040521;
   DELETE FROM movies WHERE "영화코드"=20040521;
   ```

   `DELETE` 명렁어로 삭제  &  `WHERE`을 사용하여 어떤 조건인지 설정

   ###### [조건에 맞는 데이터 수정]

   ```sqlite
   SELECT * FROM movies WHERE "영화코드"=20185124;
   UPDATE movies SET "감독"="없음" WHERE "영화코드"=20185124;
   ```

   `UPDATE` `SET`  을 사용해 데이터를 어떻게 수정할지 알려줌

   

4. `04_ expression.sql` 파일 생성

   ###### [조건에 맞는 데이터 출력]

   ```sqlite
   -- 모든 영화의 총 누적관객수를 출력하세요.
   SELECT max(누적관객수) FROM movies;
   ```

   `max`,`min`,`avg`를 이용할 수 있음

   ```sqlite
   -- 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력하세요.
   SELECT count() FROM movies WHERE 장르="애니메이션" and 상영시간>=100;
   ```

   `count`를 이용해 조건에 맞는 개수를 세어 반환함 

   

5. `05_order.sql` 파일 생성

   ###### [조건에 맞는 데이터 출력]

   ```sqlite
   -- 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개만 출력하세요.
   SELECT * FROM movies WHERE 장르="애니메이션" ORDER BY 제작국가, 누적관객수 DESC LIMIT 10; 
   ```

   `ORDER BY`은 오름차순, `ORDER BY DESC`는 내림차순으로 정렬

   `LIMIT`를 이용해 원하는 개수만큼만 출력

