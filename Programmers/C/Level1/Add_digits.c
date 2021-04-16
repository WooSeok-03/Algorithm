#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int count = 0;
    int num = n;
    int a = 0;
    
    while(num != 0)
    {
        num /= 10;
        count++;
    }
    
    for(int i = 0; i < count; i++)
    {
        a = n % 10;
        n /= 10;
        answer += a;
    }
    return answer;
}