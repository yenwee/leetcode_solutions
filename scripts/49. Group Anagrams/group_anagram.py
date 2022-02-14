class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in d:
                d[sorted_string] = [string]
            else:
                d[sorted_string].append(string)
                
        return (list(d.values()))