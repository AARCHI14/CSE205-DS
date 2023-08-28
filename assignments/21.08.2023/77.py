class Solution(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def combination(i,path):
            if len(path)==k:
                res.append(path.copy())
                return 
            for i in range(i,n+1):
                path.append(i)
                combination(i+1,path)
                path.pop()
                
        combination(1,[])
        return res
            

           