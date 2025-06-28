function quickselect(arr, k) {
  if (arr.length === 1) return arr[0];

  // Choose random pivot
  const pivot = arr[Math.floor(Math.random() * arr.length)];

  // Partition
  const smaller = arr.filter((x) => x < pivot);
  const equal = arr.filter((x) => x === pivot);
  const larger = arr.filter((x) => x > pivot);

  // Recurse on appropriate partition
  if (k <= smaller.length) {
    return quickselect(smaller, k);
  } else if (k <= smaller.length + equal.length) {
    return pivot;
  } else {
    return quickselect(larger, k - smaller.length - equal.length);
  }
}

function findKthLargest(nums, k) {
  // kth largest = (n-k+1)th smallest
  return quickselect([...nums], nums.length - k + 1);
}

// Example
const nums = [3, 2, 1, 5, 6, 4];
const k = 4;
console.log(findKthLargest(nums, k)); // Output: 5
