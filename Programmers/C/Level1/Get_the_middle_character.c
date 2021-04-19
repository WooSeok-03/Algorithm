#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요
    int mid_idx = strlen(s) / 2;
    
    if(strlen(s) % 2 != 0)
    {
        char* answer = (char*)malloc(sizeof(char));
        answer[0] = s[mid_idx];
        answer[1] = '\0';       // 문자열 마지막에 NULL(\0)을 꼭 넣어주어야 한다.
        return answer;
    }
    else
    {
        char* answer = (char*)malloc(sizeof(char)*2);
        answer[0] = s[mid_idx-1];
        answer[1] = s[mid_idx];
        answer[2] = '\0';       // 문자열 마지막에 NULL(\0)을 꼭 넣어주어야 한다.
        return answer;
    }
}