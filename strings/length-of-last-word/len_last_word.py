def len_last_word(s):
  n = len(s) - 1
  count = 0
  while(True):
      print(s[n])
      if(s[n] == ' ' and count == 0):
          n -= 1
      elif(s[n] == ' ' and count > 0):
          break
      else:
          count += 1
          n -= 1
  return count


text = "Hello World"
len_last_word(text)