* 주차 : 2주차 
* 문제명 : 전화번호 목록
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/42577
* 사용언어 : Pyton3
* 자체평점(5점 만점) : 2/5 
  
  ---

* 풀이

전화번호 A가 다른 전화번호 들의 접두어가 되면 안된다.

1. 사전순 정렬을 함. 사전순 정렬의 경우 맨앞글자가 작은 숫자인 경우 앞으로 오게됨
2. 하나라도 접두어가 있는 경우 False를 반환하기 때문에 비교는 바로 다음것과만 하면 됨