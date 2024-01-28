class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students1 = students.count(1)
        students0 = students.count(0)
        for s in sandwiches:
            if s == 1:
                if students1 > 0:
                    students1 -= 1
                else:
                    return students0
            else:
                if students0>0:
                    students0 -= 1
                else:
                    return students1
        return 0
        