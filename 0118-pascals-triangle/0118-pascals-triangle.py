class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lis = []
        if numRows == 0 :
            return lis
        lis.append([1])
        for i in range(2,numRows+1):
            temp = [0]+lis[-1]+[0]
            row = []
            for j in range(i):
                row.append(temp[j]+temp[j+1])
            lis.append(row)
        return lis
            