"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def helper(id):
            res = dic[id]
            for sub_id in sub[id]:
                res += helper(sub_id)
            return res
        
        dic = {}
        sub = {}
        for employee in employees:
            dic[employee.id] = employee.importance
            sub[employee.id] = employee.subordinates
        
        return helper(id)