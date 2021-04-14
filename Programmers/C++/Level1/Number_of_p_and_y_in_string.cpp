#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int len = s.length();
    int p = 0;
    int y = 0;
    
    for(int i = 0; i < len; i++)
    {
        if(s[i] == 'p' || s[i] == 'P') p++;
        if(s[i] == 'y' || s[i] == 'Y') y++;
    }

    return p == y;
}