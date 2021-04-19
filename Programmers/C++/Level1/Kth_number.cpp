#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> temp;
    int idx = 0;
    
    for(int i = 0; i < commands.size(); i++)
    {
        for(int j = commands[i][0]-1; j < commands[i][1]; j++)
        {
            temp.push_back(array[j]);
            idx++;
        }
        sort(temp.begin(), temp.end());
        answer.push_back(temp[commands[i][2] - 1]);
        temp.erase(temp.begin(), temp.end());
    }
    
    return answer;
}