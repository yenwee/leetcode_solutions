class Solution(object):
    def threeSum(self, nums):
        ans = []
        neg = dict()
        pos = dict()
        zeros = 0
        
        for x in nums:
            if x > 0:
                pos[x] = pos.get(x,0)+1
            elif x < 0:
                neg[x] = neg.get(x,0)+1
            else:
                zeros += 1
        
        #case1: (0,0,0)
        if zeros >= 3:
            ans.append([0,0,0])
        
        for x in neg:
            #case2: (n,0,p)
            if zeros > 0 and -x in pos:
                ans.append([x,0,-x])
            #case 3: (n,n,p)
            if neg[x] >= 2 and -(x+x) in pos:
                ans.append([x,x,-(x+x)])
            #case 4: (n1,n2,p)
            for y in neg:
                if x < y and -(x+y) in pos:
                    ans.append([x,y,-(x+y)])

        for x in pos:
            #case5:(n,p,p)
            if pos[x] >= 2 and -(x+x) in neg:
                ans.append([-(x+x),x,x])
            #case6:(n,p1,p2)
            for y in pos:
                if x < y and -(x+y) in neg:
                    ans.append([-(x+y),x,y])                      
        return ans