class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        dq, seen, steps, furthest = deque([(True, 0)]), {(True, 0)}, 0, max(x, max(forbidden)) + a + b
        for pos in forbidden:
            seen.add((True, pos))
            seen.add((False, pos))
        while dq:
            for _ in range(len(dq)):
                dir, pos = dq.popleft()
                if pos == x:
                    return steps
                forward, backward = (True, pos + a), (False, pos - b)
                if pos + a <= furthest and forward not in seen:
                    seen.add(forward)
                    dq.append(forward)
                if dir and pos - b > 0 and backward not in seen:
                    seen.add(backward)
                    dq.append(backward)
            steps += 1
        return -1