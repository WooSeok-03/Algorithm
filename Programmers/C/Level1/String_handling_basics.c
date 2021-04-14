#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true;
    int len = strlen(s);
    
    if(!(len == 4 || len == 6))
    {
        answer = false;
        return answer;
    }
    
    for(int i = 0; i < len; i++)
    {
        if(!(s[i] >= 48 && s[i] <= 57))
        {
            answer = false;
        }
    }
    
    return answer;
}