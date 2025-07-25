def isPalindrome(s: str):
  left, right = 0, len(s) - 1

  while left < right:
    while left < right and not s[left].isalnum():
      left += 1
    while left < right and not s[right].isalnum():
      right -= 1

    if s[left].lower() != s[right].lower():
      return False
  pass


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
