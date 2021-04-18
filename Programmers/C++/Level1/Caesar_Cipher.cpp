#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] != ' ')
        {
            for(int j = 0; j < n; j++)
            {
                if(s[i] == 'z') s[i] = 96;
                if(s[i] == 'Z') s[i] = 64;
                s[i]++;
            }
            answer += s[i];
        }
        else answer += ' ';
    }
    
    return answer;
}