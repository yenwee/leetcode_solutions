class Solution:
    def countAndSay(self, n: int) -> str:
        return self.recursive(n, "1") if n > 1 else "1"
    
    def recursive(self, n, string):
        if n > 1:
            say = []
            count = 0
            prev = string[0]
            for index, current in enumerate(string):
                if prev == current:
                    count += 1
                    
                else:
                    say.append(str(count) + prev)
                    count = 1
                
                prev = current
                
                if (index == len(string) - 1):
                    if prev == current:
                        say.append(str(count) + prev)
                    else:
                        say.append("1" + current)

            n -= 1
            return self.recursive(n, ''.join(say))
        
        if n == 1:
            return string
        

            
            
        
        