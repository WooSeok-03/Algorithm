#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int total_budget = 0;
    int count = 0;
    
    sort(d.begin(), d.end()); 
    for(int i = 0; i < d.size(); i++)
    {
        total_budget += d[i];
        if(total_budget > budget) break;
        count++;
    }
    return count;
}