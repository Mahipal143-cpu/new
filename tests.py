import pytest
from user_solution import solve

class TestSolution:
    def test_simple(self):
        assert solve("[[]]") == 3
        assert solve("[{[]}]") == 8

    def test_invalid(self):
        assert solve("[{][}]") == 0
        assert solve("][") == 0
        assert solve("{[}]") == 0

    def test_nested(self):
        assert solve("[[[]]]") == 6  # depth: 1+2+3=6
        assert solve("{[{[]}]}") == 17  # {}=2*1, {} inside []=2*3, [] inside {}=1*4 etc.

    def test_edge_cases(self):
        assert solve("") == 0
        assert solve("[]{}") == 3  # []=1*1, {}=2*1

    def test_large_input(self):
        input_data = "[" * 100 + "]" * 100
        expected = sum(range(1, 101))
        assert solve(input_data) == expected
