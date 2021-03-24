#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int result = 0;
    int n = x;
    int a;
    
    while(n != 0)
    {
        a = n%10;
        n = n/10;
        result += a; 
    }
    
    if(x % result == 0) answer = true;
    else answer = false;
    
    return answer;
}