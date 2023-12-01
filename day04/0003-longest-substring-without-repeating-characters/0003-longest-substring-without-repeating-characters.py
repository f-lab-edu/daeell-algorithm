class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        curr_word = []
        for string in s:
            if string not in curr_word:
                curr_word.append(string)
            else:
                while string in curr_word:
                    del curr_word[0]
                curr_word.append(string)
            max_length = max(max_length, len(curr_word))
        return max_length