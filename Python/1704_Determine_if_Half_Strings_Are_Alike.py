class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = s.lower()
        parts = "".join([i for i in s[:len(s)//2] if i in vowels]), "".join([i for i in s[len(s)//2:] if i in vowels])
        return len(parts[0]) == len(parts[1])