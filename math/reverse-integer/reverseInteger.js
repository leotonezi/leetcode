function reverseInteger(x) {
  /**
   * Reverses the digits of a signed 32-bit integer.
   * Returns 0 if the result overflows 32-bit signed integer range.
   */
  const minSigned32bit = -(2 ** 31);
  const maxSigned32bit = 2 ** 31 - 1;

  const sign = x < 0 ? -1 : 1;
  const reversedStr = Math.abs(x).toString().split("").reverse().join("");
  const reversedNum = sign * parseInt(reversedStr);

  if (!(minSigned32bit <= reversedNum && reversedNum <= maxSigned32bit)) {
    return 0;
  }

  return reversedNum;
}

// Example usage:
console.log(reverseInteger(-495)); // Output: -594
console.log(reverseInteger(1534236469)); // Output: 0 (overflow)
console.log(reverseInteger(123)); // Output: 321
