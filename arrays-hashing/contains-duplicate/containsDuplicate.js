function containsDuplicate(nums) {
  const already_seen = new Set();
  for (const num of nums) {
    if (already_seen.has(num)) {
      return true;
    }
    already_seen.add(num);
  }
  return false;
}
