#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;
    int a = n;
    int count = 0;
    
    while(a != 0) 
    {
        a /= 10;
        count++;
    }
    
    for(int i = 0; i < count; i++)
    {
        answer += n % 10;
        n /= 10;
    }
    
    return answer;
}