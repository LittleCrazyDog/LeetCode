class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Process all transactions to arrive at each person's final balance
        balances = {}
        for A, B, amount in transactions:
            balances.setdefault(A, 0)
            balances.setdefault(B, 0)
            balances[A] -= amount
            balances[B] += amount
        
        # Eliminate people who end up with 0 balance (i.e. they're
        # already happy so don't have to be part of the problem)
        balances = { P: amount for P, amount in balances.items() if amount != 0 }
        
        # If there's nothing left then people are already happy, and no transactions
        # are needed to make everybody happy.
        if not balances: return 0
        
        # Explore partitions of 0-sum subgroups, keeping track of biggest number
        # of the subgroups we see as we explore. We will do this recursively but also
        # use a persistent stack.
        
        # This is a mutable variable we will update as we explore partitions.
        to_update = {'max_num_subgroups': 1}
        
        # This is the persistent stack we will use. Each recursive call will operate
        # on remaining_balances, which will be the last item of the stack, to search
        # for subgroups. Every time we find a subgroup, we will break it out of the
        # remaining_balances and put it onto the stack in front of remaining_balances
        #
        # As we traverse down the recursive calls, the break off of subgroups mean the
        # stack will end up looking like:
        #
        # [subgroup1, subgroup2, subgroup3, remaining_balances]
        #
        # Every time we finish search through everything from a particular remaining_balances
        # and below, we will merge it with the previous subgroup as we get back up the recursion stack
        #
        # The purpose of this stack is to avoid having to copy the remaining_balances across recursive
        # calls in order to both mutate it for the next call, and to keep its state for subsequent
        # searches of the current call. Without it, we would either need to have a similar stack but pass
        # it through recursive calls as call args, or to perform copy-and-delete to recurse on a new
        # remaining_balances without mutating the existing one, which is more expensive. This stack
        # brings space usage from O(n^2) to O(n)
        #
        # Note that, despite the use of a stack, recursion is still better for this problem than a purely
        # iterative approach, because we are making multiple recursive calls over a for loop at each
        # level, so recursion lets us keep track of our place in that for loop for free.
        subgroups = [balances]
        
        def explore_subgroups():
            # pop off the remaining balances
            remaining_balances = subgroups.pop()
            
            if remaining_balances:
                # iterate through all combinations of all possible sizes
                # that could result in a valid 0-sum subgroup
                for subgroup_size in range(2, len(remaining_balances)+1):
                    for subgroup in itertools.combinations(remaining_balances, subgroup_size):
                        if sum(remaining_balances[person] for person in subgroup) == 0:
                            # we have found a zero-sum subgroup, seperate out this subgroup
                            # from remaining_balances, and push both back onto the stack
                            # for next recursion call
                            subgroup_balances = {}
                            for person in subgroup:
                                subgroup_balances[person] = remaining_balances.pop(person)
                            subgroups.append(subgroup_balances)
                            subgroups.append(remaining_balances)
                            
                            # recurse down
                            explore_subgroups()
                            
                            # once back up, we are done with searching through this case of
                            # remaining_balances, so we can re-join remaining_balances with
                            # the subgroup we seperate out, restoring state back to what we had,
                            # for subsequent subgroups in this for loop
                            remaining_balances = subgroups.pop()
                            subgroup_balances = subgroups.pop()
                            for person in subgroup_balances:
                                remaining_balances[person] = subgroup_balances[person]
            else:
                # we found a complete partition, simply update max_num_subgroups
                # this is the base case where recursion stops
                to_update['max_num_subgroups'] = max(to_update['max_num_subgroups'], len(subgroups))
            
            # push remaining_balances back onto stack to reset state back
            # to what the previous level had
            subgroups.append(remaining_balances)
        
        explore_subgroups()
        return len(balances) - to_update['max_num_subgroups']