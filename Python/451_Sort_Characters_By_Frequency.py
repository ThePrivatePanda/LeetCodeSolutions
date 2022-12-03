from collections import Counter # just so pylance doesn't scream at me :)

class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c * t for c, t in Counter(s).most_common())