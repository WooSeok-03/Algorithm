#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    return atoi(s); // atoi함수는 문자열을 정수로 바꾸어주는 함수이다.
}

// atoi함수 예시
// "1234" -> 1234