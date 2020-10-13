class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        zig zag means going all the way down and coming all the way up
        A       G
        |     / |
        B    F  H
        |   /   |
        C  E    i
        | /
        D
        
        1. add a letter in each row as we go down 
		2. and once we reach the 
		3. add a letter in each row as we go up
        4. and once reaching top repeat 1,2,3 until end of string
        '''
        matrix = [[] for _ in range(numRows)]
        
        i, k = 0, 0
        while k < len(s):
            while i < numRows and k < len(s):
                matrix[i].append(s[k])
                k += 1
                i += 1
            
            i -= 2
            
            while i > 0 and k < len(s):
                matrix[i].append(s[k])
                k += 1
                i -= 1
        
        answer = ''.join([''.join(row) for row in matrix])
        return answer
