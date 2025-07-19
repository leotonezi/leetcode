def valid_parentheses(s: str) -> bool:
    """
    Determines if the input string has valid parentheses.

    Args:
        s: A string containing only the characters '(', ')', '{', '}', '[', ']'

    Returns:
        True if the input string is valid, False otherwise
    """
    # Map closing brackets to their opening counterparts
    brackets_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Use a stack to keep track of opening brackets
    stack = []

    for char in s:
        # If it's a closing bracket
        if char in brackets_map:
            # Pop the top element from stack if it's not empty, otherwise assign dummy value
            top_element = stack.pop() if stack else '#'

            # Check if the popped element matches the corresponding opening bracket
            if brackets_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push to stack
            stack.append(char)

    # If the stack is empty, all brackets have been matched
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    test_cases = [
        "()",          # Example 1          - should return True
        "()[]{}",      # Example 2          - should return True
        "(]",          # Example 3          - should return False
        "([)]",        # Additional test    - should return False
        "([])",        # Example 4          - should return True
        "{[]}",        # Additional test    - should return True
        "[[[]]]",      # Additional test    - should return True
        "]",           # Additional test    - should return False
        "({[)"         # Additional test    - should return False
    ]

    for i, test in enumerate(test_cases):
        result = valid_parentheses(test)
        print(f"Test case {i+1}: '{test}' -> {result}")
