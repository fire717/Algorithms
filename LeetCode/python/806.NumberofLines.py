class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 0
        line_count = 0
        l = len(S)
        #ord('a') = 97
        for i in range(l):
            this_width = widths[ord(S[i])-97]
            if line_count+this_width>100:
                lines+=1
                line_count = this_width
            else:
                line_count += this_width
        return [lines+1, line_count]
