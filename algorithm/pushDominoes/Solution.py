class Solution:
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N
        
        # Populate Rs
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1,0)
            force[i] += f
        
        # Populated Ls
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f
            
        for i in range(N):
            if force[i] == 0:
                force[i] = '.'
            elif force[i] > 0:
                force[i] = 'R'
            elif force[i] < 0:
                force[i] = 'L'
        return "".join(force)
    
    
print(Solution().pushDominoes(".L.R...LR..L.."))