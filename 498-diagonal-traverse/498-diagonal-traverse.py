class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d = {}
        
        # loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    # if you're already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
        
        # we're done with the pass, let's build our answer array
        ans = []
        # look at the diagonal and each diagonal's elements
        for entry in d.items():
            # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
            # snake time, look at the diagonal level
            if entry[0] % 2 == 0:
                # Here we append in reverse order because its an even numbered level/diagonal.
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        
        return ans