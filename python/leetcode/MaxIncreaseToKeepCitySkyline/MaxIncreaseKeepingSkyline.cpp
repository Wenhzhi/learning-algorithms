#include <iostream>
#include <vector>
#include ".\lib\json-3.9.1\single_include\nlohmann\json.hpp"

using json = nlohmann::json;
using namespace std;

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> rowMax(n);
        vector<int> colMax(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rowMax[i] = max(rowMax[i], grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans += min(rowMax[i], colMax[j]) - grid[i][j];
            }
        }
        return ans;
    }
};


int main() {
    string gridStr;
    getline(cin, gridStr);
    auto gridJson = json::parse(gridStr);
    vector<vector<int>> grid = gridJson;
    cout << Solution().maxIncreaseKeepingSkyline(grid) << endl;
}
