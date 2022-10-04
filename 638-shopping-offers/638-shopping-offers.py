class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}
        def check(need):
            if tuple(need) not in memo:
                res = sum(p * n for p, n in zip(price, need))
                for offer in special:
                    new_need = [a - b for a, b in zip(need, offer)]
                    if min(new_need) >= 0:
                        res = min(res, offer[-1] + check(new_need))
                memo[tuple(need)] = res
            return memo[tuple(need)]
        return check(needs)