#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int lowest_rank(vector<int>lottos, vector<int>win_nums)
{
    int count = 0;
    
    for(int i = 0; i < win_nums.size(); i++)
    {
        for(int j = 0; j < lottos.size(); j++)
        {
            if(lottos[j] == win_nums[i])
            {
                count++;
                lottos.erase(lottos.begin()+j);
            }
        }
    }
    return count;
}

int top_ranking(vector<int> lottos, vector<int> win_nums)
{
    int count = lowest_rank(lottos, win_nums);
    for(int i = 0; i < lottos.size(); i++)
    {
        if(lottos[i] == 0)
        {
            count++;
        }
    }
    return count;
}

int ranking(int count)
{
    if(count == 6) return 1;
    else if(count == 5) return 2;
    else if(count == 4) return 3;
    else if(count == 3) return 4;
    else if(count == 2) return 5;
    else return 6;
}

vector<int> solution(vector<int> lottos, vector<int> win_nums) 
{
    vector<int> answer;
    
    int lowest_count = lowest_rank(lottos, win_nums);
    int top_count = top_ranking(lottos, win_nums);
    
    int top_rank = ranking(top_count);
    int lowest_rank = ranking(lowest_count);
    
    answer.push_back(top_rank);
    answer.push_back(lowest_rank);
    return answer;
}