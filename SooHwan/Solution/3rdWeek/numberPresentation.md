* 주차 : 3주차 
* 문제명 : 숫자의 표현
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12924
* 사용언어 : Pyton3,C++ 
* 자체평점(5점 만점) : 2/5 
  
  ---

* 풀이

1부터 n까지의 합을 Sn이라고 하면, 모든 자연수의 연속적인 합은 Sb-Sa(b>a)로 나타낼 수 있다. 또한 Sn = n(n+1)/2이므로, 나타내고자 하는 자연수를 T라고 하면, 아 문재는 2T = (b+1)b - (a+1)a(b>a>=0)를 만족하는 a,b의 쌍을 찾는 문제로 바뀌게 된다.

위 조건을 검사하기 위한 연산이 n(n+1)/2회 일어나므로, 시간 복잡도는 O(n^2)이다.