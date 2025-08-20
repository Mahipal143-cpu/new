def solve(input_data):
    """
    Correct solution to calculate weight of nested brackets.
    """
    s = input_data.strip()
    stack = []
    total_weight = 0

    for ch in s:
        if ch in "[{":
            # Push opening bracket with current depth
            stack.append((ch, len(stack)+1))
        elif ch == "]":
            if stack and stack[-1][0] == "[":
                _, depth = stack.pop()
                total_weight += 1 * depth
            else:
                # Invalid closing, reset stack
                stack.clear()
        elif ch == "}":
            if stack and stack[-1][0] == "{":
                _, depth = stack.pop()
                total_weight += 2 * depth
            else:
                # Invalid closing, reset stack
                stack.clear()

    return total_weight
