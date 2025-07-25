def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()          # chars currently in the window
        left = 0              # start index of window
        max_len = 0

        for right, ch in enumerate(s):
            # shrink the window until no duplicate of ch remains
            while ch in seen:
                seen.remove(s[left])
                left += 1

            # expand the window to include ch
            seen.add(ch)
            max_len = max(max_len, right - left + 1)

        return max_len
