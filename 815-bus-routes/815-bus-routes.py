class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        to_routes = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                to_routes[stop].add(bus)
        
        queue = [(S, 0)]
        seen = set([S])
        
        for curr, dist in queue:
            if curr == T: return dist
            for bus in to_routes[curr]:
                for next in routes[bus]:
                    if next not in seen:
                        queue.append((next, dist + 1))
                        seen.add(next)
                routes[bus] = []
        
        return -1