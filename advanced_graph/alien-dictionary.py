class Solution(object):
    def alienOrder(self, words):
        # Find ancestors of each node by DFS.
        n = len(words)
        adj = {c: set() for w in words for c in w}

        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            #check invalid order
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(c):
            #condition to detect cicle
            if c in visited:
                return visited[c]
            #makr node have been in the path
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
            #mark as not visited for other paths to be explore
            visited[c] = False
            res.append(c) #because of dfs add leaf node first

        for c in adj:
            if dfs(c):
                return ""
        #reverse to get correct order
        return "".join(res[::-1])
                

 
 
