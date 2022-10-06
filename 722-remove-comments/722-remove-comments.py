class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # 1. There are three important tokens we want to identify within the source code //, /*, and */
        # 2. We use a variable called buffer that acts as a buffer to store the characters that will
        #    definitely go into the final source code. This buffer can contain characters from multiple
        #    lines because of block comments.
        # 3. We use another variable block_comments_open to keep track of whether we are inside a block
        #    comment or not.
        # 4. At the end of each source line, we simply have to check whether we are inside of a block
        #    comment or not (i.e. block_comments_openn is True) to decide whether we want to flush the
        #    buffer and append it to the results.
        
        # In each loop, we have to check:
        # 1. // --- If it is a line comment and not part of a block comment, skip the rest of the line
        #           by shifting the pointer to the end of the line.
        # 2. /* --- If it is an opening block comment token and not part of a block comment, set
        #           block_comment_open to True
        # 3. */ --- If it is a closing block comment token and part of a block comment, set
        #           block_comment_open to False
        # 4. Else append to buffer if not part of a block comment
        
        res, buffer, block_comment_open = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                # "//" -> Line comment
                if char == '/' and (i+1) < len(line) and line[i+1] == '/' and not block_comment_open:
                    i = len(line)   # Advance pointer to end of current line
                # "/*" -> Start of block comment
                elif char == '/' and (i+1) < len(line) and line[i+1] == '*' and not block_comment_open:
                    block_comment_open = True
                    i += 1
                # "*/" -> End of block comment
                elif char == '*' and (i+1) < len(line) and line[i+1] == '/' and block_comment_open:
                    block_comment_open = False
                    i += 1
                # Normal character. Append to buffer if not in block comment
                elif not block_comment_open:
                    buffer += char
                i += 1
            if buffer and not block_comment_open:
                res.append(buffer)
                buffer = ''
        return res