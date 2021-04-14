#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = false;
    int len = s.length();
    
    if(len == 4 || len == 6)
    {
        for(int i = 0; i < len; i++)
        {
            if(s[i] >= '0' && s[i] <= '9')
            {
                answer = true;
            }
            else
            {
                answer = false;
                break;
            }
        }
    }
    
    return answer;
}

// isdigit함수 사용한 코드
bool solution(string s) {
    bool answer = true;
	int len = s.length();

    for (int i = 0; i < len; i++)
    {
        if (!isdigit(s[i])) answer = false;
		if (!(len == 4 || len == 6)) answer = false;
    }

    return answer;
}

// isdigit함수는 숫자를 판단하는 함수이다.
// char 타입이 10진수 숫자로 변경이 가능하면 숫자를 return / 아니면 0(false)를 반환하는 함수이다.