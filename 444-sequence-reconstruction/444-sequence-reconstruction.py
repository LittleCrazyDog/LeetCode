class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # First, construct the dependency graph using seqs
        # try topological sorting on the dependency graph
        #   -- during each step, check whether there is only one option to select the node
        #   -- if there is more than one options, return False directly
        # after getting the topological sorted node list, check whether its length is the same with number of distinct
        # values and whether it's the same with seg
        
        values = { x for seq in sequences for x in seq }
        graph = { x: [] for x in values }
        indegrees = { x: 0 for x in values }
        
        for seq in sequences:
            for i in range(len(seq) - 1):
                s = seq[i]
                t = seq[i+1]
                graph[s].append(t)
                indegrees[t] += 1
        
        queue = deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)
        res = []
        
        while queue:
            if len(queue) != 1:
                return False
            source = queue.popleft()
            res.append(source)
            for target in graph[source]:
                indegrees[target] -= 1
                if indegrees[target] == 0:
                    queue.append(target)
        
        return len(res) == len(values) and res == nums