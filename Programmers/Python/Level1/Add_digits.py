def solution(n):  
    return sum(map(int, str(n)))
    
# sum()은 iterable한 자료형을 받는다. ( 리스트 & 튜플처럼 인덱스 순환 접근이 가능한 자료형 )
# sum()은 iterable의 합을 구하는 함수이다.
# map()은 리스트의 요소를 지정된 함수로 처리해주는 함수이다.
# map()의 첫번째 파라미터에 int를 넣어주고, 두번째 파라미터에 리스트를 넣어주면 리스트의 모든 요소를 int로 변환한다.