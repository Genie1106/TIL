# Homework 01

1. ###### Python에서 사용할 수 없는 식별자

  False, True, None, and, as, assert, break, class, continue, def, del, elif, else, if
  except, finally, for, from, global, import, in, is, lamboda, nonlocal, not, or, pass
  raise, return, try, while, with, yield, sum, int 

2. ###### Float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않는다. 아래의 값을 비교하기 위해 작성해야하는 코드는?

  a = 0.1 * 3
  b = 0.3

  1) abs비교.
  ​	abs(a-b)<= 1e-10
  2) float epsilon 비교
  ​	abs(a-b) <= sys.float_info.epsilon
  3) math 모듈 이용
  ​	import math
  ​	math.isclose(a,b)

3. ###### 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \을 작성

  1) \n
  2) \t
  3) \\\\

4. ###### "안녕, 철수야"를 string Interpolation을 사용하여 출력

  name = " 철수 "

  ​	print(f"안녕, {name}야")

5. ###### 다음 중 형변환시 오류가 발생하는 것은?

  1. str(1)

  2. int('30')

  3. int(5)

  4. bool('50')

  5. int('3.5')

     5번.  int는 정수형이므로 3.5인 float 형태를 받을 수 없다.