class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not all([i for i in strs if i.__len__() < 1]):
            return ""
        if len(strs) == 1:
            return strs[0]
        if set([i[0] for i in strs]).__len__() != 1:
            return ""
        strs.sort(key=len)
        _max_iter = strs[0].__len__()
        _max = 0

        for i in range(_max_iter):
            if set([i[_max] for i in strs]).__len__() == 1:
                _max += 1
            else:
                break

        return strs[0][:_max]

class Solution2:
    def longestCommonPrefix(self, strs) -> str:
        if not all([i for i in strs if i.__len__() < 1]):
            return ""
        if len(strs) == 1:
            return strs[0]

        min_elem = min(strs, key=len)
        min_elem_idx = strs.index(min_elem)
        int_l = [[ord(i) for i in list(j)] for j in strs]
        zero_list = []
        s_elem = int_l.pop(min_elem_idx)
        for str_int in int_l:
            z_idx = 0
            for i, s in enumerate(s_elem):
                if s == str_int[i]:
                    z_idx += 1
                else:
                    break
            zero_list.append(z_idx)

        c_idx = min(zero_list)
        if c_idx == 0:
            return ""
        else:
            return min_elem[:c_idx]


