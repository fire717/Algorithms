# 202ms-53%

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        total = 0
        e_tmp = [id]
        while e_tmp:
            total += employees[e_tmp[0]-1].importance
            e_tmp.extend(employees[e_tmp[0]-1].subordinates)
            e_tmp=e_tmp[1:]
        return total
