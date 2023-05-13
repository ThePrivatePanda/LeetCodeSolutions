class Solution:  # second attempt :)
    def spiralOrder(self, matrix):
        pairs = []
        while matrix:
            pairs += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return pairs


class Solution2:  # first attempt
    def spiralOrder(self, matrix):
        i = 0
        j = 0
        ui = len(matrix[0])
        uj = len(matrix)
        li = 0
        lj = 1
        l_final = []
        while True:
            if i >= ui:
                break
            while i < ui:
                l_final.append(matrix[j][i])
                i += 1
            i -= 1
            j += 1
            if j >= uj:
                break
            while j < uj:
                l_final.append(matrix[j][i])
                j += 1
            j -= 1
            if i <= li:
                break
            while li < i:
                i -= 1
                l_final.append(matrix[j][i])
            if j <= lj:
                break
            while lj < j:
                j -= 1
                l_final.append(matrix[j][i])

            i += 1
            ui -= 1
            uj -= 1
            li += 1
            lj += 1
        return l_final
