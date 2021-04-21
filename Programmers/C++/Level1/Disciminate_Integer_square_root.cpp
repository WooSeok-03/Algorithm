#include <string>
#include <vector>
#include <math.h>
#include <iostream>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    
    double f_n = sqrt(n);
    long long i_n = sqrt(n);
    
    if(f_n - i_n > 0) return -1;
    
    answer = pow(i_n+1, 2);
    
    return answer;
}