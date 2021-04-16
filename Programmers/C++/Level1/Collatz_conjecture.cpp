#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int count = 0;
    
    while(num != 1)
    {
        count++;
        if(num % 2 == 0) 
        {
            num /= 2;
        }
        else
        {
            num *= 3;
            num += 1;
        }
        if(count > 500 || num < 1)
        {
            return -1;
        }
    }
    
    return count;
}