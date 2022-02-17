class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.next_candidate(sorted(candidates), target, 0 , [] , ans)
        return ans
        
    def next_candidate(self,candidates, current, index, stack, ans): 
        if current == 0:
            ans.append(stack)
            return
        
        for i in range(len(candidates)):
            if candidates[i] > current :
                break
                
            self.next_candidate(candidates[i:], current - candidates[i], i ,stack + [candidates[i]], ans)

