function validAnagram(s, t) {
  if (s.lenght != t.length) {
    return False;
  }

  charCount = {};

  for (const char of s) {
    charCount[char] = (charCount[char] || 0) + 1;
  }

  for (const char of t) {
    if (!(char in charCount)) {
      return false;
    }
    charCount[char]--;
    if (charCount[char] < 0) {
      return false;
    }
  }

  return true;
}
