class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        inverted_index = defaultdict(list)
        for i, ch in enumerate(source):
            inverted_index[ch].append(i)
        loop_cnt = 1
        i = -1
        for ch in target:
            if ch not in inverted_index: return -1
            offset_list_for_ch = inverted_index[ch]
            j = bisect_left(offset_list_for_ch, i)
            if j == len(offset_list_for_ch):
                loop_cnt += 1
                i = offset_list_for_ch[0] + 1
            else:
                i = offset_list_for_ch[j] + 1
        return loop_cnt