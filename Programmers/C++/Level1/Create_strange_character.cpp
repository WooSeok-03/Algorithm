#include <string>
#include <vector>

using namespace std;

string solution(string s) 
{
    int upper_idx = 0;
    
    for(int i = 0; i < s.size(); i++)
    {   
        if(s[i] == ' ')
        {
            upper_idx = 0;
            s[i+1] = toupper(s[i+1]);
            continue;
        }
        if(upper_idx % 2 == 0)
        {
            s[i] = toupper(s[i]);
        }
        else
        {
            s[i] = tolower(s[i]);
        }
        upper_idx++;
    }
    
    
    return s;
}