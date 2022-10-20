class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, curr_list, nums_of_letters = [], [], 0
        for word in words:
            if nums_of_letters + len(word) + len(curr_list) > maxWidth:
                size = max(1, len(curr_list) - 1)
                for i in range(maxWidth - nums_of_letters):
                    index = i % size
                    curr_list[index] += ' '
                result.append(''.join(curr_list))
                curr_list, nums_of_letters = [], 0
            curr_list.append(word)
            nums_of_letters += len(word)
        final_line = ' '.join(curr_list)
        for _ in range(maxWidth - len(final_line)):
            final_line += ' '
        result.append(final_line)
        return result