#include <string>
#include <vector>

using namespace std;

// sprintf()를 사용하여 char배열(answer)에 넣어주었다.
string solution(vector<string> seoul) {
    char answer[11];
    
    for(int i = 0; i < seoul.size(); i++)
    {
        if(seoul[i] == "Kim") sprintf(answer, "김서방은 %d에 있다", i);
    }
    
    return answer;
}

// to_string()을 사용하여 string변수(answer)에 넣어주었다.
/*
string solution(vector<string> seoul) {
    string answer = "";
    
    for(int i = 0; i < seoul.size(); i++)
    {
        if(seoul[i] == "Kim") answer = "김서방은 " + to_string(i) +"에 있다";
    }
    
    return answer;
}
*/
