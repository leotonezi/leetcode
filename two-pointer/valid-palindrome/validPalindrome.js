function isPalindrome(s) {
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    while (left < right && !s[left].isalnum()) {
      left++;
    }
    while (left < right && !s[right].isalnum()) {
      right--;
    }

    if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      return false;
    }
  }
}