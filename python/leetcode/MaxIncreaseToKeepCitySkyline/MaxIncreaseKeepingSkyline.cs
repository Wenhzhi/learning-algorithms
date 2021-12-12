using System;
using Newtonsoft.Json;

namespace ConsoleAppDemoOne
{
    public class Solution {
        public int MaxIncreaseKeepingSkyline(int[][] grid) {
            int n = grid.Length;
            int[] rowMax = new int[n];
            int[] colMax = new int[n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    rowMax[i] = Math.Max(rowMax[i], grid[i][j]);
                    colMax[j] = Math.Max(colMax[j], grid[i][j]);
                }
            }
            int ans = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    ans += Math.Min(rowMax[i], colMax[j]) - grid[i][j];
                }
            }
            return ans;
        }
        
        public static void Main(string[] args)
        {
            var gridInput = Console.ReadLine();
            var grid = JsonConvert.DeserializeObject<int[][]>(gridInput ?? String.Empty);
            Console.WriteLine(new Solution().MaxIncreaseKeepingSkyline(grid));
        }
        
    }
}
