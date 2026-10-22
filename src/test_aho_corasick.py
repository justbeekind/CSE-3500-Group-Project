import unittest

from aho_corasick import AhoCorasick

# Runs the algorithm and sorts the results
def run(patterns, text):
    return sorted(AhoCorasick(patterns).search(text))

class TestAhoCorasick(unittest.TestCase):

    # Original paper - "Aho & Corasick, 1975"
    # Tests the paper's example
    # The trie, failure links, and output links all together
    def test_textbook_example(self):
        self.assertEqual(
            run(["he", "she", "his", "hers"], "ushers"),
            [(1, "she"), (2, "he"), (2, "hers")],
        )

    # Tests output links
    # "he" ends at the same position as "she"
    # Without output links finds "she" and misses "he"
    def test_suffix_pattern(self):
        self.assertEqual(run(["she", "he"], "she"), [(0, "she"), (1, "he")])

    # Tests that patterns ending at internal trie nodes
    def test_pattern_prefix(self):
        self.assertEqual(
            run(["a", "ab", "abc"], "abc"),
            [(0, "a"), (0, "ab"), (0, "abc")],
        )

    # Tests overlapping occurrences of the same pattern
    def test_pattern_overlap(self):
        self.assertEqual(run(["aa"], "aaaa"), [(0, "aa"), (1, "aa"), (2, "aa")])

    # Tests failure links
    # After matching "abc", the "x" may mismatch "abcd"
    def test_failure_link(self):
        self.assertEqual(run(["abcd", "bcx"], "abcx"), [(1, "bcx")])

    def test_edge_cases(self):
        with self.subTest("empty text"):
            self.assertEqual(run(["a", "ab"], ""), [])
        with self.subTest("no matches"):
            self.assertEqual(run(["xyz", "qq"], "abcabc"), [])
        with self.subTest("single-char text and pattern"):
            self.assertEqual(run(["a"], "a"), [(0, "a")])
        with self.subTest("pattern longer than text"):
            self.assertEqual(run(["abcdef"], "abc"), [])

    # Tests on a long repetitive text ("abab...", 20000 chars)
    # "aba" overlaps itself at every even index and "ba" at every odd index
    def test_stress_large_repetitive_text(self):
        text = "ab" * 10000
        expected = sorted([(i, "aba") for i in range(0, len(text) - 2, 2)]
                        + [(i, "ba") for i in range(1, len(text) - 1, 2)]
        )

        result = run(["aba", "ba", "aab"], text)

        self.assertEqual(len(result), 19998)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()