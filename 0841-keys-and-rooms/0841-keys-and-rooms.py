class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        to_visit = [0]
        
        while to_visit:
            room = to_visit.pop()
            if room in visited: continue
            visited.add(room)
            to_visit.extend(rooms[room])
        
        return len(visited) == len(rooms)