# LCM of N
* 주차 : 4주차
* 문제명 : N개의 최소공배수
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12953
* 사용언어 : Python
* 자체평점(5점 만점) : 2/5
 
  —

* 풀이
LCM을 구하는 공식과, 두 수를 어떻게 비교할 것인지 설계할 수 있다면 쉽게 풀 수 있다.
LCM을 구하는 공식은 총 3가지가 있다.
1. 두 수의 배수로 각각 집합을 만들고, 교집합 중 가장 작은 원소를 찾는 방법
2. 서로소 a’, b’, 최대공약수를 모두 곱해서 찾는 공약수로 나누는 방법
3. 소인수분해를 하고, 지수를 활용하는 방법

해당 소스는 2번째인 공약수로 나눠서 찾았다.
Lcm 이라는 함수를 새로 만들어 두 정수를 입력받아 2부터 입력받은 정수중 작은 수까지 공약수만 찾아서 나누고 해당 값 만큼 공약수를 곱해주면 최소공배수를 구하게 된다. 해당 i 값으로 게속 나눌 수 있으므로 while & continue로 반복해준다.
가장 처음 입력받은 리스트(배열) 값의 맨 앞자리[0]부터 끝자리까지 1씩 더해가며 참조했던 뒤의 자리에 최고공배수를 반환해서 저장하고 비교하면 자연스럽게 모든 숫자의 최소공배수를 찾게된다.