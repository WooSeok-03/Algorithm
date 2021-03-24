#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = phone_number;
    int len = answer.length();
    
    for(int i = 0; i < len - 4; i++)
    {
        answer.replace(i, 1, "*");   
    }
    
    return answer;
}