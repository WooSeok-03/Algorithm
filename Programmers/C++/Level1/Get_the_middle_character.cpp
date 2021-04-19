#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int mid_idx = s.length() / 2;
    
    if(s.length() % 2 == 0)
    {
        answer += s[mid_idx-1];
        answer += s[mid_idx];
    }
    else
    {
        answer += s[mid_idx];
    }
        
    return answer;
}