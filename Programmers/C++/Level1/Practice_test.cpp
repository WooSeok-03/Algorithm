#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> scores;
    
    int first_selection = 1;
    int first_score = 0;
    
    int second_selection = 1;
    int second_score = 0;
    
    int third_score = 0;
    
    for(int i = 0; i < answers.size(); i++)
    {
        // 1번 수포자
        if(answers[i] == first_selection) first_score++;
        first_selection++;
        if(first_selection > 5) first_selection = 1;
        
        // 2번 수포자
        if(i % 2 == 0)
        {
            if(answers[i] == 2) second_score++;
        }
        else
        {
            if(answers[i] == second_selection) second_score++;
            second_selection++;
            if(second_selection == 2) second_selection++;
            if(second_selection > 5) second_selection = 1;
        }
        
        // 3번 수포자
        switch(i % 10)
        {
            case 0:
            case 1:
                if(answers[i] == 3) third_score++;
                break;
            case 2:
            case 3:
                if(answers[i] == 1) third_score++;
                break;
            case 4:
            case 5:
                if(answers[i] == 2) third_score++;
                break;
            case 6:
            case 7:
                if(answers[i] == 4) third_score++;
                break;
            case 8:
            case 9:
                if(answers[i] == 5) third_score++;
                break;
        }
    }
    scores.push_back(first_score);
    scores.push_back(second_score);
    scores.push_back(third_score);
    
    int top_rank = *max_element(scores.begin(), scores.end());
    for(int i = 0; i < scores.size(); i++)
    {
        if(top_rank == scores[i]) answer.push_back(i+1);
    }
    
    return answer;
}