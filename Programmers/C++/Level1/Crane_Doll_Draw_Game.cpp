#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int count = 0;
    vector<int> basket;
    
    for(int i = 0; i < moves.size(); i++)
    {
        for(int j = 0; j < board.size(); j++)
        {
            if(board[j][moves[i]-1] != 0)
            {
                basket.push_back(board[j][moves[i]-1]);
                //cout << board[j][moves[i]-1] << ' ';
                board[j][moves[i]-1] = 0;
                break;
            }
        }
    }
    
    
    while(1)
    {
        if(basket[count] == basket[count+1]) 
        {
            basket.erase(basket.begin() + count, basket.begin() + count+2);
            answer += 2;
            count = -1;     // -1로 해주어야 if문 밖에 있는 count++이 된 이후, 0부터 접근이 가능하다.
        }
        count++;
        if(count == basket.size()) break;
    }
    
    return answer;
}