
from collections import defaultdict

def shortest_substring(str, set):

    sparse_str = [(i,c) for i,c in enumerate(str) if c in set]
    N = len(sparse_str)
    S = len(s)

    result_start, result_end, result_len = 0, N, float('inf')
    curr_left = 0
    rindex = defaultdict(list)   # an ordered list of indices where each c in set appears, with the indices curr_left <= i <= curr_right
    found_cnt = 0
    
    for curr_right, right_c in enumerate(sparse_str):
        if not len(rindex[c]):
            found_cnt += 1            
        rindex[c].append(curr_right)

        while found_cnt == S:   # [curr_left..curr_right] is a valid substring
            curr_len = curr_right - curr_left + 1
            if curr_len < result_len:
                result_start = curr_left
                result_end = curr_right
                result_len = curr_len
            left_c = str[curr_left]
            assert curr_left == rdict[left_c].pop(0)   # better to use a deque I guess
            
            if not len(rdict[c]):
        if found_cnt == S:  # End of valid substring (perhaps not shortest)
        
        while             

