from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string_len = len(s1)
        d1 = Counter(s1)
        
        # Initial sliding window of length s1
        window = s2[ : string_len]
        d2 = Counter(window)
        
        if d1 == d2:
            return True
  
        for i in range(len(s2) - string_len):
        
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            
            if s2[i + string_len] in d2:
                d2[s2[i + string_len]] += 1
            else:
                d2[s2[i + string_len]] = 1
                
            if d1 == d2:
                return True
                
        return False