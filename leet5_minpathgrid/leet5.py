class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length_horizontal=len(grid[0])
        length_vertical=len(grid)
        for i in range(length_vertical):
        	for j in range(length_horizontal):
        		if i==0 and j!=0:
        			grid[i][j]=grid[i][j]+grid[i][j-1]#只能从左面过来
        		elif i!=0 and j==0:
        			grid[i][j]=grid[i][j]+grid[i-1][j]#只能从上面过来
        		elif i!=0 and j!=0:
        			grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]#只能从上面或左面过来
        return grid[length_vertical-1][length_horizontal-1]
