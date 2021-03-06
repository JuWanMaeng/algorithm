from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        graph=defaultdict(list)
        for a,b in sorted(tickets):
            graph[a].append(b)

        route=[]
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')

test=Solution()
print(test.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))