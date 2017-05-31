class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        Aindex = {u: i for i, u in enumerate(list1)}
        best, ans = 1e9, []
        #先把A遍历一遍存为字典，然后只遍历B求和即可。
        for j, v in enumerate(list2):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans
