class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for directory in path.split('/'):
            if directory in ('', '.'):
                pass
            
            elif directory == '..':
                if stack: 
                    stack.pop()
                    
            else:
                stack.append(directory)
                
        return '/' + '/'.join(stack)