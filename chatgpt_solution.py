def solve(input_data):
    """
    ChatGPT attempted solution: counts brackets but ignores nesting depth properly.
    """
    s = input_data.strip()
    total_weight = 0
    total_weight += s.count("[")  # Only counts number of '['
    total_weight += 2 * s.count("{")  # Only counts number of '{'
    return total_weight
