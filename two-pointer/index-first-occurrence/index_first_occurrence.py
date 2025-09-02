def strStr(self, haystack, needle):
  """
  :type haystack: str
  :type needle: str
  :rtype: int
  """
  if len(needle) > len(haystack):
      return -1
  
  # Check each possible starting position
  for i in range(len(haystack) - len(needle) + 1):
      # Check if needle matches at position i
      match = True
      for j in range(len(needle)):
          if haystack[i + j] != needle[j]:
              match = False
              break
      
      if match:
          return i
  
  return -1

# haystack = "sadbutsad", needle = "sad"