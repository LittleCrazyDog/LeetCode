class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Constant defined for color drawing to person
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
        def helper(person_id, color):
            # Draw person_id as color
            color_table[person_id] = color
            
            # Draw the_color, with opposite color, in dislike table of current person_id
            for the_color in dislike_table[person_id]:
                if color_table[the_color] == color:
                    return False
                if color_table[the_color] == NOT_COLORED and (not helper(the_color, -color)):
                    return False
            
            return True
        
        if n == 1 or not dislikes:
            return True
        
        dislike_table = defaultdict(list)
        color_table = defaultdict(int)
        
        for p1, p2 in dislikes:
            dislike_table[p1].append(p2)
            dislike_table[p2].append(p1)
        
        for person_id in range(1, n+1):
            if color_table[person_id] == NOT_COLORED and (not helper(person_id, BLUE)):
                return False
        
        return True