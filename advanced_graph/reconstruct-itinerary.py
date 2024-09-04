from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #init graph
        graph = defaultdict(list)

        #build graph
        #sorted dest so that we go to lower lexical order first
        for src, dest in sorted(tickets, reverse= True):
            graph[src].append(dest)
        itinerary = []
        @cache
        def dfs(src):
            #go to dest, must use while in here
            while graph[src]:
                dfs(graph[src].pop())
            #append src
            itinerary.append(src)
                #init itinerary
        
        dfs("JFK")
        return itinerary[::-1]
            