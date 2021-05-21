#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> rotate(vector<int> temp_queries)
{
    int last_value = temp_queries.back();
    temp_queries.insert(temp_queries.begin(), last_value);
    temp_queries.pop_back();
    return temp_queries;
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries) 
{
    vector<int> answer;
    vector< vector<int> > matrix(rows, vector<int>(columns,0));
    vector<int> temp_queries;
    int num = 0;
    
    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            matrix[i][j] = ++num;
        }
    }
    
    for(int i = 0; i < queries.size(); i++)
    {
        vector<int> queries_position = queries[i];
        int x1 = queries_position[0]-1;
        int y1 = queries_position[1]-1;
        int x2 = queries_position[2]-1;
        int y2 = queries_position[3]-1;
        for(int y_pos = y1; y_pos < y2; y_pos++)
        {
            temp_queries.push_back(matrix[x1][y_pos]);
        }
        for(int x_pos = x1; x_pos < x2; x_pos++)
        {
            temp_queries.push_back(matrix[x_pos][y2]);
        }
        for(int y_pos = y2; y_pos > y1; y_pos--)
        {
            temp_queries.push_back(matrix[x2][y_pos]);
        }
        for(int x_pos = x2; x_pos > x1; x_pos--)
        {
            temp_queries.push_back(matrix[x_pos][y1]);
        }
        
        temp_queries = rotate(temp_queries);
        
        int min_value = *min_element(temp_queries.begin(), temp_queries.end());
        answer.push_back(min_value);
        
        for(int y_pos = y1; y_pos < y2; y_pos++)
        {
            matrix[x1][y_pos] = temp_queries.front();
            temp_queries.erase(temp_queries.begin());
        }
        for(int x_pos = x1; x_pos < x2; x_pos++)
        {
            matrix[x_pos][y2] = temp_queries.front();
            temp_queries.erase(temp_queries.begin());
        }
        for(int y_pos = y2; y_pos > y1; y_pos--)
        {
            matrix[x2][y_pos] = temp_queries.front();
            temp_queries.erase(temp_queries.begin());
        }
        for(int x_pos = x2; x_pos > x1; x_pos--)
        {
            matrix[x_pos][y1] = temp_queries.front();
            temp_queries.erase(temp_queries.begin());
        }
    }
    
    return answer;
}