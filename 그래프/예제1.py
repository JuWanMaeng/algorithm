"""
섬의 개수 
1을 육지로 0을 물로 가정한 2D그리드 맵이 주여졌을때, 섬의 개수를 계산하라(1의 덩어리 개수를 구하라)

11110
11010
11000
00000 --->1

"""
class Solution:
    def numIslands(self, grid):

        def dfs(i,j):                            #중첩함수 dfs 조건
            if i<0 or i>=len(grid) or \
                j<0 or j>=len(grid[0]) or \
                grid[i][j] !='1':
                return

            grid[i][j]=0
        
            dfs(i+1,j)            #동서남북 모두 확인
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1

        return count

test=Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(test.numIslands(grid))