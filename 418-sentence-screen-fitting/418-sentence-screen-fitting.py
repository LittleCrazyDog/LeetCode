class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        sentence_ptr = 0
        for i in range(rows):
            sentence_ptr += cols - 1
            # case 1: sentence_ptr at the end of screen falls exactly on the space
            if s[sentence_ptr % len(s)] == ' ':
                sentence_ptr += 1
            # case 2: sentence_ptr at the end of screen coincides with the last letter of a word (next is space)
            elif s[(sentence_ptr+1) % len(s)] == ' ':
                sentence_ptr += 2
            # case 3: sentence_ptr at the end of screen falls in the middle of a word; roll back
            else:
                while sentence_ptr > 0 and s[(sentence_ptr - 1) % len(s)] != ' ':
                    sentence_ptr -= 1
        return sentence_ptr // len(s)