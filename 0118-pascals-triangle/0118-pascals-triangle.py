class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(2,numRows+1):
            temp = [0]+ans[-1]+[0]
            row = []
            for j in range(i):
                row.append(temp[j]+temp[j+1])
            ans.append(row)
        return ans
        